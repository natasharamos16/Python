# Natasha Ramos-Gomez
# COP4538
# 2/2/2020

#creating main function
def main():
    #prompting user input to enter range of numbers
    userInput = int(input("Enter unique integers to be entered in ascending order: "))
    list = []

    while(userInput > 0):
        #prompting user to enter numbers
        n = int(input("Enter a number: "))
        list.append(n)
        userInput = userInput - 1
        
    #printing out the both functions in main
    print(magic_sequential(list))
    print(magic_binary(list))

#creating the functions
def magic_sequential(list):
    for i in range(len(list)):
        if(list[i] == i):
            return i
    return -1

def magic_binary(list):
    begin = 0
    finish = len(list) - 1

    while(begin < finish):
        midNum = int((begin + finish)/2)
        if(list[midNum] == midNum):
            return midNum
        elif(list[midNum] > midNum):
            finish = midNum
        else:
            begin = midNum + 1
    return -1

#invoking the main function
main()
