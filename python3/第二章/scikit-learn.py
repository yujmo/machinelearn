import pickle
from sklearn.datasets.base import Bunch
from sklearn import  feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

def readbunchobj(path):
    file_obj = open(path,"rb")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writebunchobj(path,bunchobj):
    file_obj = open(path,"wb")
    pickle.dump(bunchobj,file_obj)
    file_obj.close()
def readfile(path):
    fp = open(path,"rb")
    content = fp.read()
    fp.close()
    return content

stopword_path = "train_word_bag/hlt_stop_words.txt"
stpwrdlst = readfile(stopword_path).splitlines()

path = "train_word_bag/train_set.dat"
bunch = readbunchobj(path)

tfidfspace = Bunch(target_name = bunch.target_name,label = bunch.label,filename = bunch.filenames,tdm =
                   [],vocabulary={})
vectorizer = TfidfVectorizer(stop_words=stpwrdlst,sublinear_tf = True,max_df = 0.5)
transformer = TfidfTransformer()
tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_
space_path = "train_word_bag/tfdifspace.dat"
writebunchobj(space_path,tfidfspace)


    
