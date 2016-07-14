from BeautifulSoup import BeautifulSoup as Soup
import urllib
import hashlib
import os
import sys

def download(url):
    print 'dowloading...'+url
    try:
        return urllib.urlopen(url).read()
    except:
        return ''

def cache_download(url):
    filename =  hashlib.sha1(url).hexdigest()
    if os.path.exists(filename):
        return open(filename).read()
    else:
        html = download(url)
        open(filename,'w').write(html)
        return html

def combine(url, path):
    if '://' in path:
        return path
    if path.startswith('//'):
        return url.split('//')[0]+path
    elif path.startswith('/'):
        base = '/'.join(url.split('/')[:3]) # http://domain.com
        return base + path
    else:
        items = url.split('/')
        n = max(3,len(items)-1)
        base = '/'.join(items[:n]) # http://domain.com
        return base + '/' + path

def crawl(url):
    filter = '/'.join(url.split('/')[:3])

    list_of_processed_urls = []
    list_of_urls_to_process = [url]

    while list_of_urls_to_process:
        url = list_of_urls_to_process.pop()
        list_of_processed_urls.append(url)

        print 'processing...'+url
        html = cache_download(url)
        soup = Soup(html)    
        links = soup.findAll('a')
        for link in links:
            if link.get('href') and not link['href'].startswith('mailto:'):
                new_url = combine(url, link['href'])
                if (not new_url in list_of_processed_urls and
                    new_url.startswith(filter)):
                    list_of_urls_to_process.append(new_url)
                    print '   discovered: '+new_url
    
        imgs = soup.findAll('img')
        for img in imgs:
            src = combine(url, img['src'])
            if src.split('.')[-1].lower() in ('png','gif','jpg','jpeg'):
                data = cache_download(src)
                filename = os.path.join('images',src.split('/')[-1])
                open(filename,'w').write(data)
                # sys.exit(0)

crawl('http://xkcd.com/')
