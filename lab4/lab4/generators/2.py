def evens(nums):
    for i in nums:
        if i%2==0:
            yield (i)
n = int(input())
a = evens([int(i) for i in range(n)])
for i in a:
    print(i)