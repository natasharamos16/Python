# Natasha Ramos-Gomez
# COP4538
# 1/28/2020

textFile = input("Enter the name of the file: ")

start = 0
while(start == 0):
    try:
        openFile = open(textFile, "r")
        start = 1
    except:
        print("The file named " + textFile + " could not be opened. Please try again!")
        textFile = input("Enter the name of the file: ")
        start = 0
counter = 0

for line in openFile:
    counter = counter + 1

print("The file contains " + str(counter) + " lines");

while True:
    try:
        userInput = int(input("Enter a number(0 to quit): "))
        startLine = 0
        break;
    except ValueError:
        print("Try Again. The number should be between 0 and 16")
while userInput != 0:
    if userInput >= 0 and userInput <= counter:
        openFile = open(textFile, "r")
        for line in openFile:
            startLine +=1
            if startLine == userInput:
                print(userInput, ":", line)

    else:
        print("Try Again. The number should be between 0 and 16")

    while True:
        try:
            userInput = int(input("Enter a number(0 to quit): "))
            startLine = 0
            break;
        except ValueError:
            print("Try Again. The number should be between 0 and 16")



#Updated
