""" A program to keep track of appropriate drinking"""

from Classes.drink import Drink
from Classes.drink_list import DrinkList

MENU = """Menu:
L = Load Available Drinks
A = Add new drink
T = Take a drink
Q = Quit
"""


def main():
    available_drinks = load_drinks("drinks.csv")
    my_drinks = DrinkList

    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != 'Q':
        if menu_choice == 'A':
            display_available_drinks(available_drinks)
            drink_choice = int(input(">>>"))
            my_drinks.add(available_drinks[drink_choice])
        else:
            print("Invalid")
        print(my_drinks)
        print(MENU)
        menu_choice = input(">").upper()
    print("You drank {} drinks ({} were alcoholic for a total of {} ml alcohol), which cost ${:.2f}".format(
        len(my_drinks), my_drinks.get_number_alcoholic(), my_drinks.get_alcohol_volume(), my_drinks.get_total_price()))


def display_available_drinks(drinks):
    print([(i, str(drink)) for i, drink in enumerate(drinks)])


def load_drinks(filename):
    drinks = []
    input_file = open(filename)
    for line in input_file:
        parts = line.strip().split(',')  # remove \n
        print(parts)  # print(parts) to validate the output

        drinks.append(Drink(parts[0], float(parts[1]), float(parts[2]), float(parts[3])))
    input_file.close()
    return drinks


main()
