import csv

"""
I added the feature to remove dashes in the id number and also made the fuction restart when an error is input. The user can also quit.
"""

def main():
    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary("students.csv", KEY_INDEX)
    i_number = input("""Please enter an I number (or type "quit" to exit): """)
    i_number = i_number.replace("-", "")
    print(i_number)

    if i_number in students:
        student = students[i_number]
        name = student[NAME_INDEX]
        print(f"Name: {name}")

    elif i_number.lower() == "quit":
        exit

    else:
        print("No such student.")
        main()

def read_dictionary(filename, key_column_index):
    student_dict = {}
    with open(filename, "rt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            key_value = row[key_column_index]
            student_dict[key_value] = row
    return student_dict

if __name__ == "__main__":
    main()