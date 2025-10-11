"""
To save me some time I made the make_periodic_table function read the elements.txt file which contains the provided mass for each element,
this way the program automatically formats the information to be usable without me having to do it manually.

Author: James Michelson
Purpose: To output the molar mass and number of moles based off of the input of a user for the chemical formula and sample size.
"""

from formula import parse_formula

def main():
    # Gathering data from user
    chem_formula = input("Input the chemical formula: ")
    sample_size = input("What is the sample size (in grams)? ")

    # Make the periodic table dictionary
    periodic_table_dict = make_periodic_table()
    
    # Get the quantity list from the parse_formula function
    symbol_quantity_list = parse_formula(chem_formula, periodic_table_dict)

    #get the molar mass
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    print(f"Molar Mass: {molar_mass}")

    # Calculate the number of moles
    num_of_moles = float(sample_size) / molar_mass
    print(f"Number of Moles: {round(num_of_moles, 5)}")

def make_periodic_table():
    """
    Creates a dictionary of the periodic table provided by the elements.txt file.
    """
    periodic_table_dict = {}
    with open("elements.txt", "r") as file:
        line = file.readlines()

        for i in line:
            data = i.split(",")
            periodic_table_dict[data[0]] = [data[1].strip(), float(data[2].strip())]
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """
    Computes the molar mass using the parsed chemical formula and periodic table dictionary
    """
    molar_mass  = 0
    for symbol_quantity in symbol_quantity_list:
        #The symbol quantity list has nested lists
        element = periodic_table_dict[symbol_quantity[0]]
        molar_mass += float(element[1]) * int(symbol_quantity[1])
    return molar_mass

if __name__ == "__main__":
    main()