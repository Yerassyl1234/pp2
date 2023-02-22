def downToZero(num):
    for i in range(num,-1,-1):
        yield i
a = downToZero(int(input()))
for i in a:
    print(i)