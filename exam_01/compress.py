#Kyra Abbu

def compress_word(w):
    i = 1
    newl = []
    vowel = "AEIOUaeiou"
    newl.append(w[0].lower())
    while i < len(w):
        if w[i] not in vowel:
            newl.append(w[i])
        i = i + 1
    print(''.join(newl))
            
compress_word("halloween") #hllwn
compress_word("Special") #spcl
compress_word("apple") #appl

def sentence(line):
    x = compress_word(line)
    return x
    
sentence("I like to eat apple pie.") #i lk t t ppl p
sentence("Who is there")
    