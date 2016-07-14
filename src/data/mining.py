import os
import nltk
import json
import rake
import numpy
import string
import operator
from collections import Counter
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from nltk.stem.porter import PorterStemmer

def get_json_data(path):
    courses = []
    with open(path,'r') as text_file:
        for line in text_file:
            courses.append(json.loads(line))
    return courses

def convert_json_to_str(data,key):
    json_str = str()
    for d in data:
        json_str += str(d[key])
    return json_str

def convert_json_to_str_arr(data,key):
    str_arr = []
    for d in data:
        str_arr.append(str(d[key]))
    return str_arr

def get_tokens(path):
    courses = get_json_data(path)
    course_desc = convert_json_to_str(courses,'desc')
    course_desc = course_desc.lower()
    no_puncutuation = course_desc.translate(None,string.punctuation)
    tokens = nltk.word_tokenize(no_puncutuation)
    return tokens

def removeStopWord(tokens):
    filtered = [w for w in tokens if not w in stopwords.words('english')]
    return filtered

def stem_tokens(tokens,stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    stemmer = PorterStemmer()
    stems = stem_tokens(tokens,stemmer)
    return stems

def tdidf(text):
    tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
    tfs = tfidf.fit_transform(text)
    print tfidf.get_feature_names()

def writeDataToFile(data,path):
    with open(path,'w') as file:
        for line in data:
            file.write(str(line)+"\n")

if __name__ == "__main__":

    path = 'course_data.json'
    courses = get_json_data(path)
    course_desc = convert_json_to_str_arr(courses,'desc')

    count_vect = CountVectorizer()
    course_count = count_vect.fit_transform(course_desc)
    #numpy.savetxt("count.csv",course_count.toarray(),delimiter=",")

    tf_transformer = TfidfTransformer()
    course_tf = tf_transformer.fit_transform(course_count)
    #numpy.savetxt("tdidf.csv",course_tf.toarray(),delimiter=",")

    tdidf_sim = (course_tf * course_tf.T).A
    numpy.savetxt("tdidf_sim.csv",tdidf_sim,delimiter=",")

    '''
    # Test tokenizer
    tokens = get_tokens(path)
    tokens_filtered = removeStopWord(tokens)
    count = Counter(tokens_filtered)
    print count.most_common(100)

    # Test stemer
    stemmer = PorterStemmer()
    stemmed = stem_tokens(tokens,stemmer)
    count = Counter(stemmed)
    # print count.most_common(5)
    
    # Test tdidf
    json_data = get_json_data(path)
    json_str = convert_json_to_str(json_data,'desc')
    tdidf(json_str)

    # RAKE
    rake_object = rake.Rake("SmartStoplist.txt")
    keywords = rake_object.run(course_desc)

    with open('course_keywords.txt','w') as ck:
        for keyword in keywords:
            ck.write(keyword[0]+"\n")

    # Write keywords computed by sklearn
    with open('keywords.txt','w') as file:
        for key in count_vect.vocabulary_:
            file.write(key+","+str(count_vect.vocabulary_[key])+"\n")
    '''





