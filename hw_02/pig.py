#Kyra Abbu
#Partner: Will Lu

"""Input: A string that is either lowercase or uppercase
Return: if first letter of the word is a vowel --> full word with "ay" added
if first letter of the word is a consonant --> first letter moved to end and add "ay"
example: kyra --> yrakay
        amber --> amberay
"""

vowels = 'aeiou' #stores all vowels
def pig_latin(word): 
    if word[0].lower() in vowels: #first letter searches vowels
        word = word.lower() #turns whole word lowercase
        pig = word + 'ay' 
    else:
        word = word.lower() 
        pig = word[1:] + word[0] + 'ay' #moves first letter to last
    return pig #returns values for either conditions
    
print(pig_latin('amber'))
print(pig_latin('kyra'))
print(pig_latin('will'))
print(pig_latin('Kyra'))
print(pig_latin('Will'))
print(pig_latin('Amber'))

    
    