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
                print(f"{i.description} {i.name}")
        else:
            print("\n\nYour bag is currently empty.")

    def on_take(self, item):
        self.room.items.remove(item)
        self.items.append(item)
        print(f"\nYou have picked up {item.description} {item.name}!")
    
    def on_drop(self, item):
        self.items.remove(item)
        self.room.items.append(item)
        print(f"\n{item.description} {item.name} has been dropped!")