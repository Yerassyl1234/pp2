import re
def test4(text):
    pattern = "[A-Z][a-z]+"
    m = re.findall(pattern, text)
    print(m)
a = input()
test4(a)