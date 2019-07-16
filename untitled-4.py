import random

def main():
    randnum = random.randint(1,100)
    tries = 6
    
    while tries > 0:
        
        guess = int(input("Please guess a number: "))
    
        if (guess == randnum):
            print("Guess is correct!")
            break
        
        elif (guess>randnum):
            print("Guess is too big")
            tries = tries - 1
            
        elif (guess<randnum):
            print("Guess is too small")
            tries = tries - 1
    
if __name__ == "__main__":
    main()