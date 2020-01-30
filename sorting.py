import random
print(__name__)
# data = []
# for i in range(100):
#     data.append(random.randint(0, 100))

# Generator Expression
data = [random.randint(0, 100) for _ in range(25)]


def bubble(data, start_first, start_second):
    num_of_loops = 0
    num_of_swaps = 0
    # Loop through all the data n times, where n is the length of the data.
    for j in range(start_first, len(data) - 1):
        swaps_before = num_of_swaps
        # Loop through the data in pairs, where the loop can get shorter each time.
        for i in range(start_second, len(data) - j - 1):
            num_of_loops += 1
            # The the next two values out of the list
            first = data[i]
            second = data[i + 1]

            # If the the first number is greater than the second,
            # swap their positions in the list.
            if first > second:
                num_of_swaps += 1
                # data[i] = second
                # data[i + 1] = first
                data[i], data[i + 1] = second, first
                return j, i

        if swaps_before == num_of_swaps:
            return j, 0

    print("Number of loops {}".format(num_of_loops))
    print("Number of swaps {}".format(num_of_swaps))


if __name__ == "__main__":

    data = [i for i in range(1000)]
    for _ in range(1000):
        bubble(data, 0, 0)

    # data = [random.randint(0, 100) if i < 500 else i for i in range(1000)]
    # bubble()
