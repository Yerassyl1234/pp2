a = tuple(input().split())
print(any(a))
# tuple is False when tuple is empty, so output will be False, when input = None
print(all(a))
# but task is asking us if all ELEMENTS of tuple are true so all would be correct in this case  