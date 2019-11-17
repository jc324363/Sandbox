"""
Write Python code to ask the user for their age, then print the square of each each number from
that age down to zero
"""

age = int(input("Age: "))
for i in range(age, -1, -1):
    print(i * 2)

print("----------------------")
"""
Write a for loop that prints Olympic years (every 4 years) from 1900 to now
"""

for year in range(1900, 2020, 4):
    print(year)
