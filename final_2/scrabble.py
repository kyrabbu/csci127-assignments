def canMakeWord(letters,word):
    tester = makeList(letters)
    real = makeList(word)
    for element in real:
        if element in tester:
            tester.remove(element) #to avoid repetition
        else:
            return False #stops program if satisfied
    return True

def makeList(word):
    l = []
    for i in word:
        l.append(i)
    return l

def wildCard(letters,word):
    tester = makeList(letters)
    real = makeList(word)
    for element in real:
        if element in tester:
            tester.remove(element)
        else:
            if "?" in tester:
                tester.remove("?")
                continue
            else:
                return False
    return True

#given tests
print(canMakeWord("ladilmy","daily"))
print(canMakeWord("eerriin","eerie"))
print(canMakeWord("orrpgma","program"))
print(canMakeWord("orppgma","program"))
#more tests
print(canMakeWord("xxxxxxxxxkyra","kyra"))
print(canMakeWord("zzzzzzzzkzzzzkkzzzk","kyra"))
print("\nWild Card:")
print(wildCard("ladi?my","daily"))
print(wildCard("eerr??iin","eerie"))
print(wildCard("orrpg?ma","program"))
print(wildCard("orp???pgma","program"))
print(wildCard("orpgma","program"))
