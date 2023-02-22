def squares(nums):
    for i in nums:
        yield (i*i)
a = squares(map(int,input().split()))
for i in a:
    print(i)