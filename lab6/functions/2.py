a = input()
k = 0
c = 0
for i in a:
    if i.islower():
        c+=1
for i in a:
    if i.isupper():
        k+=1
print("num of upper case letters:",k)
print("num of lower case letters",c)