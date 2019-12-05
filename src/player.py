# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, current_room):
        self.room = current_room
        self.items = []
    
    def print_inventory(self):
        if len(self.items) != 0:
            print(f"\n\nCurrent items in your bag: {self.items}")
        else:
            print("\n\nYour bag is currently empty.")