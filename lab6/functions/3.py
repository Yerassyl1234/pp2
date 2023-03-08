a = input()
b = "".join(list(reversed(a)))
if b == a:
    print("yes")
else:
    print("no")