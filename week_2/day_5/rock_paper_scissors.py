# Part II - rock-paper-scissors.py

# Step 6: Implement get_user_menu_choice Function

from game import Game

def get_user_menu_choice():
    while True:
        print("----------------")
        print("\nMENU OPTIONS:")
        print("\n1. Play a new game\n2. Show scores\n3. Quit")
        user_choice = input("\nChoose an option: ")
        if not user_choice.isdigit():
            print("Please enter a number.")
            continue
        if int(user_choice) not in [1, 2, 3]:
            print("Please enter a number between 1 and 3")
            continue
        else:
            return int(user_choice)


# Step 7: Implement print_results Function

def print_results(results):
    print("\nRESULTS:")
    print(f"\nWins: {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws: {results['draw']}")
    print("\nThank you for playing !")

# Step 8: Implement main Function

def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice == 1:
            game = Game()
            result = game.play()
            results[result] += 1

        elif choice == 2:
            print_results(results)

        elif choice == 3:
            break

if __name__ == "__main__":
    main()




   
