import os
def listOfAllFiles(a):
    print("All folders in this path: ")
    for i in os.listdir(a):
        if os.path.isdir(os.path.join(a, i)):
            print(i)
    print("\nAll files in this path: ")
    for i in os.listdir(a):
        if os.path.isfile(os.path.join(a, i)):
            print(i)
    print("\nAll files and folders: ")
    for i in os.listdir(a):
        print(i)
a = input()
listOfAllFiles(a)