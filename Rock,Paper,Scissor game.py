a = input('YOUR NAME :')
b = input("YOUR OPPONENT'S NAME :")

import random

x = ['ROCK', 'PAPER', 'SCISSOR']

ax = random.choice(x)
by = random.choice(x)
print('{} choice is {}\n'.format(a, random.choice(x)))
print('{} choice is {}\n'.format(b, random.choice(x)))
if ax == by:
    print("""''' --ONE MORE ROUND-- '''""")
else :
    if ax == 'ROCK' and by == 'PAPER':
         ax_value = 0
         by_value = 1
    elif ax == 'ROCK' and by == 'SCISSOR':
         ax_value = 1
         by_value = 0
    elif ax == 'PAPER' and by == 'ROCK':
          ax_value = 1
          by_value = 0
    elif ax == 'PAPER' and by == 'SCISSOR':
         ax_value = 0
         by_value = 1
    elif ax == 'SCISSOR' and by == 'ROCK':
         ax_value = 0
         by_value = 1
    elif ax == 'SCISSOR' and by == 'PAPER':
         ax_value = 1
         by_value = 0
    if ax_value == 1 and by_value == 0:
          print("''' --{} won-- '''".format(a))
    elif ax_value == 0 and by_value == 1:
          print('{} won'.format(b))
