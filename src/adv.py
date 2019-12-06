from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare all items

item = {
    'key': Item("key", "shiny"),
    'flashlight': Item("flashlight", "black"),
    'llama': Item("llama", "plushie"),
    'candy': Item("KitKat", "chocolate bar")
}

# Link items to respective rooms

room['foyer'].items.append(item['flashlight'])
room['overlook'].items.append(item['candy'])
room['narrow'].items.append(item['key'])
room['outside'].items.append(item['llama'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
adventurer = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Create a REPL loop to process commands

print("\n\n\nWelcome to the mystery cave.\nA hidden treasure lies within.\nWill you be the one to find the treasure?")
while True: # Loop
    
    if len(adventurer.room.items) == 0:
        print(f"\nYou are at the {adventurer.room.name}.\n{adventurer.room.description}\n")
    else:
        print(f"\nYou are at the {adventurer.room.name}.\n{adventurer.room.description}\nYou find the following items: ")
        adventurer.room.discover_items()
    
    # Read
    cmd = input("Choose a command to proceed.\n(n, e, s, w for directions, i for inventory) >>> ")

    # REPL should accept 'n', 'e', 's', 'w' commands
    # 'q' to quit
    # Eval
    if cmd == "n":
        if (adventurer.room.n_to != None):
            adventurer.room = adventurer.room.n_to
            pass
        else:
            print("Seems like you can't go that way...\n")
    elif cmd == "e":
        if (adventurer.room.e_to != None):
            adventurer.room = adventurer.room.e_to
            pass
        else:
            print("Seems like you can't go that way...\n")
    elif cmd == "s":
        if (adventurer.room.s_to != None):
            adventurer.room = adventurer.room.s_to
            pass
        else:
            print("Seems like you can't go that way...\n")
    elif cmd == "w":
        if (adventurer.room.w_to != None):
            adventurer.room = adventurer.room.w_to
            pass
        else:
            print("Seems like you can't go that way...\n")
    elif cmd == "i":
        adventurer.print_inventory()
        pass
    elif cmd == "q":
        # Break out of loop - quit game
        print("Come back soon, goodbye!")
        break
    else:
        #Print
        print("\nThat movement/command is not allowed! Please choose a valid command.")