import random


def main():
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        user_choice = input("What is your choice? ")
        if user_choice.title() == "Q":
            print("Game Over")
            done = True
        elif user_choice.title() == "E":
            print("Miles traveled:", miles_traveled)
            print("Drinks in canteen:", canteen_drinks)
            print("The natives are", miles_traveled - natives_distance, "miles behind you.")
        elif user_choice.title() == "D":
            camel_tiredness = 0
            print("The camel is happy.")
            natives_distance += random.randrange(7, 15)
        elif user_choice.title() == "C":
            miles_traveled += random.randrange(10, 21)
            print("You have traveled", miles_traveled, "miles.")
            thirst += 1
            camel_tiredness += random.randrange(1,4)
            natives_distance += random.randrange(7, 15)
            if random.randrange(19) == 0:
                print("You have found an oasis!")
                print("Your canteen is full.")
                print("Your thirst is zero.")
                print("Your camel is rested.")
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif user_choice.title() == "B":
            miles_traveled += random.randrange(5, 13)
            print("You have traveled", miles_traveled, "miles.")
            thirst += 1
            camel_tiredness += 1
            natives_distance += random.randrange(7, 15)
            if random.randrange(19) == 0:
                print("You have found an oasis!")
                print("Your canteen is full.")
                print("Your thirst is zero.")
                print("Your camel is rested.")
                canteen_drinks = 3
                thirst = 0
                camel_tiredness = 0
        elif user_choice.title() == "A":
            if canteen_drinks <= 0:
                print("You have no drinks.")
            else:
                canteen_drinks -= 1
                thirst = 0
        if thirst > 4 and thirst <= 6:
            print("You are thirsty.")
        elif thirst > 6:
            print("You died of thirst.")
            done = True
        if camel_tiredness > 5 and camel_tiredness <= 8:
            print("Your camel is getting tired.")
        elif camel_tiredness > 8:
            print("Your camel is dead.")
            done = True
        if natives_distance > miles_traveled - 15 and natives_distance < miles_traveled:
            print("The natives are getting close!")
        elif natives_distance >= miles_traveled:
            print("The natives have caught you. You have died.")
            done = True
        if miles_traveled >= 200:
            print("Congratulations you have survived the desert!")
            done = True

main()
