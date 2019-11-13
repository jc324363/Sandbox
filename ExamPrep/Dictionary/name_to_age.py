"""
Given the existing dictionary, write code to prompt the user for a name and age,
add these to the dictionary, then display all of the data nicely.
"""
name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
name = input("Name: ")
age = int(input("Age: "))
for name, age in name_to_age.items():
    print("{:6} - {:6}".format(name, age))
