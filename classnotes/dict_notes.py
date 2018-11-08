student = {'name': 'John', 'age': 25, 'courses': ['Math. CompSci']}

student['phone'] = '123-4567' #adds to dict
student['name'] = 'Sarah' #updates key-value

#print(student.get('school','Not Found'))
#looks for value
#if not found, says not found

#student.update({'name':'Jane','age':29,'phone':'555-5555'})
#multiple updates at once

#del student['age'] #deletes key

age = student.pop('age')
#deletes from list but can still return value


print(student)
print('\n')
print(age)
print('\n')
print(len(student)) #three key-values
print('\n')
print(student.keys())
print('\n')
print(student.values())
print('\n')
print(student.items())

for key in student:
    print(key) #only printed keys

print('\n')
for key in student.items():
    print(key) 

print('\n')
for key, value in student.items():
    print(key, value) 
    