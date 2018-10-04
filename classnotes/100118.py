#[] used for indexing too
empty_list = [] #empty list
l =[0,10,20,30,40,50,60,7080,90,100,110,120,130,140,150]
l2=[10,"Hello",True,3.5,20] #can mix and match but usually just put one kind
s="Hello World!"
#check s[3]

""" 
similarities of strings and lists:
s+s
l2+l2
a string is a list with somelimitations
- you can index, slice, and add lists like arrays
"""


print(len(l))
print(l2)
l2[2]="New String" #you can reassign a list value
#s[2] = 'a' <-- you can't do this to a string
#a string is immutable, you can;t change stuff on a string but you can on lists

print(12)
l3.append(1)
l3.append("word")
l3.append(l2)
print("l3: ", l3)

l4 = l3 + l2
print("Changing l2910 to a Z")
l2[1] = 'Z'

l2.remove(3.5) #removes the first ocurance of 3.5
12.delete(1)
12.pop()
