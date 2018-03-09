# -*- coding: utf-8 -*-
__author__ = 'tend'

import matplotlib.pyplot as plt


decisionNode = dict(boxstyle ="sawtooth",fc ="0.8")
leafNode = dict(boxstyle="round4",fc="0.8")
arrow_args=dict(arrowstyle="<-")


#使用注解画节点
def plotNode(nodeTxt,centerPt,parentPt,nodeType):
    createPlot2.ax1.annotate(nodeTxt,xy=parentPt,xycoords='axes fraction',
                            xytext=centerPt,textcoords='axes fraction',
                            va ="center",ha="center",bbox=nodeType,arrowprops=arrow_args)


def createPlot2():
    fig = plt.figure(1,facecolor='white')
    fig.clf()
    #创建子图
    createPlot2.ax1 = plt.subplot(111,frameon =False)
    plotNode('a decision node',(0.5,0.1),(0.1,0.5),decisionNode)
    plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()




#执行
#createPlot()



#构造注解树

#获取叶子节点数量和树的层数
def getNumLeafs(myTree):
    numLeafs =0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for  key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict': #判断类型
            numLeafs +=getNumLeafs(secondDict[key])
        else: numLeafs +=1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth =0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            thisDepth = 1+ getTreeDepth(secondDict[key])
        else: thisDepth =1
        if thisDepth > maxDepth:maxDepth = thisDepth

    return maxDepth



#构造树
def retrieveTree(i):
    #定义一个list
    listOfTrees =[{'no surfacing':{0:'no',1:{'flippers':{0:'no',1:'yes'}}}},
                  {'no surfacing':{0:'no',1:{'flippers':{0:{'head':{0:'no',1:'yes'}},1:'no'}}}}
                  ]
    return listOfTrees[i]

#execute
myTree =retrieveTree(0)

print getNumLeafs(myTree)

print getTreeDepth(myTree)



#plotTree函数

def plotMidText(cntrPt,parentPt,txtString):
    xMid =(parentPt[0]-cntrPt[0]/2.0 + cntrPt[0])
    yMid = (parentPt[1] - cntrPt[1]/2.0 + cntrPt[1])
    createPlot.ax1.text(xMid,yMid,txtString)


def plotTree(myTree,parentPt,nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]
    cntrPt = (plotTree.xoff + (1.0 + float(numLeafs))/2.0/plotTree.totalW,plotTree.yOff)















