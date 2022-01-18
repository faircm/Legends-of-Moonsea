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
        self.location = 'b2'
        self.game_over = False


my_player = Player()

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

zone_map = {
    'a1': {ZONENAME: "Town Hospital",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: '',
           DOWN: 'b1',
           LEFT: '',
           RIGHT: 'a2'
           },
    'a2': {ZONENAME: "Town Entrance",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: '',
           DOWN: 'b2',
           LEFT: 'a1',
           RIGHT: 'a3'
           },
    'a3': {ZONENAME: "Town Square",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: '',
           DOWN: 'b3',
           LEFT: 'a2',
           RIGHT: 'a4'
           },
    'a4': {ZONENAME: "Town Hall",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: '',
           DOWN: 'b4',
           LEFT: 'a3',
           RIGHT: ''
           },
    'b1': {ZONENAME: "Grassy Plain 1",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'a1',
           DOWN: 'c1',
           LEFT: '',
           RIGHT: 'b2'
           },
    'b2': {ZONENAME: "Campsite",
           DESCRIPTION: 'This is your tent',
           EXAMINATION: 'You feel safe here',
           CLEARED: True,
           UP: 'a2',
           DOWN: 'c2',
           LEFT: 'b1',
           RIGHT: 'b3'
           },
    'b3': {ZONENAME: "Grassy Plain 3",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'a3',
           DOWN: 'c3',
           LEFT: 'b2',
           RIGHT: 'b4'
           },
    'b4': {ZONENAME: "Grassy Plain 4",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'a4',
           DOWN: 'c4',
           LEFT: 'b3',
           RIGHT: ''
           },
    'c1': {ZONENAME: "Dark Woods 1",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'b1',
           DOWN: 'd1',
           LEFT: '',
           RIGHT: 'c2'
           },
    'c2': {ZONENAME: "Dark Woods 2",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'b2',
           DOWN: 'd2',
           LEFT: 'c1',
           RIGHT: 'c3'
           },
    'c3': {ZONENAME: "Dark Woods 3",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'b3',
           DOWN: 'd3',
           LEFT: 'c2',
           RIGHT: 'c4'
           },
    'c4': {ZONENAME: "Dark Woods 4",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'b4',
           DOWN: 'd4',
           LEFT: 'c3',
           RIGHT: ''
           },
    'd1': {ZONENAME: "Burned Village 1",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'c1',
           DOWN: '',
           LEFT: '',
           RIGHT: 'd2'
           },
    'd2': {ZONENAME: "Burned Village 2",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'c2',
           DOWN: '',
           LEFT: 'd1',
           RIGHT: 'd3'
           },
    'd3': {ZONENAME: "Burned Village 3",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'c3',
           DOWN: '',
           LEFT: 'd2',
           RIGHT: 'd4'
           },
    'd4': {ZONENAME: "Burned Village 4",
           DESCRIPTION: 'description',
           EXAMINATION: 'examination',
           CLEARED: False,
           UP: 'c4',
           DOWN: '',
           LEFT: 'd3',
           RIGHT: ''
           }
}

# Title Screen Function

def title_screen_selections():
    option = input('>> ')
    if option.lower() == 'play':
        start_game()
    elif option.lower() == 'help':
        help_menu()
    elif option.lower() == 'quit':
        print('Are you sure you wish to exit?')
        if input().lower() == 'y' or 'yes':
            sys.exit()
    else:
        print('Please enter a valid command.')
        title_screen_selections()


def title_screen():
    os.system('cls')
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

# Game interactivity


def print_location():
    print('\n' + ('#' * (4 + len(my_player.location))))
    print('# ' + my_player.location.upper() + ' #')
    print('# ' + zone_map[my_player.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(my_player.location))))


def prompt():
    print('\n' + '====================================')
    print('What would you like to do?')
    action = input('>> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'quit', 'exit', 'examine', 'inspect', 'interact', 'look']
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again")
        prompt()
    if action.lower() == 'quit' or 'exit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    if action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())


def player_move(my_action):
    ask = 'In what direction?\n'
    direction = input(ask).lower()
    if direction in ['up', 'north']:
        direction = zone_map[my_player.location][UP]
        movement_handler(direction)
    elif direction in ['down', 'south']:
        direction = zone_map[my_player.location][DOWN]
        movement_handler(direction)
    elif direction in ['right', 'east']:
        direction = zone_map[my_player.location][RIGHT]
        movement_handler(direction)
    elif direction in ['left', 'west']:
        direction = zone_map[my_player.location][LEFT]
        movement_handler(direction)


def movement_handler(direction):
    print('\nYou have moved to the' + direction + '.')
    my_player.location = direction
    print_location()


def player_examine(action):
    if zone_map[my_player.location][CLEARED]:
        print('This zone has already been cleared.')
    else:
        print('Events here.')


# Game functionality
def start_game():
    setup_game()
    main_game_loop()


def main_game_loop():
    while my_player.game_over is False:
        prompt()
        # Check if all zones cleared, enemies defeated, etc.


def setup_game():
    os.system('cls')
    ask_name = "What is your name?\n"
    for character in ask_name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.009)
    player_name = input('>> ')
    my_player.name = player_name

    ask_job = f"What is your job, {my_player.name}?\n"
    for character in ask_job:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.009)
    player_job = input('>> ')
    while player_job.lower() not in ['warrior', 'mage', 'rogue']:
        print("This is not a valid job, please choose either Warrior, Mage or Rogue.\n")
        player_job = input('>> ')
    my_player.job = player_job.lower()
    # print(f"You have chosen the {my_player.job} class.\n")

    if my_player.job == 'warrior':
        my_player.hp = 20
        my_player.mp = 5
    elif my_player.job == 'mage':
        my_player.hp = 10
        my_player.mp = 20
    elif my_player.job == 'rogue':
        my_player.hp = 15
        my_player.mp = 10

    welcome_message = f'''Welcome, .\n
    Welcome to Moonsea, {my_player.name} the {my_player.job}...\n
    You feel a storm brewing around you...\n
    Watch the shadows closely...'''
    for character in welcome_message:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.009)
    time.sleep(1.5)
    os.system('cls')

title_screen()
