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
print("Plurals:", countPlurals("apples apples grapes banana"))
print("Plurals with 's:", countPlurals("apple's orange's grape's banana's"))
print("Plurals with 's:", countPlurals("apple'ss orange's grape's banana's"))
print("No Possessives:", notPossessive("apple's oranges grape's banana"))
print("No Possessives:", notPossessive("apples oranges grapes banana"))
