temperatures = []

with open("data/data.csv", "r") as file:
    for line in file:
        clean_line = line.strip()
        parts = clean_line.split(",")
        temperatures.append(float(parts[1]))

print(temperatures)

if len(temperatures) > 0:
    print(sum(temperatures) / len(temperatures))
else: print("Error on data file")