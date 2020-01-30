
def main(needle):
    with open("data_nums_1000000.txt", "r") as file:
        numbers = list(map(int, file.read().splitlines()))

        # for i in range(len(numbers)):
        #     numbers[i] = int(numbers[i])

        for index, n in enumerate(numbers):
            if n == needle:
                return index


print(main(12345678))
