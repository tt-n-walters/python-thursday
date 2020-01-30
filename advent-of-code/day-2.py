def opcode1(input1_position, input2_position, output_position):
    global instructions
    input1 = instructions[input1_position]
    input2 = instructions[input2_position]
    print("Running opcode1 with numbers {}, {}".format(input1, input2))
    result = input1 + input2

    instructions[output_position] = result

def opcode2(input1_position, input2_position, output_position):
    global instructions
    input1 = instructions[input1_position]
    input2 = instructions[input2_position]
    print("Running opcode1 with numbers {}, {}".format(input1, input2))
    result = input1 * input2

    instructions[output_position] = result


with open("day-2-input.txt", "r") as file:
    contents = file.read().split(",")

instructions = [int(num_as_string) for num_as_string in contents]
instructions[1] = 12
instructions[2] = 2
for i in range(0, len(instructions), 4):
    opcode = instructions[i]
    print("Found opcode {}".format(opcode))
    if opcode == 1:
        opcode1(i + 1, i + 2, i + 3)
    elif opcode == 2:
        opcode2(i + 1, i + 2, i + 3)
    elif opcode == 99:
        print("Reached opcode 99. Exiting program.")
        print(instructions)
        exit()
