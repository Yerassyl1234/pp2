import re
def test6(text):
    m = re.sub("[,. ]", ":", text)
    print(m)
a=input()
test6(a)