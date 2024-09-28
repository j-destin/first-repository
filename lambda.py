import time

people = [
    {"name": "Abu", "country": "Liberia"},
    {"name": "Destine", "country": "Gabon"},
    {"name": "Annette", "country": "Ghana"},
    {"name": "Jerome", "country": "USA"}
]

def f(person):
    return person["name"]

people.sort(key=f)

for persons in people:
    time.sleep(1)
    print(persons, sep="----------")