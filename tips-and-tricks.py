
#__#        Tip & Trick  no 1   
# We want to iterate over more than one list at a time

x_coords = [45, 92, 20, 71, 53]
y_coords = [24, 21, 68, 47, 19]
z_coords = [67, 83, 42, 13, 99]

# x = 0
# while x < 5:
#     print(x_coords[x], y_coords[x])
#     x += 1

# for n in range(len(x_coords)):
#     print(x_coords[n], y_coords[n])

for x, y, z in zip(x_coords, y_coords, z_coords):
    print(x, y, z)




# output:
# 45 24
# 92 21
# 20 68
# 71 47
# 53 19







#_#


#__#        Tip & Trick  no 2   
# We want to loop through some data, and have access to the items and indexes at the same time

shopping_list = ["bread", "cereal", "rice", "pasta", "eggs", "orange juice"]


for i in range(len(shopping_list)):
    print("Item {}: {}".format(i, shopping_list[i]))


for i, item in enumerate(shopping_list):
    print("Item {}: {}".format(i, item))






# output:
# Item 0: bread
# Item 1: cereal
# Item 2: rice



#_#


#__#        Tip & Trick  no 3   
# We want to swap two variables

a = "hello there"
b = "general kenobi"

# tmp = a
# a = b
# b = tmp

a, b = b, a


print(a)
print(b)







# output:
a = "general kenobi"
b = "hello there"






#_#


#__#        Tip & Trick  no 4   
# We want to inspect a variable, object, module, class, etc...

import math

print(dir(math))


shapes = {"square": 4, "triangle": 3, "hexagon": 6}
print(dir(shapes))











#_#


#__#        Tip & Trick  no 5   
# We want to categorise a sentance of words

from pprint import pprint
from collections import defaultdict


sentence = "A cranky old lady shoots lemons with her high-powered machinegun while wearing crocks."

# words = sentence.split(" ")
# results = dict()

# for word in sorted(words):
#     first_letter = word[0]
#     if first_letter in results:
#         results[first_letter].append(word)
#     else:
#         results[first_letter] = [word]

words = sentence.split(" ")
results = defaultdict(list)

for word in sorted(words):
    first_letter = word[0]
    results[first_letter].append(word)

pprint(results)












"""
Split the sentence into words
Loop over the words:
    If the first letter of the word exists in the dictionary:
        Add the word to list in the dictionary
    Otherwise:
        Create a list inside the dictionary

"""






# output: dictionary of lists
# {
#     "a": ["A"],
#     "c": ["cranky", "crocks"],
#     "h": ["high-powered"],
#     "l": ["lady", "lemons"],
#     etc...
# }









# We want to count the occurences of each letter in a sentence.










#_#

#__#        Tip & Trick  no 6   
# We want to print a larger, more complicated data structure

import random
from pprint import pprint
pprint(dir(random), compact=True, width=30)













#_#

#__#        Tip & Trick  no 7   
# We want to initialise a list with a number of starting values

a = []
for _ in range(10):
    a.append(0)



a = [0 for _ in range(10)]


a = [0] * 10





print(a)


# output:
# a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]




#_#

#__#        Tip & Trick  no 8   
# We want to access items in a dictionary, but there is a chance the items don't exist in the dictionary

people = {
    "arthur": "ginger",
    "bill": "ginger",
    "charlie": "ginger",
    "dobby": "bald",
    "errol": "feathers",
    "fred": "ginger",
    "george": "ginger",
    "harry": "black"
}












#_#

#__#        Tip & Trick  no 9   
# Making comparisons more concise


# Check if a value is within a range
age = 15

if 5 <= age < 18:
    print("You can join a class!")
else:
    print("No luck.")









# Check if a value is equal to discrete set of values

















#_#

#__#        Tip & Trick  no 10      
# We want to use 
























#_#