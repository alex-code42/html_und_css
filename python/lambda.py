#List of People
#Instead of a string, the string is a dictionary
#a Dictionary in a List    List(Dictionary)


people = [
    {"name": "Harry" , "house": "Gryffindor"},
    {"name" : "Cho" , "house": "Ravenclaw"},
    {"name" : "Draco", "house": "Slytherin"},
]






people.sort(key=lambda person: person["name"])

print(people)