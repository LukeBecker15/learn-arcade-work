class Room:

    def __init__(self, description, north, south, east, west):

        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west


def main():
    room_list = []

    room = Room("You are in the entrance to the Clue house.\nThe path leads north.", 2, None, None, None)
    room_list.append(room)

    room = Room("You are in the billiard room.\nThe path leads north and east.", 4, None, 2, None)
    room_list.append(room)

    room = Room("You are in the ballroom.\nThe path leads north, south, east, and west.", 5, 0, 3, 1)
    room_list.append(room)

    room = Room("You are in the kitchen.\nThe path leads north and west.", 6, None, None, 2)
    room_list.append(room)

    room = Room("You are in the library.\nThe path leads south and east.", None, 1, 5, None)
    room_list.append(room)

    room = Room("You are in the study.\nThe path leads south, east, and west.", None, 2, 6, 4)
    room_list.append(room)

    room = Room("You are in the dining room.\nThe path leads south and west.", None, 3, None, 5)
    room_list.append(room)


    current_room = 0

    done = False
    while done == False:
        print()
        print(room_list[current_room].description)

        next_room = input("What direction do you want to move? ")
        if next_room.title() == "N" or next_room.title() == "North":
            next_room = room_list[current_room].north

            if next_room == None:
                print()
                print("You can't go this way")
            else:
                current_room = next_room
        elif next_room.title() == "S" or next_room.title() == "South":
            next_room = room_list[current_room].south
            if next_room == None:
                print()
                print("You can't go this way")
            else:
                current_room = next_room

        elif next_room.title() == "E" or next_room.title() == "East":
            next_room = room_list[current_room].east

            if next_room == None:
                print()
                print("You can't go this way")
            else:
                current_room = next_room

        elif next_room.title() == "W" or next_room.title() == "West":
            next_room = room_list[current_room].west

            if next_room == None:
                print()
                print("You can't go this way")
            else:
                current_room = next_room

        elif next_room.title() == "Q" or next_room.title() == "Quit":
            done = True
            print()
            print("The game is over")


main()
