                                #WE WANT TO CREATE SNAKE,WATER,GUN GAME.
                        #IN THIS GAME SNAKE BEATS WATER,GUN BEATS SNAKE,WATER BEATS GUN. 

def game():
    a=["w","s","g"] 
    import random as rn  #USING RANDOM TO RANDOMLY CHOOSE ONE OUT OF 3.
    x=rn.choice(a)
    print(f"Computer's turn: {x}")
    print('Choose one:-\nw = Water\ng = Gun\ns = Snake') #HERE WE TELL SHOW OPTIONS.
    opt = ("w","g","s")
    while True:
        d=input('Your turn:- ').lower()
        if d in opt:
            d=d
            break
        else:
            print('Please type correct input.')

    if d == x:
        print('Draw')
    elif x == "s":
        if d == "w":
            print('You loss.')
        elif d == "g":
            print('You Win.')
        else:
            print('Wrong input.')
    elif x =="g":
        if d == "w":
            print('You Win.')
        elif d == "s":
            print('You Loss.')
        else:
            print('Wrong input.')
    elif x == 'w':
        if d == "g":
            print('You Loss.')
        elif d == "s":
            print('You Win.')
        else:
            print('Wrong input.')
    while True:
        try:
            x=int(input('Type 1 for continue or 0 to exit: '))
            if x==0:
                print('Ok exited.')
                break
            elif x==1:
                a=["w","s","g"]
                x=rn.choice(a)
                print(f"Computer's turn: {x}")
                print('Choose one:-\nw = Water\ng = Gun\ns = Snake')
                while True:
                    d=input('Your turn:- ').lower()
                    if d in opt:
                        d=d
                        break
                    else:
                        print('Please type correct input.')
                if d == x:
                    print('Draw')
                elif x == "s":
                    if d == "w":
                        print('You loss.')
                    elif d == "g":
                        print('You Win.')
                    else:
                        print('Wrong input.')
                elif x =="g":
                    if d == "w":
                        print('You Win.')
                    elif d == "s":
                        print('You Loss.')
                    else:
                        print('Wrong input.')
                elif x == 'w':
                    if d == "g":
                        print('You Loss.')
                    elif d == "s":
                        print('You Win.')
                    else:
                        print('Wrong input.')
            else:
                print('Wrong input.')
        except:
            print("please type integer 0/1: ")

    
        
game()