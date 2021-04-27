import random
import sys
print('\n\t\t Your Turn\n')
inp = 1
output = 'yes'
while (inp):
    if inp == 1:
        dice = random.randint(1,6)
        print('\t\t\tDice says: ', dice, '\n')
        output = input('\t\tDo you want to roll again? ')
    else:
        output = input("\t\tPrint 'yes' or 'no'\n Want to roll the dice once more? ")
    if output.lower() == 'yes' or output.lower() == 'y':
        inp = 1
    elif output.lower() == 'no' or output.lower() == 'n':
        inp = 0
    else:
        inp = 2
print("\nEND\n")
