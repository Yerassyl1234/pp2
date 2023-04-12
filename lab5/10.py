import re
def test10(text):
    print('_'.join(
        re.sub('([A-Z][a-z]+)', r' \1',
        re.sub('([A-Z]+)', r' \1',
        text.replace('-', ' '))).split()).lower())
a=input()
test10(a)