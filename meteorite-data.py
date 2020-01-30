from statistics import mean

def reader(filename):
    with open(filename, "r") as file:
        data = file.read()
        
        print(len(data))
        masses = []
        for line in data.splitlines():
            name, id, type, recclass, mass, fall, year, lat, long, geo = line.split("")
            masses.append(int(mass))
        
        print("Smallest meteorite weighed: {}".format(min(masses)))
        print("Largest meteorite weighed: {}".format(max(masses)))
        print("Average of all meteorite weights was: {}".format(mean(masses)))


reader("meteorites.csv")
