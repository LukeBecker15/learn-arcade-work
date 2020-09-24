def main():



    room_list = []
    a = "You are in the entrance to the Clue house\nThe path leads north"
    n = 2
    e = None
    w = None
    s = None
    room_0 = [a, n, e, w, s]
    room_list.append(room_0)

    a1 = "You are in the billiard room\nThe path leads north and east"
    n1 = 4
    e1 = 2
    w1 = None
    s1 = None
    room_1 = [a1, n1, e1, w1, s1]
    room_list.append(room_1)

    a2 = "You are in the ballroom\nThe path leads north, south, east, and west"
    n2 = 5
    e2 = 3
    w2 = 1
    s2 = 0
    room_2 = [a2, n2, e2, w2, s2,]
    room_list.append(room_2)

    a3 = "You are in the kitchen\nThe path leads north and west"
    n3 = 6
    e3 = None
    w3 = 2
    s3 = None
    room_3 = [a3, n3, e3, w3, s3]
    room_list.append(room_3)

    a4 = "You are in the library\nThe path leads south and east"
    n4 = None
    e4 = 5
    w4 = None
    s4 = 1
    room_4 = [a4, n4, e4, w4, s4]
    room_list.append(room_4)

    a5 = "You are in the study\nThe path leads south, east, and west"
    n5 = None
    e5 = 6
    w5 = 4
    s5 = 2
    room_5 = [a5, n5, e5, w5, s5]
    room_list.append(room_5)

    a6 = "You are in the dining room\nThe path leads south and west"
    n6 = None
    e6 = None
    w6 = 5
    s6 = 3
    room_6 = [a6, n6, e6, w6, s6]
    room_list.append(room_6)

    done = False
    while not done:


        current_room = 0
        print()
        print(room_list[current_room][0])

        move_room = input("What direction do you want to move? ")
        if move_room.title() == "N" or move_room.title() == "North":
            next_room = room_list[current_room][1]
            if next_room == None:
                print("You can't go this way")
                current_room = next_room
        elif move_room.title() == "S" or move_room.title() == "South":
            next_room = room_list[current_room][4]
            if next_room == None:
                print("You can't go this way")
                current_room = next_room



main()