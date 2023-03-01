import re
txt=input()
txt=re.findall("ab{2,3}",txt)
print(txt)