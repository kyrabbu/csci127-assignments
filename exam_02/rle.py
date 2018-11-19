def encode(string):
    l = []
    count = 1
    for i in range(len(string)):
        #print(i)
        if  i == len(string)-1 or string[i] != string[i+1]:
            l.append([string[i], count])
            count = 1
        else:
            count = count + 1
    return l

def decode(list):
    result = ""
    for item in list:
        result = result + item[0]*item[1]
    return result

#print("Program will return empty list if no letters are found.")
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))
#print(encode(" "))
#print(encode("__"))
print(encode("AbCdEfCoNd"))

#print("\nProgram will not return anything if input does not contain letters OR is not a letter.")
print(decode(encode("abbaaacddaaa")))
print(decode(encode("abcd")))
print(decode(encode("cbbbbbdee")))
#print(decode(encode(" ")))
#print(decode(encode("__")))
print(decode(encode("AbCdEfCoNd")))
#print(decode(encode("hell0")))

