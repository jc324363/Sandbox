"""Write a list comprehension to produce a new list containing only the products that are on sale
(True means it's on sale)
"""

products = [["phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
print(products)

on_sale_products = [product[0] for product in products if product[2]]
print(on_sale_products)
print(sum([product[1] for product in products if product[2]]))
