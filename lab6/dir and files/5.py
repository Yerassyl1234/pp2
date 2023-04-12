fileW = open("list.txt",'w')
l = list(input().split())
for i in l:
    fileW.write(i.__str__()+" ")
fileW.close()
