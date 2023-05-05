import random

# this program is about who pay to bill

# this is to accept members and convert to list
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# randomisation
ran = random.randint(0, len(names))

# to print who pay to bill
print(f"{names[ran]} is going to buy the meal today!")
