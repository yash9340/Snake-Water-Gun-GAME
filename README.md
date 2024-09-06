# SNAKE-WATER-GUN-GAME

Snake, Water, Gun is a humorous version of the famous "Rock, Paper, Scissors" game. This game in Python involves two players, the user and the computer-both playing a simple yet entertaining decision-making game. The rules for this are as follows:

### `Snake beats Water`: 
The snake drinks the water. In this case, when the user selects snake and the computer opts for water, the user is the winner.

### `Water beats Gun`:
The water quenches the gun; hence, for the case where a player selects water and the computer selects gun, the player wins.

### `Gun beats Snake`:
A gun shoots the snake. Where a player selects a gun and the computer selects a snake, the player wins.

## How the Game Works:

### `Game Start`:
The computer initiates the game by making one of three moves. Let the three possible moves be denoted as Water ('w'), Snake ('s'), or Gun ('g').

### `Player Input`: 
The player has to select one of the three options by typing 'w', 'g' or 's'. Program checks that only one of the three keys is entered.

### `Declaration of the Winner`: 
The game takes the player choice and the computer's choice and declares the result of the game. Here it does based on:

If both are the same, then it is a draw.
If the player's choice beats the computer's current choice based on the rules, he wins.

If the computer's choice beats the player's choice, he loses.

## Continue or Exit:
In every round, the game asks the player if he wants to play the game again or not. He should type '1' to continue or '0' to exit. In case the player inputs anything invalid, the game asks him to input a valid option.

### `Error Handling`:
The game includes very basic error handling to ensure only integers 0 or 1 are accepted for the continuation prompt.

# `The game loops until such time as the player elects to quit by entering '0'. This Python code has a main function that starts the game and is thus executable with a check that this script is the main one being run.`