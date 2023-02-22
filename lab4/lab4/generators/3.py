def div(nums):
    for i in nums:
        if i%3 == 0 and i%4 == 0:
            yield i
n = int(input())
a = div([int(i) for i in range(n)])
for i in a:
    print(i)