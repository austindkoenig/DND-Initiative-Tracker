
'''
Initiative Tracker

Useful program to track initiative order in Dungeons and Dragons gameplay.

Uses
----

Features
--------
- Keep track of the players in a session
- Easily add and remove players
- Initiative order

'''

import pprint

printer = pprint.PrettyPrinter(indent = 4, sort_dicts = True)
players = {}

def add(name):
    players[name] = 0

def remove(name):
    del players[name]

def show():
    print('Initiative Order: ')
    printer.pprint(players)
    print()

def itv():
    print('\nRolling Initiative...\n')
    for p in players:
        players[p] = input(f'{p} Itv Roll: ')
    
    print()
    show()