"""
Author: James Michelson
Purpose: Prints a receipt for a customer's order.
Additions: I added a countdown timer at the bottom reminding the customer how many days until the New Years sale.
"""

import csv
import datetime

def read_dictionary(filename, key_column_index):
    store_dict = {}
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for line in csv_reader:
            store_dict[line[key_column_index]] = [line[1], line[2]]
    return store_dict

def main():
    try:
        KEY_INDEX = 0
        products_dict = read_dictionary("week05/products.csv", KEY_INDEX)
        num_of_items = 0
        subtotal = 0.00
        print("Steven's Freshest Market")
        print("")
        with open("week05/request.csv", "rt") as csv_file:
            requests = csv.reader(csv_file, delimiter=",")
            next(requests)
            for line in requests:
                print(f"Name: {products_dict[line[KEY_INDEX]][0]} {line[1]} @ {products_dict[line[KEY_INDEX]][1]} ")
                num_of_items += 1
                subtotal += float(products_dict[line[0]][1])
        sales_tax = subtotal * 0.06
        date = datetime.datetime.now().strftime("%Y-%M-%d %H:%M:%S")
        days_to_sale = (datetime.date(2026, 1, 1) - datetime.date.today()).days

        print(f"Number of items: {num_of_items}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Sales Tax: ${sales_tax:.2f}")
        print(f"Total: ${(subtotal + sales_tax):.2f}")
        print("")
        print("Thank you for shopping at Steven's Freshest Market!")
        print(date)
        print("")
        print(f"{days_to_sale} days to New Years sale!")
    except FileNotFoundError as file_error:
        print("Error: missing file")
        print(file_error)
    except PermissionError as permission_error:
        print("Error: invalid permissions")
        print(permission_error)
    except KeyError as key_error:
        print("Error: an unkown ID was found in the request.csv")
        print(key_error)

if __name__ == "__main__":
    main()