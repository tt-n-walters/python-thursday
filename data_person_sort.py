from collections import namedtuple
from random import choice


processes = [
    str, str, float, int, str
]

# def data_formatter(data_string):
#     processes = [
#         lambda x: x,
#         lambda x: x,
#         lambda x: float(x),
#         lambda x: int(x),
#         lambda x: x
#     ]
#     for i, value in enumerate(data_string.split(",")):
#         yield processes[i](value)

def data_processor(processes, data):
    for process, item in zip(processes, data):
        yield process(item) 


with open("data_person_1000.csv", "r") as file:
    people_data = file.read().splitlines()
    Person = namedtuple("Person", people_data[0])

    person_1 = Person(*choice(people_data).split(","))
    print(person_1)

    person_2 = Person(*data_processor(processes, choice(people_data).split(",")))
    print(person_2)

    person_3 = Person(*(fn(data) for fn, data in zip(processes, choice(people_data).split(","))))
    print(person_3)

