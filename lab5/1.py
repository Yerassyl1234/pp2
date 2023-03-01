import re
txt=input()
txt=re.findall("ab*",txt)
print(txt)