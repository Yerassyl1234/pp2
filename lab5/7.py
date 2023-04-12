import re
def test7(text):
    print(''.join(x.capitalize() or '_' for x in text.split('_')))
a=input()
test7(a)