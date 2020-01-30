from statistics import mean

def reader(filename):
    file = open(filename, "r", encoding="utf-8")
    while True:
        yield file.readline()
        

###########################
#
#   GENERATORS PROVIDE DATA
#     ONE ITEM AT A TIME
#
###########################


def main():
    generator = reader("data.title.basics.tsv")
    genres = {}

    next(generator)

    while True:
        value = next(generator)

        if value == "":
            break
            
        id, title_type, primary_title, secondary_title, a, start_year, end_year, runtime, genre_string = value.strip("\n").split("\t")

        for genre in genre_string.split(","):
            # Check if the genre already exists in the dictionary
            # If so, increment the value, otherwise start it at 0
            if genre in genres.keys():
                genres[genre] += 1
            else:
                genres[genre] = 1

    with open("imdb-data-output.txt", "w") as file:
        file.write("\n".join(map(str, genres.items())))


main()






# print(len(data))
# masses = []
# for line in data.splitlines():
#     name, id, type, recclass, mass, fall, year, lat, long, geo = line.split("")
#     masses.append(int(mass))

# print("Smallest meteorite weighed: {}".format(min(masses)))
# print("Largest meteorite weighed: {}".format(max(masses)))
# print("Average of all meteorite weights was: {}".format(mean(masses)))