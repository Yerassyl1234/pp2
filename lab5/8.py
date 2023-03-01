import re
def test8(text):
    print(re.findall("[A-Z][^A-Z]*", text)