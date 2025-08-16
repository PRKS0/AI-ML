# snake water gun (error handeling)

import random
comp = random.randint(0, 2)

option = ['gun', 'water', 'snake']

while True:
    try:
        user = int(input("Snake(2), Water(1), Gun(0): "))
        if user in (0, 1, 2):
            def comparison(user, comp):
                print(f"computer: {option[comp]}")
                print(f"user: {option[user]}")

                result = user - comp    
                if result == 0:
                    print("Tie")
                elif result in (1, -2):
                    print("You Win")
                elif result in (-1, 2):
                    print("You lose")

            comparison(user, comp)
            break
        else:
            print("***Please enter a valid number: 0, 1, or 2.***")
        
    except ValueError:
        print("***Please enter a valid number: 0, 1, or 2.***")


# s(2), w(1), g(0)
# W = 1, -2
# L = -1, 2
# T = 0