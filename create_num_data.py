import random

def gen_nums(min=1, max=100000000):
    while True:
        yield random.randint(min, max)

def main(filename=None, amount=10000000):
    if not filename:
        filename = f"data_nums_{amount}.txt"
    nums = gen_nums()

    with open(filename, "w") as file:
        # file.write("[")
        
        for _ in range(amount):
            file.write(f"{next(nums)}\n")
        
        # file.write(f"{next(nums)}]")

if __name__ == "__main__":
    main(amount=10000)
