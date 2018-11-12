"""
If there is no underscore, check if adjacent;
If there is an underscore, count if there is more than two of each;

"""

def happyLadybugs(b):
    if happy(b):
        return "YES"
    else:
        return "NO"

def happy(b):
    if '_' not in b:
        return scanAdjacent(b)
    else: #if there is an underscore
        b = b.replace("_","")
        return TwoOrMore(b)       
        
def scanAdjacent(b):
    for i in range(1,len(b)): #does not include first and last
            if b[i] != b[i-1] and b[i] != b[i-1]:
                return False
            else:
                return True

def ColorCount(b):
    colors = {}
    for a in b:
        colors[a] = 0
    for a in b:
        colors[a] = colors[a]+1
    return colors

def TwoOrMore(b):
    colors = ColorCount(b)
    for value in colors.values():
        if value < 2:
            return False
        return True
    
print("Empty String (NO BUGS) =>", happyLadybugs(""))        
print("_ (NO BUGS) => " ,happyLadybugs("_"))
print("ABABABABA =>",happyLadybugs("ABABABABA"))
print("AAABBBCCC =>",happyLadybugs("AAABBBCCC"))
print("A_BCD =>",happyLadybugs("A_BCD"))
print("_AACBCB =>",happyLadybugs("_AACBCB"))
print("___ (NO BUGS) =>",happyLadybugs("___"))
print("AB__ =>", happyLadybugs("AB__"))
print("AA__ =>", happyLadybugs("AA__"))
print("ABAB_ =>", happyLadybugs("ABAB_"))
print("ABAB =>", happyLadybugs("ABAB"))
print("AABB =>", happyLadybugs("AABB"))
