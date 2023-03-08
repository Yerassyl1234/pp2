fileR = open("sample.txt",'r')
fileW = open("sample1.txt",'w')
for i in fileR:
    fileW.write(i.__str__())