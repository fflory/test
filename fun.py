import random

def introduction():
    print("Welcome to the Adventure Game!")
    print("You are standing at the edge of a dark forest.")
    print("In front of you are two paths: a left path and a right path.")
    print("what will you do?")
    print("Which path will you choose?")

def choose_path():
    choice = input("Type 'left' or 'right': ").strip().lower()
    if choice == 'left':
        encounter_wolf()
    elif choice == 'right':
        find_treasure()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        choose_path()

def encounter_wolf():
    print("You follow the left path and encounter a wild wolf!")
    action = input("Do you want to 'fight' the wolf or 'run' away? ").strip().lower()
    if action == 'fight':
        if random.choice([True, False]):
            print("You fought bravely and defeated the wolf!")
        else:
            print("The wolf was too strong. You had to run away!")
            choose_path()
    elif action == 'run':
        print("You ran away safely and found yourself back at the start.")
        choose_path()
    else:
        print("Invalid choice. Please choose 'fight' or 'run'.")
        encounter_wolf()

def find_treasure():
    print("You follow the right path and discover a hidden treasure chest!")
    action = input("Do you want to 'open' the chest or 'leave' it alone? ").strip().lower()
    if action == 'open':
        if random.choice([True, False]):
            print("Congratulations! You found a pile of gold and precious gems!")
        else:
            print("Oh no! The chest was a trap and you got covered in confetti!")
            choose_path()
    elif action == 'leave':
        print("You leave the chest alone and find yourself back at the start.")
        choose_path()
    else:
        print("Invalid choice. Please choose 'open' or 'leave'.")
        find_treasure()

def main():
    introduction()
    choose_path()

if __name__ == "__main__":
    main()
