#Kyra Abbu

def compress_word(w):
    i = 1
    newl = []
    vowel = "AEIOUaeiou"
    newl.append(w[0].lower())
    while i < len(w):
        if w[i] not in vowel:
            value = w[i].lower()
            newl.append(value)
        i = i + 1
    return ''.join(newl)
    
            
print(compress_word("halloween")) #hllwn
print(compress_word("Special")) #spcl
print(compress_word("apple")) #appl
print(compress_word("oRaNge")) #orng

def sentence(line):
    newl = []
    sen = line.split(" ")
    for element in sen:
        new_sen = compress_word(element)
        newl.append(new_sen)
    return " ".join(newl)
    


print(sentence("I like to eat apple pie.")) #i lk t et appl p
print(sentence("Who is there")) #Wh is thr
    