import random

sen ="The <NOUN> <VERB> the <NOUN> with an enthusiasm unknown to mankind."

nouns =["dog","boy","girl","hammer","frog","boat"]
verbs =['ate','slept','walked','bludgeoned']

dict = {"NOUN": nouns, "VERB": verbs}

def madlibify(s,d):
    result = []
    for word in s.split(): #splits string into a list
        if word == "<NOUN>":
            result.append(random.choice(d["NOUN"]))
        elif word == "<VERB>":
            result.append(random.choice(d["VERB"]))
        else:
            result.append(word)
    return " ".join(result)

print(madlibify(sen,dict))