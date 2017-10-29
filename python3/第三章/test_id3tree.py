from ID3DTree import *
import treePlotter as tp
dtree = ID3DTree()
dtree.loadDataSet("dataset.dat",["age","revenue","student","credit"])
dtree.train()
tree = dtree.tree
tp.createPlot(tree)
