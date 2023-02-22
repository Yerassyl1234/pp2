from cmath import pi
def degtorad(num):
    x = (num*pi)/180
    return x
a = int(input())
print(degtorad(a))