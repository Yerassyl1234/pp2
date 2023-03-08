import os
def ifExist(path):
    if os.path.exists(path):
        for i in os.listdir(path):
            if os.path.isfile(os.path.join(path, i)):
                print(i)
    else:
        print("no such path")
a = input()
ifExist(a)   