from numpy import *
import os
def file2matrix(path,delimiter):	
    with open(path) as fp:
        rowlist = fp.read().splitlines()
    return mat([row.split(delimiter) for row in rowlist if row.strip()])

print([shape(file2matrix("testdata/"+path,"\t")) for path in os.listdir("testdata")])
