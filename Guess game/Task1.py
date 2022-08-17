

#Number Guessing Game in Python,

#UNI COMPILER INTERN.................................

import random
import math

x = random.randint(0, 100)
score = 100
print("\t\t I have a number is my mind .Can You Guess It?")
print("\n")



#calculate......................................................
multiples = [ x*3, x*5,x*7]
greater = x+10
less = x-10
if x>1:
    for i in range(2, int(x/2)+1):
        if (x % i) == 0:
            prime = "It is not a prime number"
            break
        else:
            prime = "It is a prime number"

factors=[]
def get_factors(x):
    factors.clear()
    for i in range(1, int(x/2)):
       if x % i == 0:
        factors.append(i)
    if x>10:
        factors.remove(1)



#def hint.........................................................
def clue1():
    print("\n")
    print("Multiples of number are :", multiples)

def clue2():
    print("\n")
    print("Number is greater than :", less)
    
def clue3():
    print("\n")
    print("Number is less than :", greater)
    
def clue4():
    print("\n")
    print(prime)
    
    
def clue5():
    print("\n")
    if prime == "It is not a prime number":
        get_factors(x)
        print("Its some factors are:", factors)
        



def show_clue(x, i, y):

    if x!=y and i ==1:
        clue1()

    if x!=y and i ==2:
        clue2()

    if x!=y and i ==3:
        clue3()
        
    if x!=y and i ==4:
        clue4()
        
    if x!=y and i ==5:
        clue5()


# condition.............................................................................
for i in range(5):
    print("Guess It Number", i + 1,"Chance.")
    if i > 0 and i < 4:
        show_clue(x, i, y)
    try:
        y = int(input("Enter a number:- "))
    except ValueError:
        print("The input was not a valid integer.")
    
    if x == y:

        print("* Congrats you did it in ", i + 1, "*")
        print("Your score is:", score)
        print("Thanks for playing!")
        break

    if x > y+20:

        print("You guessed too small!")
        score -=10

    if x < y-20:

        print("You Guessed too high!")
        score -=10
        
    if x>y and x < y+10:
            print("You guessed very close! Just a little bit higher!")
            score -= 10
            
    if x<y and x > y-10:
            print("You guessed very close! Just a little bit lower!")
            score -= 10
        
if y!=x:    
    print("Oopps Wrong Number!Only 5 Chance. The number was ", x)

    print("Good Luck Next Time")

    print("Your score is:", score)

    print("Thanks for playing!")
    



        
