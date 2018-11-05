def happyLadybugs(b):
    if happiness(b):
        return "YES"
    else:
        return "NO"
    
def happiness(b):
    happy = False
    if underscore(b):
        happy = True
    elif repeat(b):
        if adjacent(b):
            happy = True
        else:
            if space(b):
                happy = True
    return happy
    
def underscore(b):
    result = True
    if len(b) == 0:
        result = False
    for element in b:
        if element != "_":
            result = False 
    return result

def adjacent(b):
    result = False
    for i in range(len(b)):          
        if b[i] == b[i-1] or b[i] == b[i+1]:
            result = True
        else:
            result = False
            break
    return result

def repeat(b):   
    result = False
    for element in b:
        count = 0
        if element != "_":
            for item in b:
                if element == item:
                    count = count + 1
            if count >= 2:
                result = True
            else:
                result = False
            break
    return result

def space(b):
    count = 0
    result = False
    for element in b:
        if element == "_":
            count = count + 1
    if count >= 1:
        result = True
    return result
        
print("' '", happyLadybugs(""))
print("_", happyLadybugs("_"))
print("RBY_YBR", happyLadybugs("RBY_YBR"))
print("X_Y__X", happyLadybugs("X_Y__X"))
print("2", happyLadybugs("2"))
print("B_RRBR", happyLadybugs("B_RRBR"))
print("BB__", happyLadybugs("BB__"))
print("ABAB", happyLadybugs("ABAB"))