import re
def test2():
    text = "http://glkjdfg.gldkfj https://gdfgkjfd.gfgdfsg"
    pattern = r"^http://\w+|https://\w+"
    x = re.findall(pattern, text)
    print(x)