def areaTrap(height,bfirstval,bsecondval):
    s = ((bfirstval+bsecondval)/2)*height
    return s
h = int(input())
a = int(input())
b = int(input())
print(areaTrap(h,a,b))