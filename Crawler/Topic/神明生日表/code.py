from bs4 import BeautifulSoup
import requests


html = requests.get('https://raw.githubusercontent.com/PYRF1215/NoteBook/master/Crawler/Topic/%E7%A5%9E%E6%98%8E%E7%94%9F%E6%97%A5%E8%A1%A8/data.html').text
# https://www.365fruit.com/RE_gods_birth.html

sp = BeautifulSoup(html,'html5lib')

fd = sp.find_all("tr","chbg")
for x in fd:
    print([s for s in x.stripped_strings])