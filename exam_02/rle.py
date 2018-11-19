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

def decode(list):
    d = {}
    result = ""
    for item in list:
        d.setdefault(item[0],0)
        d[item[0]] = item[1]
    for k in d:
        repeat = k * d[k]
        result = result + repeat
    return result

#tests
print("Program will return empty list if no letters are found.")
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))
print(encode(" "))
print(encode("__"))
print(encode("AbCdEfCoNd"))

print("\nProgram will not return anything if input does not contain letters OR is not a letter.")
print(decode(encode("abbaaacddaaa")))
print(decode(encode("abcd")))
print(decode(encode("cbbbbbdee")))
print(decode(encode(" ")))
print(decode(encode("__")))
print(decode(encode("AbCdEfCoNd")))
print(decode(encode("hell0")))





        






        