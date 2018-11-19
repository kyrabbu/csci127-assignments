
def build_word_counts(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_data(s):
    result=""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            result = result + letter.lower()
        else:
            result = result + " "
    return result

def build_word_lists_by_index(words):
    d={}
    words = words.split()
    for i in range(0,len(words)-2):
        d.setdefault(words[i],[])
        d[words[i]].append(words[i+1])
    return d

def build_word_lists(words):
    d={}
    words = words.split()
    prev = words[0]
    for nextword in words[1:]:
        d.setdefault(prev,[])
        d[prev].append(nextword)
        prev = nextword
    return d

filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/moby-small.txt"

f = open(filename)
s = f.read()
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
#print("-------------------")
cleaned_string = clean_data(s)
#words = build_word_counts(cleaned_string)
#vals = words.values()
#vals = sorted(vals)
#print('------')
#common_words = []



filename="/home/zamansky/gh/fall-2018-127/classcode/dictionaries/moby-small.txt"

f = open(filename)
s = f.read()
s = clean_data(s)
wl = build_word_lists(s)
#words_uncleaned = build_word_counts(s)
#print(words_uncleaned)
#print("-------------------")
cleaned_string = clean_data(s)
words = build_word_counts(cleaned_string)
vals = words.values()
vals = sorted(vals)
#print('------')
#common_words = []
#for k in words:
#    if words[k] > 1000:
#        common_words.append([k,words[k]])

#common_words = [ [k,words[k]] for k in words if words[
#for k in words:
#    if words[k] > 1000:
#        common_words.append([k,words[k]])

#common_words = [ [k,words[k]] for k in words if words[k] > 50 ]def build_word_count(words):
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

import random
def gen_text(wl,number):
    next = wl[0]
    text = []
    for i in range(number):
        text.append(next)
        next = random.choice(wl[next])
    return ' '.join(text)


        
