                                    # Snake, Water, Gun Game
                    # In this game, snake beats water, gun beats snake, and water beats gun.

def game():
    a = ["w", "s", "g"]  # Options: Water, Snake, Gun
    import random as rn  # Using random to randomly choose one out of 3.
    x = rn.choice(a)  # Computer's choice
    print(f"Computer's turn: {x}")
    print('Choose one:\n'
          'w = Water\n'
          'g = Gun\n'
          's = Snake')  # Option shortcuts
    opt = ("w", "g", "s")  # Valid options

    while True:
        d = input('Your turn: ').lower()  # User input
        if d in opt:
            d = d
            break
        else:
            print('Please type a correct input.')

    # Checking for input...
    if d == x:
        print('Draw')
    elif x == "s":
        if d == "w":
            print('You lose.')
        elif d == "g":
            print('You win.')
        else:
            print('Wrong input.')
    elif x == "g":
        if d == "w":
            print('You win.')
        elif d == "s":
            print('You lose.')
        else:
            print('Wrong input.')
    elif x == 'w':
        if d == "g":
            print('You lose.')
        elif d == "s":
            print('You win.')
        else:
            print('Wrong input.')

    # ASKING TO PLAY...
    while True:
        try:
            x = int(input('Type 1 to continue or 0 to exit: '))
            if x == 0:
                print('Ok, exiting.')
                break
            elif x == 1:
                a = ["w", "s", "g"] # Options: Water, Snake, Gun
                x = rn.choice(a) # Computer's choice
                print(f"Computer's turn: {x}")
                print('Choose one:\n'
                      'w = Water\n'
                      'g = Gun\n'
                      's = Snake') # Option shortcuts
                while True:
                    d = input('Your turn: ').lower()
                    if d in opt:
                        d = d
                        break
                    else:
                        print('Please type a correct input.')
                if d == x:
                    print('Draw')
                elif x == "s":
                    if d == "w":
                        print('You lose.')
                    elif d == "g":
                        print('You win.')
                    else:
                        print('Wrong input.')
                elif x == "g":
                    if d == "w":
                        print('You win.')
                    elif d == "s":
                        print('You lose.')
                    else:
                        print('Wrong input.')
                elif x == 'w':
                    if d == "g":
                        print('You lose.')
                    elif d == "s":
                        print('You win.')
                    else:
                        print('Wrong input.')
            else:
                print('Wrong input.')
        except:
            print("Please type an integer (0/1):")


game()
