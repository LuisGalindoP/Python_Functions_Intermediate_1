#-------------------------------------------------------
# 1 Update values in Dictionaries and Lists

# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]


# def UpdateValues(x, students, sports_directory):
#     x[1][0] = 15
#     students[0]["last_name"] = "Bryant"
#     sports_directory["soccer"][0] = "Andres"
#     z[0]["y"] = 30
    
# UpdateValues(x, students, sports_directory)
# print(len(x))
# print(len(students))
# print(len(sports_directory))
# print(len(z))


#-------------------------------------------------------
# 2 Iterate through a list of dictionaries

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary(students):
#     for i in range(len(students)):
#         print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")
    
# iterateDictionary(students)



#-------------------------------------------------------
# 3 Get values from a list of dictionaries

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterateDictionary2(key_name, list):
#     for i in range(len(list)):
#         print(list[i][key_name])

# iterateDictionary2("first_name", students)
# iterateDictionary2("last_name", students)



#-------------------------------------------------------
# 4 Iterate through a dictionary with list values

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo):
    print(f"{len(dojo['locations'])} LOCATIONS")
    for i in range(len(dojo["locations"])):
        print(dojo["locations"][i])
    print(" ")
    print(f"{len(dojo['instructors'])} INSTRUCTORS")
    for i in range(len(dojo["instructors"])):
        print(dojo["instructors"][i])




printInfo(dojo)
