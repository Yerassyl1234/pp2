import re
def test3(text):
    m = re.split("_", text)
    result = []
    for i in range(len(m) - 1):
        if m[i] != ' ' and m[i + 1] != ' ' and m[i].islower() and m[i + 1 ].islower():
            result.append(f"{m[i]}_{m[i+1]}")
    print(result)