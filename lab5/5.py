import re
def test5(text):
    pattern = "a.+b$"
    m = re.findall(pattern, text)
    print(m)
a=input()
test5(a)