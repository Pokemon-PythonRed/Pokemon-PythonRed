#import
from random import *
import math
import time

#vars
startOption=0
playerGender=0
playerName=''

#start menu
print('')
print('         Pokemon PythonRed Version')
time.sleep(4)
print('')
input('            Press Enter to begin')
print('')
print('1. New Game')
print('2. Continue')
print('')
while startOption!='1' and startOption!='2':
    startOption=input('>')
    print('')
    if startOption!='1' and startOption!='2':
        print('Invalid answer!')
if startOption=='2':
    input('Saving and continuing coming soon! Please restart!')
    while True:
        input('Please restart!')

'''#intro
print('Please wait..')
time.sleep(5)
print('')
print('')'''

input('That\'s all for now, thanks!')
