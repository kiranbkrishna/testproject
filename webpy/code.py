import web
from web import form
import requests
from bs4 import BeautifulSoup as BS
import dryscrape
urls = ('/', 'index')

search_form = form.Form(form.Textbox('query'))
render = web.template.render('templates/')

class index:
    def GET(self):
        sf = search_form()
        return render.index(sf)

    def POST(self):
        f = search_form()
        
        if not f.validates():
            return render.index(f)
        else:
            search = f.get('query').value
            y = yahoo('abc')
            g = google('abc')
            dic = {}

            commons = [] 
            for i in y:
                dic[to_hashcode(i)] = i
            for i in g:
                if dic.get(to_hashcode(i)):
                    commons.append(i)
            return render.results("\t".join(commons))

def to_hashcode(s):
    h = 0
    for char in s:
        h = 31 * h + ord(char)
    return h
def get_soup(text):
    try:
        soup = BS(text.encode('ascii', 'ignore'))
    except Exception as e:
        soup = None
    return soup

def google(search):
    sess = dryscrape.Session(base_url = 'http://google.co.in')
    sess.set_attribute('auto_load_images', False)
    sess.visit('/')
    q = sess.at_xpath('//*[@name="q"]')
    q.set(search)
    q.form().submit()
    soup = get_soup(sess.body())
    try:
        div = soup.find('div', {'id':'search'})        
    except Exception as e:
        div = None
    if div:
        sites = [i.text.strip("/") for i in div.findAll('cite')]
        return sites
    return []

def yahoo(search):
    print "Yahoo"
    url = "http://in.search.yahoo.com/search?p="  + search
    res = requests.get(url)
    soup = get_soup(res.text)
    ret = []
    for tag in soup.findAll('div', {'class':'compTitle options-toggle'}):
         ret.append(tag.findChildren('div')[0].find('span').text.strip('/'))
    return ret


if __name__ == 	"__main__":
    app = web.application(urls, globals())
    app.run()
