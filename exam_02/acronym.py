def makeacronym(string):
    acronym = []
    for word in string.split():
        #print(word)
        acronym.append(word[0].lower())
    return "".join(acronym)
        
#tests
input1 = "Laugh Out Loud"
input2 = "Read the... fine manual"
input3 = "In my humble opinion"
input4 = "In my not so humble opinon"
input5 = "Be right back!"
input6 = "Talk To you Later."

print("\nInput:", input1, "\nAcronym:", makeacronym(input1))
print("\nInput:", input2, "\nAcronym:", makeacronym(input2))
print("\nInput:", input3, "\nAcronym:", makeacronym(input3))
print("\nInput:", input4, "\nAcronym:", makeacronym(input4))
print("\nInput:", input5, "\nAcronym:", makeacronym(input5))
print("\nInput:", input6, "\nAcronym:", makeacronym(input6))
