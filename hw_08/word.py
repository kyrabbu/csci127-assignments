def build_word_count(words):
    d = {}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(string):
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    punctuations = """`~!@#$%^&*()_+{}[]|\:"<>?;',./"""
    result = "" #string
    string = clean_apos(string)
    for a in string:
        if a in alphabet:
            result = result + a.lower()
        elif a in punctuations:
            result = result + ""
        else:
            result = result + " "
    return result

def clean_apos(string):
    result = ""
    result = result + string[0]
    for i in range(1,len(string)):
        if string[i] == "'":
            if string[i+1] == "s":
                result = result + ""
        elif string[i] == "s":
            if string[i-1] == "'":
                result = result + ""
            else:
                result = result + string[i]
        else:
            result = result + string[i]
    return result
           
f = open("moby-small.txt", encoding='utf-8')
s = f.read()
#print(s)

#tests
words_uncleaned = build_word_count(s)
#print(words_uncleaned)

words_cleaned = clean_apos(s)
#print(words_cleaned)

words_cleanagain = clean_data(words_cleaned)
#print(words_cleanagain)

words_count = build_word_count(words_cleanagain)
#print("COMMON WORDS COUNT:",words_count)

"""
sorted() works on any iterable, not just lists.
Strings, tuples, dictionaries (you'll get the keys),
generators, etc., returning a list containing all elements,
sorted. Use list.sort() when you want to mutate the list,
sorted() when you want a new sorted object back
"""
vals = words_count.values()
vals = sorted(vals)
#print(vals)

common_words = []
key_words = []
for key in words_count:
    if words_count[key] > 1:
        common_words.append([key,words_count[key]]) #is this appending a list within a list?
        key_words.append(key)
print("COMMON WORDS COUNT:",common_words)
#print(key_words)

#hw_08
word_after = {}
cleaned = words_cleanagain.split()
key_words = key_words
#print(cleaned)
print("\nCOMMON WORDS:",key_words)
for i in range(1,len(cleaned)-1):
    if cleaned[i] in key_words:
        element = cleaned[i]
        word_after.setdefault(element,[])
        word_after[element].append(cleaned[i+1])
print("\nWORD(S) AFTER COMMON WORDS:",word_after)



        
