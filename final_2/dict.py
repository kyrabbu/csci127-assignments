def addline(d, line):
    l = line.lower()
    for element in l.split():
        d.setdefault(element[0], [])
        d[element[0]] += [element]
    return d

def spellcheck(d, word):
    w = word.lower()
    for l in d.values():
        if w in l:
            return True
    return False

d = {} #empty at first
print(addline(d,"HELLO MY NAME IS KYRA"))
print(addline(d,"I LIKE APPLES"))
print(addline(d,"HeLlO mY nAmE is KyRa"))
print(addline(d,"WHAT is WRONG with THIS line"))
print(addline(d,"testing testing testing testing"))

k = addline(d,"HELLO MY NAME IS KYRA")
print(spellcheck(k,"DO YOU LIKE APPLES"))
print(spellcheck(k,"hi"))
print(spellcheck(k,"i"))
print(spellcheck(k,"kyra"))
print(spellcheck(k,"testing"))
