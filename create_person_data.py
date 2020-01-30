import random

class Person:
    def __init__(self, first:str, last:str, age:float, worth:int, eye_colour:str):
        self.first = first.capitalize()
        self.last = last.capitalize()
        self.age = age
        self.worth = worth
        self.eye_colour = eye_colour
    
    def __repr__(self):
        return f"{self.first},{self.last},{self.age},{self.worth},{self.eye_colour}"
    

def person_generator():
    eye_colours = ["amber", "blue", "brown", "gray", "green", "hazel"]
    min_age = 18.0
    max_age = 90.0
    min_worth = 10000
    max_worth = 1000000000

    with open("data_names_first_all.txt", "r", encoding="utf-8") as file:
        first_names = file.read().splitlines()
    with open("data_names_last_all.txt", "r", encoding="utf-8") as file:
        last_names = file.read().splitlines()

    while True:
        yield Person(
            random.choice(first_names),
            random.choice(last_names),
            round(random.random() * (max_age - min_age) + min_age, 1),
            min(int(random.paretovariate(0.6) * min_worth), max_worth),
            random.choice(eye_colours))



def main(filename=None, amount=1000):
    if not filename:
        filename = f"data_person_{amount}.csv"

    people = person_generator()
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("first,last,age,net_worth,eye_colour\n")

        for _ in range(amount):
            file.write(f"{next(people)}\n")


if __name__ == "__main__":
    main(amount=100000)
