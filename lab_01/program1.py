
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

#Warmup-1>sleep_in
def sleep_in(weekday, vacation):
  if not weekday or vacation: #or means either one or both weekday or vacation 
    return True
  else:
    return False

print(sleep_in(False,True))
print(sleep_in(False,False))
print(sleep_in(True,True))
print(sleep_in(True,False))

#warmup-1>monkey trouble
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

print(monkey_trouble(True, False))
print(monkey_trouble(False, False))
print(monkey_trouble(True, True))
print(monkey_trouble(False, True))
