# this is a new file - this is a comment

#print('hello')

a = 10
b = 2 * a
print(a,b)
a = 30
print(a,b)

 #def means define #add_one(x) is the identifier #(x) is a parameter # def identifier(params)
def add_one(x):
    """
    this is a docstring that
    can describe the function""" #good practice to do this
    #a = x
    #print('I received', a)
    #a = a + 1
    #print('Now x is', a)
    x = x + 1
    return x #sending back the value of a

print("this line isnt indented lol")
a = 20 #variables created in a function are only usable in the function. they are created each time you call or use the function and are destroyed when the function returns
# scope
# they are called "local variables"
# argumens/parameters are like local variables but they get values from the function caller each time the function is called/used

a = add_one(a)
print(x)
#in math, a function akes in an input and releases an output
#not enirely true for computers but works most of the time
#in python, if you do not do anything it returns "none"