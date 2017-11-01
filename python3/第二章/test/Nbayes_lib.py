# -*- coding: utf-8 -*-
import sys  
import os 
import numpy as np

#简单的数据，关注算法本身
def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him','my'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec


class NBayes(object):
    def __init__(self):
	self.vocabulary = [] # 词典
	self.idf=0           # 词典的idf权值向量
	self.tf=0            # 训练集的权值矩阵
	self.tdm=0           # P(x|yi)
	self.Pcates = {}     # P(yi)--是个类别字典
	self.labels=[]       # 对应每个文本的分类，是个外部导入的列表
	self.doclength = 0   # 训练集文本数
	self.vocablen = 0    # 词典词长
	self.testset = 0     # 测试集

        # 加载训练集并生成词典，以及tf, idf值
    def train_set(self,trainset,classVec):
        print(classVec,"classVec")
	self.cate_prob(classVec)   # 计算每个分类在数据集中的概率：P(yi) 
	self.doclength = len(trainset) 
	tempset = set()
	[tempset.add(word) for doc in trainset for word in doc ] # 生成词典
        self.vocabulary = list(tempset) 
	self.vocablen = len(self.vocabulary)
	self.calc_wordfreq(trainset)
	# self.calc_tfidf(trainset)  # 生成tf-idf权值
	self.build_tdm()           # 按分类累计向量空间的每维值：P(x|yi)
	
        # 测试集映射到当前词典
    def map2vocab(self,testdata):
	self.testset = np.zeros([1,self.vocablen])
	for word in testdata:
	    self.testset[0,self.vocabulary.index(word)] +=1		
	
        # 生成普通的词频向量					
    def calc_wordfreq(self,trainset):
	self.idf = np.zeros([1,self.vocablen]) # 1*词典数
	self.tf = np.zeros([self.doclength,self.vocablen]) # 训练集文件数*词典数
	for indx in xrange(self.doclength):    # 遍历所有的文本
	    for word in trainset[indx]:          # 遍历文本中的每个词
		self.tf[indx,self.vocabulary.index(word)] +=1  # 找到文本的词在字典中的位置+1
	    for signleword in set(trainset[indx]):              
		self.idf[0,self.vocabulary.index(signleword)] +=1 

        # 计算每个分类在数据集中的概率：P(yi)
    def cate_prob(self,classVec):		
	self.labels = classVec
        #print(self.labels)
	labeltemps = set(self.labels) # 获取全部分类
        #print(labeltemps)
	for labeltemp in labeltemps:  
	    # 统计列表中重复的值：self.labels.count(labeltemp)
	    self.Pcates[labeltemp] = float(self.labels.count(labeltemp))/float(len(self.labels))
        print(self.Pcates)
	    
        # 输出分类类别		
    def predict(self,testset):
	if np.shape(testset)[1] != self.vocablen:
	    print "输入错误"
	    exit(0)
	predvalue = 0
	predclass = ""
	for tdm_vect,keyclass in zip(self.tdm,self.Pcates):
	    # P(x|yi)P(yi)
	    temp = np.sum(testset*tdm_vect*self.Pcates[keyclass])
	    if temp > predvalue:
		predvalue = temp
		predclass = keyclass
	return predclass
	
	#按分类累计向量空间的每维值：P(x|yi)
    def build_tdm(self):
	self.tdm = np.zeros([len(self.Pcates),self.vocablen]) #类别行*词典列
	sumlist = np.zeros([len(self.Pcates),1])  # 统计每个分类的总值
	for indx in xrange(self.doclength):
	    self.tdm[self.labels[indx]] += self.tf[indx]  # 将同一类别的词向量空间值加总
	    sumlist[self.labels[indx]]= np.sum(self.tdm[self.labels[indx]])  # 统计每个分类的总值--是个标量
	self.tdm = self.tdm/sumlist	  # P(x|yi)
	
dataSet,listClasses = loadDataSet()
nb = NBayes()
nb.train_set(dataSet,listClasses)
nb.map2vocab(dataSet[3])
print nb.predict(nb.testset)
