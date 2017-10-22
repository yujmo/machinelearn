import chardet
import urllib
data1 = urllib.urlopen('http://www.163.com').read()
chardit1 = chardet.detect(data1)
print(chardit1)
