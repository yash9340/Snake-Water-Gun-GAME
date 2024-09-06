# SNAKE-WATER-GUN-GAME

The Snake, Water, Gun game is a playful twist on the classic "Rock, Paper, Scissors" game. In this Python-coded game, players compete against the computer in a simple but engaging decision-making challenge. The rules are straightforward:

#Snake beats Water: The snake consumes the water, so if the player chooses snake and the computer chooses water, the player wins.
Water beats Gun: The water extinguishes the gun, so if the player chooses water and the computer chooses gun, the player wins.
Gun beats Snake: The gun shoots the snake, so if the player chooses gun and the computer chooses snake, the player wins.
Here’s how the game works:

Game Start: The game begins with the computer randomly selecting one of the three options: Water (represented by 'w'), Snake (represented by 's'), or Gun (represented by 'g').

Player Input: The player is prompted to choose one of the three options by typing 'w', 'g', or 's'. The game ensures that only valid inputs are accepted.

Determine the Winner: The game compares the player’s choice with the computer’s choice and declares the result:

If both choices are the same, the result is a draw.
If the player’s choice beats the computer’s choice based on the rules, the player wins.
If the computer’s choice beats the player’s choice, the player loses.
Continue or Exit: After each round, the player is asked if they want to play again. They can type '1' to continue or '0' to exit. If an invalid input is provided, the game prompts the player to enter a correct option.

Error Handling: The game includes basic error handling to ensure that only integers (0 or 1) are accepted for the continuation prompt.

The game loop continues until the player chooses to exit by typing '0'. This Python code is structured with a main function that initiates the game and can be easily run by checking if the script is being executed as the main program.
