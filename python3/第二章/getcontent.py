import requests
from lxml import etree,html
from bs4 import BeautifulSoup
webdata = requests.get('http://www.163.com')
webpage = BeautifulSoup(webdata.text,"lxml")
page = html.document_fromstring(str(webpage))
text = page.text_content()
print(text) 
