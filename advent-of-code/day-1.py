from math import floor
from pprint import pprint

def calculate_fuel(mass):
    return floor(mass / 3) - 2


with open("day-1-input.txt", "r") as file:
    contents = file.read().splitlines()


numbers = [int(s) for s in contents]

answers = []
for mass in numbers:
    fuels = []
    last = calculate_fuel(mass)

    while last > 0:
        fuels.append(last)
        last = calculate_fuel(last)

    answers.append(fuels)

pprint(answers)

summed_answers = []
for answer in answers:
    summed_answers.append(sum(answer))



summed_answers = [sum(answer) for answer in answers]

print(sum(summed_answers))
