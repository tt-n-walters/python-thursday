from people_data import main as load_people_data
from binary_search import binary_search 


def main():
    people_data = load_people_data()

    age_key = lambda person: person.age

    age_sorted = sorted(people_data, key=age_key)
    age_result = binary_search(age_sorted, 66.6, key=age_key)
    
    print(f"Found index: {age_result}")
    print(f"Person found: {age_sorted[age_result]}")

    def complex_key(person):
        if person.first.startswith("N") and person.eye_colour == "green":
            if person.net_worth < 100000 or person.age < 42:
                return -1
            elif person.net_worth > 200000 or person.age >= 43:
                return 1
            else:
                return 0
        else:
            return -1
    
    complex_sorted = sorted(people_data, key=complex_key)
    complex_result = binary_search(complex_sorted, 0, key=complex_key)
    
    print(f"Found index: {complex_result}")
    print(f"Person found: {complex_sorted[complex_result]}")



if __name__ == "__main__":
    main()
