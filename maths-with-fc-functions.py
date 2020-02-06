
# def add_5(number):
#     return number + 5


def create_adder(value):
    def adder(number):
        return value + number
    
    return adder



process_func = create_adder(9999)


print(process_func(110))
