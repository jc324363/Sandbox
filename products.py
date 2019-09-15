"""
0. Pattern-based programming
1. Names based on the problem domain
2. Functions at the same level of abstraction (main should "look like" the whole program)

Menu-driven product program
load products
- L_list products
- S_wap sale status (get product number with error checking)
- Q_uit (save file)
"""

# make CSV from list of lists
# with open ("products.csv", 'w') as output_file:
#     for product in products:
#         sale_status = 'y' if product[2] else 'n'
#         print("{},{}.{}".format(product[0], product[1], sale_status)

PRODUCTS_FILE = "products.csv"
MENU = """
 L_ist products
 S_wap sale status
 Q_uit
"""


def main():
    products = load_products()
    print(products)
    print(MENU)
    choice = input(">").upper()
    while choice != "Q":
        if choice == "L":
            list_products(products)
        elif choice == "S":
            swap_sale_status(products)
        else:
            print("Invalid")
        print(MENU)
        choice = input(">").upper()
    save_products(products)
    print("Finished")


def load_products():
    """Load lists of products"""
    product_lists = []
    file = open(PRODUCTS_FILE, 'r')
    for line in file:
        product = line.split(",")
        product_lists.append([product[0], float(product[1]), product[2][:-1]])
    file.close()
    return product_lists


def list_products(products):
    """Display list of products"""
    for number, product in enumerate(products):
        if product[2] == "y":
            print("{}. {:5} ${:7} is on sale".format(number, product[0], product[1]))
        else:
            print("{}. {:5} ${:7} is not on sale".format(number, product[0], product[1]))


def swap_sale_status(products):
    """get product number with error checking"""
    list_products(products)
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("?"))
            if number < 0:
                print("Product must be >= 0")
            elif number > len(products) - 1:
                print("Invalid product number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    print("{} swapped".format(products[number]))


def save_products(products):
    """save product to products.csv"""
    out_file = open(PRODUCTS_FILE, 'w')
    for product in products:
        out_file.writelines("{},{},{}\n".format(product[0], product[1], product[2]))
    out_file.close()


main()
