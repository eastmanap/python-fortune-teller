# Apollos Eastman
# 10/23
# Fortune Teller

import random
import sys
import time

#lists
fortunes = ['You are a winner!','A secret admirer will soon send you a sign of affection!',
            'The one you love is much closer than you think!',
            'Good things will happen to you by the end of the day today!',
            'Fame and fortune will be yours if you take the time to learn Python!', 
            'I\'m just a computer program, and have no magical powers!']

magic_colors = ['blue','red','green','yellow']

#input name

user_name = input('Enter your first name:\n')

print(f'Welcome to my Fortune Teller {user_name}!\n')

question = input('Do you wish to have your fortune told? [y/n]\n')
time.sleep(2)
# Calculation

if question.lower() == 'yes' or question.lower() == 'y':
    time.sleep(1)
    color = input('Okay! To get your fortune, please input a magic color: [blue/red/green/yellow]\n')
    time.sleep(2)
    print(f'Here is your fortune, {user_name}:\n')
    time.sleep(1)

    if color in magic_colors:
        index = random.randint(0, len(fortunes)-1)
        print(fortunes[index])
        print()
    
    else:
        print('Please choose a magic color of either blue, red, green, or yellow.\n')
        time.sleep(1)
        print('Once you have input a magic color, I will reveal your fortune!\n')
else:
    print(f'Thank you for playing my Fortune Teller game today, {user_name}.\n')
    print('Goodbye!')
    quit()

print(f'Thank you for playing my Fortune Teller game today, {user_name}.')
print('Goodbye!')
