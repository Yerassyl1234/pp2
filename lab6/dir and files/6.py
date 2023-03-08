l = [] 
for i in range(65,91):
    l.append(chr(i))
for i in l:
    fileW = i + ".txt"
    with open(fileW,'w') as file:
        file.write(fileW)
