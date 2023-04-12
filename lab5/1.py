import re
txt=input()
text=re.findall("^b*",txt)
print(text)