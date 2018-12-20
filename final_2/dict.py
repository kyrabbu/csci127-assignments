def addline(d, line):
    line = line.lower()
    for element in line.split():
        d.setdefault(element[0], [])
        d[element[0]] += [element]
    return d

def spellcheck(d, word):
    word = word.lower()
    for i in d.values():
        if word in i:
            return True
    return False

d = {} #empty at first
print(addline(d,"HELLO MY NAME IS KYRA"))
print(addline(d,"I LIKE APPLES"))
print(addline(d,"HeLlO mY nAmE is KyRa"))
print(addline(d,"WHAT is WRONG with THIS line"))
print(addline(d,"testing testing testing testing"))

new_d = addline(d,"HELLO MY NAME IS KYRA")
print(spellcheck(new_d,"DO YOU LIKE APPLES"))
print(spellcheck(new_d,"hi"))
print(spellcheck(new_d,"i"))
print(spellcheck(new_d,"kyra"))
print(spellcheck(new_d,"testing"))
