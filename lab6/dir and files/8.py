import os 
def delete(path):
    if os.access(path,os.X_OK):
        os.remove(path)
    else:
        print("no such path")
a = input()
delete(a)