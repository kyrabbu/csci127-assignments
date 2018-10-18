import random

"""
The story unfolds in <SETTING>.
The text revolves around <CHARACTER>. <PRONOUN> is <CHARACTER TRAIT> and
<ANOTHER CHARACTER TRAIT>. <MAIN CHARACTER PRONOUN> wanted to <WHAT DO CHAR WANT>.
The problem is <PROBLEM>. <MAIN CHARACTER> ovecome this by <VERB>. Readers learn
<MESSAGE/THEME/MORAL>.
"""

#choices
noun_place = ["New York", "California", "Florida", "Ohio", "Massachusetts"]
noun_char = ["James", "Mary", "John", "Partricia", "Robert"]
pronoun = ["He", "She"]
adj_bad =  ["antisocial", "cocky", "devious", "evil", "greedy"]
adj_good = ["loyal", "honest", "respectful", "responsible", "humble"]
verb = ["cry", "eat", "sleep", "dance", "walk"]
problem = ["diarrhea", "glutony", "procrastination"]
gerund = ["stabbing", "sweating", "exploding"]
theme = ["sadness","death","love"] 

#story
first = "The story unfolds in"
second = "The text revolves around"
third = "is and"
fourth = "wanted to"
fifth = "The problem is"
sixth = "overcomes this by"
seventh = "Readers learn"

def madlibs_one(x):
    print("Sentence:", x)
    sentence = x.split()
    select = random.choice(noun_place)
    sentence.append(select)
    sentence = str(" ".join(sentence)) + '.'
    return sentence
    
def madlibs_two(x):
    print("Sentence:", x)
    global noun_char
    sentence = x.split()
    select_name = random.choice(noun_char)
    
    noun_char = select_name
    
    sentence.append(select_name)
    sentence = str(" ".join(sentence)) + '.' #what is this " "
    return sentence

def madlibs_three(x):
    print("Sentence:", x)
    global pronoun
    sentence = x.split()
    select_pronoun = random.choice(pronoun)
    select_bad = random.choice(adj_bad)
    select_good = random.choice(adj_good)
    sentence.insert(0, select_pronoun)
    sentence.insert(3, select_bad)
    sentence.insert(5, select_good)
    sentence = str(" ".join(sentence)) + '.'
    pronoun = select_pronoun
    return sentence

def madlibs_four(x):
    print("Sentence:", x)
    sentence = x.split()
    select_verb = random.choice(verb)
    sentence.insert(0, pronoun)
    sentence.append(select_verb)
    sentence = str(" ".join(sentence)) + '.'
    return sentence

def madlibs_five(x):
    print("Sentence:", x)
    sentence = x.split()
    select_problem = random.choice(problem)
    sentence.append(select_problem)
    sentence = str(" ".join(sentence)) + '.'
    return sentence
    
def madlibs_six(x):
    print("Sentence:", x)
    sentence = x.split()
    select_gerund = random.choice(gerund)
    sentence.append(select_gerund)
    sentence.insert(0, pronoun)
    sentence = str(" ".join(sentence)) + '.'
    return sentence

def madlibs_seven(x):
    print("Sentence:", x)
    sentence = x.split()
    select_theme = random.choice(theme)
    sentence.append(select_theme)
    sentence = str(" ".join(sentence)) + '.'
    return sentence


#tests
print(madlibs_one(first))
print(madlibs_two(second))
print(madlibs_three(third))
print(madlibs_four(fourth))
print(madlibs_five(fifth))
print(madlibs_six(sixth))
print(madlibs_seven(seventh))