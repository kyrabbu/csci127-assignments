#Kyra Alyssa Abbu
#CSCI 127
#HW01
#091718

def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    return name.title() #capitalized each first letter

print(capitalize('kyra abbu'))
print(capitalize('john doe'))
print(capitalize('mary kate'))

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    initial = name[0].upper() #takes first letter of first word
    name.split(' ')
    a,b = name.split(' ') #splits two words into a and b
    full_name = initial + '. ' + b.title() 
    return full_name

print(init('kyra abbu'))
print(init('john doe'))
print(init('mary kate'))

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    new_word = name[1:] + name[0] + 'ay'
    #takes second charater to the end
    #adds the first letter of string to end
    return new_word

print(part_pig_latin('hello'))
print(part_pig_latin('nothing'))
print(part_pig_latin('pink'))

def make_out_word(out, word):
  wrd = out[0:2] + word + out[2:] #the second number in the [0:2] prints position before it
  return wrd

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('HHoo', 'Hello'))

def make_tags(tag, word):
  x = '<' + tag + '>' + word + '</' + tag + '>'
  return x

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))


