import os
import json
import recommender as rec
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    majors,levels = rec.profileOptions()
    return render_template('index.html',majors=majors,levels=levels)

@app.route('/tags')
def tags():
    major = request.args.get("major")
    tags = rec.recConcentrations(major)
    return render_template('tags.html',tags=tags)

@app.route('/recs',methods=['GET', 'POST'])
def recs():
    major = request.args.get("major")
    level = request.args.get("level")
    concen = json.loads(request.args.get("concen"))
    userProfile = rec.profile(major,level,concen)
    courses,teachers = rec.recCourseTeachers(userProfile)
    return render_template('recs.html',courses=courses,teachers=teachers)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000)) 
    app.run(host='0.0.0.0', port=port,debug=True)
