#Natasha Ramos-Gomez
#bs.py
#January 18, 2020

import random

def main():
    #A program is being created with ranges and lets the user guess
    #the computer's number until the guess is right

    smallerNum = int(input("Enter the smaller number in the range: "))#method used to input low number
    largerNum = int(input("Enter the larger number in the range: "))#method used to input high number 
    print ("Now think of a number between", smallerNum, "and", largerNum)#method tells user to think of a number
    print ("Hit enter to continue...")

    attempts = 0 #used to count how many tries the computer took
    guess = False #method used if guess is not correct

    print("I'm trying to guess your number. I know it is between", smallerNum, "and", largerNum)

    while smallerNum <= largerNum and not guess: #method used to go through a loop until correct number is found
        attempts = attempts + 1 #method used to add 1 to each attempt
        selNum = (largerNum + smallerNum) // 2 #calculating a value between the range
        print ('Is your number? ', selNum) #print statement used to ask user in guess is correct or not
        userAn = input('Enter =, <, or >:') #prompts user to make a choice is guess is <, > or =

        if userAn == '=': #method comfirms guess is correct
            print ("Hooray, I'v got it in", attempts, "tries!")
            guess = True
        elif userAn == '<': #method used to check if guess is too high
            largerNum = selNum - 1
        elif userAn == '>': #method used to check if guess is too low
            smallerNum = selNum + 1
#shows the entire main function
main()

    
    

        
        
        
    

    
    
