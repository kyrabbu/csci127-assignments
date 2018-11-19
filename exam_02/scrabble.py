def score(w):
    w = w.upper()
    d = {}
    letters = "AEIOULNRSTDGBCMPFHVWYKJXQZ"
    total = 0
    for item in letters:
        d.setdefault(item,0)
        if item in "AEIOULNRST":
            d[item] = 1
        if item in "DG":
            d[item] = 2
        if item in "BCMP":
            d[item] = 3
        if item in "FHVWY":
            d[item] = 4
        if item in "K":
            d[item] = 5
        if item in "JX":
            d[item] = 8
        if item in "QZ":
            d[item] = 10
    for string in w:
        if string in d.keys():
            total = total + d[string]
    return total


print("hello", score("hello"))
print("goodbye",score("goodbye"))
print("TeStIng", score("TeStIng"))
print("tHisisAlOngWord",score("tHisisAlOngWord"))
print("pneumonoultramicroscopicsilicovolcanoconiosis",score("pneumonoultramicroscopicsilicovolcanoconiosis"))
