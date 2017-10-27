import matplotlib.pyplot as plt  
decisionNode = dict(boxstyle="sawtooth", fc="0.8") 
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")  

def plotNode(Nodename, centerPt, parentPt, nodeType):  
    creatPlot.ax1.annotate(Nodename, xy=parentPt, xycoords='axes fraction', xttest=centerPt, textcoords='axes fraction', va="center", ha="center", bbox=nodeType, arrowprops=arrow_args) 

def creatplot():
    fig = plt.figure(1, facecolor='white')
    fig.clf() 
    creatplot.ax1 = plt.subplot(111,frameon=False)  
    plotNode('decision Node', (0.5,0.1), (0.1,0.5), decisionNode)
    plotNode('leaf Node', (0.8,0.1), (0.3,0.8), leafNode)
    plt.show()

def getNumleafs(myTree): 
    #初始化树的叶子节点个数
    Numleafs = 0 
    firstStr = list(mytree.keys())[0] 
    secondDict = mytree[firstStr]  
    for key in secondDict.keys(): 
        if type(secondDict[key]).__name__=='dict': 
            Numleafs += getNumleafs(secondDict[key]) 
        else:
            Numleafs += 1
    return Numleafs

def getTreeDepth(mytree):
    maxDepth = 0
    thisDepth = 0
    firstStr = list(mytree.keys())[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys(): 
        if type(secondDict[key]).__name__=='dict': 
            thisDepth += getTreeDepth(secondDict[key]) 
        else:
            Numleafs = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def plotMidText(cntrPt, parentPt, txtString):  
    xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
    yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
    creatPlot.ax1.text(xMid, yMid, txtString)  
def plotTree(myTree, parentPt, nodeName):  
    numleafs = getNumleafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff+(0.5/plotTree.totalw+float(numleafs)/2.0/plotTree.totalw), plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeName) 
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD 
    for key in secondDict.keys():
        if type(secondDict[key]).__name__=='dict':
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalw
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD

def creatPlot(inTree):  
    fig = plt.figure(1, facecolor='white')
    fig.clf()  
    axprops = dict(xticks=[], yticks=[]) 
    creatPlot.ax1 = plt.subplot(111, frameon=False, **axprops) 
    plotTree.totalw = float(getNumleafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))  
    plotTree.xOff = -0.5/plotTree.totalw 
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5,1.0), '')
    plt.show()

a = {'age': {'1': 'yes', '0': {'student': {'1': 'yes', '0': 'no'}}, '2': {'credit': {'1': 'no', '0': 'yes'}}}}

creatPlot(a)
