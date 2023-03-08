fileR = open("sample.txt",'r')
c = 0
for line in fileR:
    c+=1
print(c)
fileR.close()