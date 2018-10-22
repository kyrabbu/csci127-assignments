import random

#choices
noun_place = ["New York", "California", "Florida", "Ohio", "Massachusetts"]
noun_char = ["James", "Mary", "John", "Patricia", "Robert"]
pronoun = ["He", "She"]
adj_bad =  ["antisocial", "cocky", "devious", "evil", "greedy"]
adj_good = ["loyal", "honest", "respectful", "responsible", "humble"]
verb = ["cry", "eat", "sleep", "dance", "walk"]
problem = ["diarrhea", "glutony", "procrastination"]
gerund = ["stabbing", "sweating", "exploding"]
theme = ["sadness","death","love"]

story = """The story unfolds in <SETTING> . The text revolves around <CHARACTER> .
<PRONOUN> is <BADTRAIT> but <GOODTRAIT> . <CHARACTER2> wanted to <VERB> .
The problem is <PROBLEM> . <CHARACTER3> ovecome this by <GERUND> . Readers learn <MESSAGE> ."""

result_char = " " #explanation in madlibs function

#when trying to understand, skip this function first and refer to it later, go to madlibs(sentence)
def pronoun_find(value):
        #print(value)
        #statement below does not work the same as valid statements (?)
        #if value == "John" or "James" or "Robert":  
                #select = pronoun[0]
        if value == "John" or value == "James" or value == "Robert": #checks if the value which is result_char from other code is equal to these
                select = pronoun[0] #makes select "he"; check list
        else:
                select = pronoun[1]
        return select #returns whichever one satisfies conditions
    
def remove_dot(l):
    new_list = [] 
    for item in l:
        if item != ".": 
            new_list.append(item) #if item is not a period, it will add it to nnew list we made
        else:
            new_list[-1] = str(new_list[-1]) + '.' #this will change the last item added in list with period
    return new_list #transfers this value to the madlibs function
    
def madlibs(sentence):
    sentence = sentence.split() #makes input (sentence), which is a string, into a list
    for element in sentence: #this scans every element in list we created
        if element == "<SETTING>": #checks every element beginning from index 0 until it finds <"SETTING"> then performs code below
            select = random.choice(noun_place) #this uses the import random and ".choice" means
                                                #select random value from (noun_place) which is our list
            replacement = sentence.index(element)
            """
            sentence.index(element) means that in the list "sentence",
            which we created in the beginning, it will find the index
            or the position of "element", element being something inside
            the list, then we are assigning its position number
            to the variable "replacement" replacement then becomes a variable
            with a number associated with, example: replacement = 3 (if index of element is 3)
            """
            
            sentence[replacement] = select
            
            """we are saying that in the list named "sentence" in the
            [position number] the index being assigned previously, it will REPLACE
            that element in the list into "select" which is the random value we
            looked for in the beginning of code"""
            
            continue
        
            """this will return the program back to the start, moving onto the following
            value in the list, which is the value after "<SETTING">"""
            
        elif element == "<CHARACTER>":
            select_name = random.choice(noun_char)
            replacement = sentence.index(element)
            sentence[replacement] = select_name
            result_char = select_name
            """
            just like what we do in while loops for increment "i = 0" where
            in the end we add "i = i + 1" we are doing the same here
            since we are assigning a string, not a number, we are
            replacing " " to the string select_name
            """
            continue
        elif element == "<PRONOUN>":
            answer = pronoun_find(result_char)
            """call another function which is on top, then the result from that
            function, we assign to answer to be able to use it in this funtion
            """
            replacement = sentence.index(element)
            sentence[replacement] = answer
            continue
        elif element == "<BADTRAIT>":
            select = random.choice(adj_bad)
            replacement = sentence.index(element)
            sentence[replacement] = select
            #print(sentence)
            continue
        elif element == "<GOODTRAIT>":
            select = random.choice(adj_good)
            replacement = sentence.index(element)
            sentence[replacement] = select
            #print(sentence)
            continue
        elif element == "<CHARACTER2>":
            replacement = sentence.index(element)
            sentence[replacement] = result_char
            continue
        elif element == "<VERB>":
            select = random.choice(verb)
            replacement = sentence.index(element)
            sentence[replacement] = select
            continue
        elif element == "<PROBLEM>":
            select = random.choice(problem)
            replacement = sentence.index(element)
            sentence[replacement] = select
            continue
        elif element == "<CHARACTER3>":
            replacement = sentence.index(element)
            sentence[replacement] = result_char
            continue
        elif element == "<GERUND>":
            select = random.choice(gerund)
            replacement = sentence.index(element)
            sentence[replacement] = select
            continue
        elif element == "<MESSAGE>":
            select = random.choice(theme)
            replacement = sentence.index(element)
            sentence[replacement] = select
            """
            we do not want this in the beginning of our code or prior if/elif
            statements because it will turn our program
            into a string and we cannot use it unless we add another
            line of code but this will join it all together and make a string
            """
            new_sentence = remove_dot(sentence)
            new_sentence = str(" ".join(new_sentence))
            print(new_sentence)
            return
        


#test
madlibs(story)
          
          
            
            
            
