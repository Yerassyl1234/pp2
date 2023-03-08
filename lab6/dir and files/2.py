import os
def existense(path):
    print(os.access(path, os.F_OK))
def readabilty(path):
    print(os.access(path,os.R_OK))
def writeability(path):
    print(os.access(path,os.W_OK))
def executability(path):
    print(os.access(path,os.X_OK))
a = input()
existense(a)
readabilty(a)
writeability(a)
executability(a)