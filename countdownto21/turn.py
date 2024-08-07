import random
def play_human_turn(n):
    choose = int(input("how many coins(1, 3) do you want?"))
    while choose < 1 or choose > 3 or choose > n:
        print("Please choose a number from 1-3 that is not more than the available coin")
        choose = int(input("how many coins (1, 3) do you want? "))
    n -= choose
    print(f"There are {n} coins left on the table.")
    # 1. prompt user for their move 
    if n == 0:
        print("Congratulations, You win!")
        return 0
    # 2. output number of coins after user's move
    # 3. If the human wins, indicate that and return 0
    # You must implement this function
    return n 
    #pass

def play_computer_turn(n):
    if n % 4 == 0:
        remove = random.randint(1, 3)
    else:
        remove = n % 4
    n -= remove
    print(f"Computer removed {remove} coins from the table.")
    
    if n == 0:
        print("computer wins")
        return 0

    return n
    # 1. Make computer move
    # 2. If computer wins, indicate that and return 0
    # 3. return number of coins remaining
        #pass
