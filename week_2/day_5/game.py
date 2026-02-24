""" Mini Project : Rock Paper Scissors

What You Will Create:
A Rock Paper Scissors game where the user plays against the computer, with a menu, game logic, and score tracking.

Instructions:
Create a directory for the game.
Create rock-paper-scissors.py (for menu, input, and summary).
Create game.py (for game logic). """

# Part I - game.py

# Step 1: Create the Game Class

import random

items = ["rock", "paper", "scissors"]

class Game:
    def __init__(self):
        pass

    # Step 2: Implement get_user_item Method

    def get_user_item(self):
        while True:
            user_item = input("\nSelect an item (rock/paper/scissors): ").lower()
            if user_item in items:
                return user_item
            else:
                print("Please enter rock/paper or scissors.")
                continue
    
    # Step 3: Implement get_computer_item Method

    def get_computer_item(self):
        computer_item = random.choice(items)
        return computer_item
    
    # Step 4: Implement get_game_result Method

    def get_game_result(self, user_item, computer_item):
        if computer_item == user_item:
            return "draw"
        
        # winning cases for the player:
        winning_cases = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        if winning_cases[user_item] == computer_item:
            return "win"
        else:
            return "loss"
        
    # Step 5: Implement play Method

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"\nuser's choice: {user_item}")
        print(f"computer's choice: {computer_item}")
        print(f"\nresult: {result}")
        return result


