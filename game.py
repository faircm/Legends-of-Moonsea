# Python text-based RPG
# Created using the Bryan Tong tutorial at https://youtu.be/xHPmXArK6Tg
# Inspired by Wizards of the Coast's Shadows over the Moonsea

import cmd
import textwrap
import sys
import os
import time
import random
import math

screen_width = 100

# Player class
class Player:
    def __init__(self):
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
my_player = Player()

# Title Screen Function
def title_screen_selections():
    option = input('>> ')
    if option.lower() == 'play':
        pass
        # start_game() PLACEHOLDER
    elif option.lower() == 'help':
        pass
        # help_menu() PLACEHOLDER
    elif option.lower() == 'quit':
        print('Are you sure you wish to exit?')
        if input().lower() == 'y' or 'yes':
            sys.exit()
    else:
        print('Please enter a valid command.')
        title_screen_selections()

def title_screen():
    os.system('clear')
    print('#####################################')
    print('# Welcome to the Legends of Moonsea #')
    print('#####################################')
    print('*              -PLAY-               *')
    print('*              -HELP-               *')
    print('*              -QUIT-               *')
    title_screen_selections()

def help_menu():
    print('#####################################')
    print('# Welcome to the Legends of Moonsea #')
    print('#####################################')
    print('*       Use arrow keys to move      *')
    print('*    Type commands to do actions    *')
    print('*    Type look to inspect objects   *')
    title_screen_selections()

# Game functionality
def start_game():


# Map
a1 a2... PLAYER STARTS AT B2
----------------------------
|        |        |        |    a4
----------------------------
|        |        |        |    b4...
----------------------------
|        |        |        |
----------------------------
|        |        |        |
----------------------------
ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
CLEARED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

cleared_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False
    }

zome_map = {
    'a1': { ZONENAME : "",
            DESCRIPTION : 'description',
            EXAMINATION : 'examination',
            CLEARED : False,
            UP : ('up', 'north'),
            DOWN : ('down', 'south'),
            LEFT : ('left', 'west'),
            RIGHT : ('right', 'east') 
            }
}