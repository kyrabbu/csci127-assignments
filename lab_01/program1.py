
def greeter(name):
    return "Hello " +name+ "!"

print(greeter("Stan"))

#String-1>hello_name
def hello_name(name):
  return "Hello "+name+"!"

print(hello_name("Sam"))

#String-1>make_abba
def make_abba(a, b):
  return a+b+b+a

print(make_abba("Hi","Bye"))
print(make_abba("Yo","Alice"))
print(make_abba("What","Up"))

#String-1>make_tags
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

print(make_tags("i","Yay"))