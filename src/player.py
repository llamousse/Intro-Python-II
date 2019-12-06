# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, room):
        self.room = room
        self.items = []
    
    def print_inventory(self):
        if len(self.items) != 0:
            print("\n\nCurrent items in your bag: ")
            for i in self.items:
                print(f"{i.description} {i.name}\n")
        else:
            print("\n\nYour bag is currently empty.")