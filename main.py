import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
          guess = int(input(f'input your number between 1 and {x}: '))
          if guess < random_num:
            print("low number!!!!")
          elif guess > random_num:
            print("high number!!!!")   
    
    print("Great!!! The nunmber!!!!!")
# guess number between 1 and 10
guess(10)    