a = {'age': {'1': 'yes', '0': {'student': {'1':'yes', '0': 'no'}}, '2': {'credit': {'1': 'no', '0': 'yes'}}}}
def getTreeDepth(mytree):
    maxDepth = 1
    firstStr = list(mytree.keys())[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys(): 
        if type(secondDict[key]).__name__=='dict': 
            thisDepth += getTreeDepth(secondDict[key]) 
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth

def getNumLeafs(mytree):
    numLeafs = 0
    firstStr = list(mytree.keys())[0]
    secondDict = mytree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs
decisionNode = dict(boxstyle = "sawtooth",fc="0.8")
leafNode = dict(boxstyle = "round4",fc="0.8")
arrow_args = dict(arrowstyle="<-")
def plotNode(nodeTxt,centerPt,parentPt,nodeType):






