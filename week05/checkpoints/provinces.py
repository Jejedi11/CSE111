list = []

def main():
    read_file("checkpoints/provinces.txt")
    print(list)
    list.pop(0)
    list.pop(int(len(list)) - 1)
    replace_in_list("AB", "Alberta")
    print(count())

def read_file(filename):
    with open(filename) as file:
        for line in file:
            list.append(line.strip())

def replace_in_list(inplace, replace):
    index = 0
    for i in list:
        if i == inplace:
            list[index] = replace
        index += 1

def count():
    count = 0
    for i in list:
        if i == "Alberta":
            count +=1
    return count

if __name__ == "__main__":
    main()