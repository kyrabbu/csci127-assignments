"""
dictionary => hash tables, hash maps, maps, key value pairs
key value pairs => set of two linked data terms
"""

d = {} #empty dictionary
       #must create first

d['key1'] = 'hello'
d['name'] = "Horatio Hornblower"

#list => check index, dict => check key
#you can use integers as keys

#you cannot use a list/other dictionaries as keys
#d[[1,2,3]] = 0

#values can be anything
#d['x'] = [5,2,3,1,6]

#you can put dictionary and look it up

person1 = {'name':'tom', 'age:'22} #must be strings 'age'
person2 = {'name':'sally', 'age:'22}
#go-to data structure

#change things in dictionary

#d.keys()
#d.values()
#makes lists, can do whatever, but will not change dict
#not guaranteed order we created them in
#can run sorted() for same kind

#sort() - mutate list
#sorted() = new sorted object back; creates copy