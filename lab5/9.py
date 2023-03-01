import re
def test9(text):
    m = re.findall("[A-Z][a-z]*", text)
    print(' '.join(m)