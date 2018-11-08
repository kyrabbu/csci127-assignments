def happyLadybugs(b):
    if "_" not in b:
        for a in range(len(b)-1):
            if b[a] != b[a-1] and b[a] != b[a+1]:
                return False
        return True
    else:
        b = b.replace("_"," ")
        counts = {}
        for bug in b:
#            if bug in counts.keys():
#                counts[bug] = counts[bug]+1
#            else:
#                counts[bug]=1
            counts.setdefault(bug,0)
            counts[bug]=counts[bug]+1
        if 1 in counts.values():
            return False
        else:
            return True
    

testcases = ["ABCDEA","ABCCDE","ABC_DEF","ABC_CDDEBA__", "ABC_ABCD_ABC"]

for test in testcases:
    print(test)
    print(happyLadybugs(test))

print(happyLadybugs(testcases))