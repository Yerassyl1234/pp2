import re
def test3():
    text = "(777) 255-84-44  (775) 265-85-43 (ffd) 254-34-23 (777)534-32-21"
    pattern = "[(]\d{3}[)] \d{3}[-]\d{2}[-]\d{2}"
    x = re.findall(pattern, text)
    print(x)