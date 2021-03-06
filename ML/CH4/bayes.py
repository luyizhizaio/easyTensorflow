# -*- coding: utf-8 -*-
__author__ = 'tend'
from numpy import *



#从文本构建词向量

def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]

    classVec = [0,1,0,1,0,1] #1
    return postingList,classVec


#包含所有单词的列表
def createVocabList(dataSet):
    vocabSet = set([]) #创建一个空集里面是数组
    for document in dataSet:
        vocabSet = vocabSet | set(document) #并集,Set是排重的
    return list(vocabSet)


#输出文档向量
def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList) #生成长度为len的列表
    for word in  inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] =1  #把单词相应的位置标示为1.
        else: print "the word: %s is not in my Vocabulary !" % word
    return returnVec


#执行
#listOPosts,listClasses = loadDataSet()

#myVocabList = createVocabList(listOPosts)

#print myVocabList


#print setOfWords2Vec(myVocabList,listOPosts[0])



#bayes 分类器训练函数
def trainNB0(trainMatrix,trainCategory):
    #训练样本的数量
    numTrainDocs = len(trainMatrix)
    #样本的特征数
    numWords = len(trainMatrix[0])
    #正样本的比例
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    #创建数组
    p0Num=zeros(numWords)
    p1Num = zeros(numWords)
    #每个类别的总词数
    p0Denom =0.0;p1Denom =0.0
    for i in range(numTrainDocs):
        if trainCategory[i] ==1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vec = p1Num/p1Denom #类型为1的条件下每个词的频率。
    p0Vec = p0Num/p0Denom
    return p0Vec,p1Vec,pAbusive


#执行
listOPosts,listClasses = loadDataSet()

myVocabList = createVocabList(listOPosts)

trainMat = [] #创建一个矩阵
for postInDoc in listOPosts:
    trainMat.append(setOfWords2Vec(myVocabList,postInDoc))

p0V,p1V,pAb = trainNB0(trainMat,listClasses)

print(pAb)

print(p0V)


#根据显示情况修改分类器

#使用贝叶斯是计算概率的积时，如果一个概率为0，最后得到的概率也为0；可以将所有的词初始化为1，并将坟墓初始化为2

#bayes 分类器训练函数
def trainNB02(trainMatrix,trainCategory):
    #训练样本的数量
    numTrainDocs = len(trainMatrix)
    #样本的特征数
    numWords = len(trainMatrix[0])
    #正样本的比例
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    #创建数组
    p0Num=ones(numWords)
    p1Num = ones(numWords)
    #每个类别的总词数
    p0Denom =2.0;p1Denom =2.0
    for i in range(numTrainDocs):
        if trainCategory[i] ==1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vec = log(p1Num/p1Denom) #类型为1的条件下每个词的频率。
    p0Vec = log(p0Num/p0Denom)
    return p0Vec,p1Vec,pAbusive  #返回结果：分类为0的各词的概率向量，分类为1的各词的概率向量，数据集中正样本的比例



#朴素贝叶斯份分类函数
def classifyNB(vec2Classify,p0Vec,p1Vec,pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1) #防止下溢问题，返回的概率是带log的，所以这里也带个log。
    p0 = sum(vec2Classify * p0Vec) + log(1 - pClass1)
    if p1 > p0: #那个概率高就属于哪个分类，log函数是个单调增函数，所以对结果没影响。
        return 1
    else:
        return 0

#测试NB函数
def testingNB():
    #加载训练数据
    listOPosts,listClass = loadDataSet()
    #生成词汇表
    myVocabList = createVocabList(listOPosts)
    #训练数据集的矩阵
    trainMat=[]
    for postInDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList,postInDoc))

    #各值：分类为0的各词的概率向量，分类为1的各词的概率向量，数据集中正样本的比例
    p0V,p1v,pAb = trainNB02(array(trainMat),array(listClasses))
    testEntry = ['love','my','dalmation']
    #返回测试集向量
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))

    print testEntry,'classified as :',classifyNB(thisDoc,p0V,p1v,pAb)
    testEntry = ['stupid','garbage']
    thisDoc = array(setOfWords2Vec(myVocabList,testEntry))
    print testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb)


#执行
testingNB()
#



#词袋模型处理数据特征
def bagOfWords2VecMN(vocabList,inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] +=1
    return returnVec



















