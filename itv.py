
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
from json import dumps


class Session(object):
    def __init__(self, players):
        self.players = {p: 0 for p in players}
    
    def add(self, name):
        self.players[name] = 0
    
    def rm(self, name):
        del self.players[name]
    
    def show(self):
        print("\nInitiative Order:")
        print(dumps(self.players, indent = 2))
    
    def itv(self):
        print("\nRolling Initiative...")
        for k in self.players:
            self.players[k] = int(input(f"{k} Roll: "))
        sorted_names = sorted(self.players, key = lambda k: self.players[k], reverse = True)
        self.players = dict([(k, self.players[k]) for k in sorted_names])
        self.show()