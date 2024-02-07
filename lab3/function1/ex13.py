import random 
def guess_the_number():
    b=random.randint(1,20)
    a=input("Hello! What is your name? \n")
    print("Well," ,a,", I am thinking of a number between 1 and 20.")
    s="Take a guess. \n"
    s1="Your guess is too low. \nTake a guess. \n"
    s2="Your guess is too high. \nTake a guess. \n"
    g=int(input(s))
    t=1
    while(b!=g):
        if g<b:
            g=int(input(s1))
            t=t+1
        elif g>b:
            g=int(input(s2))
            t=t+1
    print("Good job, ",a,"! You guessed my number in " ,t, "guesses!")
        
guess_the_number()