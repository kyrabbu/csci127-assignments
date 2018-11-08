"""
Finish the Happy Ladybug program using a dictionary to determine if
there are enough of each type of ladybug to make them happy.
"""
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"

def happyLadybugs(b):
    if TwoOrMore(b):
        if ScanAdjacent(b):
            return "YES"
        elif FindUnderscore(b):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
        
def FindUnderscore(b):
    if len(b) == 0: 
        return False #empty string
    for a in b:
        if a != "_":
            return False #scans until "_" found
        return True

def ScanAdjacent(b):
    result = False
    for a in range(len(b)):
        if len(b) == 1:
            return False
        elif b[-1] == b[-2]:
            result = True
        elif b[-1] != b[-2]:
            return False
        elif a == (len(b)-1):
            if b[a] == b[-1]:
                result = True
            else:
                return False
        elif a == 0:
            if b[a] == b[a+1]:
                result = True
            else:
                return False
        elif b[a] == b[a+1] or b[a] == b[a-1]:
            result = True
        else:
            return False
    return result
        

#using dictionaries
def ColorCount(b):
    colors = {}
    for a in b:
        colors[a] = 0
    for a in b:
        colors[a] = colors[a]+1
    return colors

def TwoOrMore(b):
    colors = ColorCount(b)
    result = False
    for value in colors.values():
        if value > 1:
            result = True
        else:
            result = False
    #print(colors)
    return result
    
        
print("Empty String =>", happyLadybugs(""))        
print("_ =>" ,happyLadybugs("_"))
print("ABABABABA =>",happyLadybugs("ABABABABA"))
print("AAABBBCCC =>",happyLadybugs("AAABBBCCC"))
print("A_BCD =>",happyLadybugs("A_BCD"))
print("_AACBCB =>",happyLadybugs("_AACBCB"))
print("___ =>",happyLadybugs("___"))
#print("AB__ =>", happyLadybugs("AB__"))
print("AA__ =>", happyLadybugs("AA__"))
print("ABAB_ =>", happyLadybugs("ABAB_"))
print("ABAB =>", happyLadybugs("ABAB"))
print("AABB =>", happyLadybugs("AABB"))

    