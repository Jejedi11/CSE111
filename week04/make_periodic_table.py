
periodic_table_dict = {}

with open("elements.txt", "r") as file:
    line = file.readlines()
    print(line[0])

    for i in line:
        data = i.split(",")
        periodic_table_dict[data[0]] = [data[1].strip(), float(data[2].strip())]
    print(periodic_table_dict)

    print(periodic_table_dict["Au"])