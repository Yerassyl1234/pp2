import re
def test1():
    text = "cat cot car c._oat cut"
    pattern = "[c]\S*[t]"
    x = re.findall(pattern, text)
    print(x)