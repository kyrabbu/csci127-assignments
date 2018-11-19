def encode(string):
    l = []
    d = {}
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    for i in string:
        if i in alphabet:
            d.setdefault(i,0)
            d[i] = d[i] + 1
    for k,v in d.items():
        list = []
        list.append(k)
        list.append(v)
        l.append(list)
        #print(list)
    return l

#tests
print("Program will return empty list if no letters are found.")
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))
print(encode(" "))
print(encode("__"))

        