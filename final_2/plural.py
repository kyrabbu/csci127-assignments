def countPlurals(line):
    count = 0
    for word in line.split():
        if word[-1] == "s":
            count = count + 1
    return count

def notPossessive(line):
    count = 0
    for word in line.split():
        if word[-1] == "s" and word[-2] != "'":
            count = count + 1
    return count

#tests
print("Plurals:", countPlurals("apples oranges grape banana"))
print("No Possessives:", notPossessive("apple's oranges grape's banana"))
print("No Possessives:", notPossessive("apples oranges grapes banana"))
