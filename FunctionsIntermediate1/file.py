#Update dictionaries and Lists
# Call key and get back value!
#Different data structures with {} and[]
x = [ [5,2,3], [10,8,9] ] 
students = [
    {"id": 1, 'first_name':  'Michael', 'last_name' : 'Jordan'},
    {"id": 2,'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
#Dictionary 1 [10,8,9] of index place holder 0 is 9

students[0]["last_name"] = "Bryant"
print(students)
#Students of 0 is all of line 1, so set students[0]of key[lastname] set equal to new value Bryant, Where: calling key (first & last name) of dictionary (line 1 or 2), value is (michael & jordan) 

sports_directory["soccer"][0] = "Andres"
#{} call by key name (soccer) and then index number (0) of the values changing to new value Andres

z[0]["y"] = 30
print(z)
#Call key of o which is {['x': 10, 'y': 20]} and then key named y setting value to be 30

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name': 'John', 'last_name' : 'Rosales'},
        {'first_name': 'Mark', 'last_name' : 'Guillen'},
        {'first_name': 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(arr):
    for student in arr:
        print(f'first_name: {student["first_name"]} last_name: {student["last_name"]}')
iterateDictionary2(students)
#student is each row and each row is a dictionary, students is the list, [] first key of the first row,

def iterateDictionary1(key_name,arr):
    for row in arr:
        print(f'{row[key_name]}')
iterateDictionary1("first_name",students)
iterateDictionary1("last_name",students)
#looks for key name and then the arr (list), key name is first & last name, specify each for each row and split into 2

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key,value in dictionary.items():
        print(f'{len(value)} {key}')
        for i in range(0,len(value)):
            print(value[i])
printInfo(dojo)
#keys = locations & instructors, dojo = dictionary, lists are inside [], 1 value for each [],













