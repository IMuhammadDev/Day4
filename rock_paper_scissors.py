import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_off_sy = [rock, paper, scissors]  # tosh , qogoz , qaychi

you = int(input("choose situation (rock = o , paper = 1 , scissors = 2): "))
comp = random.randint(0, 2)

print("YOU")
print(list_off_sy[you])
print()

print("COMPUTER")
print(list_off_sy[comp])

if you == 0:
    if comp == 0:
        print("equal")
    elif comp == 1:
        print("computer winn")
    else:
        print("you winn")
elif you == 1:
    if comp == 0:
        print("you winn ")
    elif comp == 1:
        print("equal")
    else:
        print("computer winn")
else:
    if comp == 0:
        print("computer winn ")
    elif comp == 1:
        print("you winn")
    else:
        print("equal")