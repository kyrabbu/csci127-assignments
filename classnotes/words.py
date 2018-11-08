s = "one one one two two three three three three four four nine nine nine five five six seven nine nine "

def build_word_counts(words):
    d = {}
    #for a in b.split():
        #d[a] = 0
    for word in words.split():
        d.setdefault(word,0) #if not yet in list, add
        d[word] = d[word]+1
    return d

def clean_string(words):
    

f = open("macbeth.txt")
s = f.read()
words = build_word_counts(s)
print(words)


    