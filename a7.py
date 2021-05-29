"""
File: a7.py
Assignment 7

"""

from stack import Stack

def isPalindrome(sentence):
    """Returns True if sentence is a palindrome or False otherwise."""
    stk = Stack() #Creates a stack called stk.
        #Write your code here
    sentence = sentence.casefold() #created to change characters to lowercase if suitable
    sentence = sentence.replace(" ", "") #remove in between spaces
    for i in range (len(sentence)):
        stk.push(sentence[i])
    for i in range (stk.size()):
        if sentence[i] != stk.pop():
            return False
        return True
    Console.WriteLine(sentence);

    # *** Do not modify main() ***
def main():
    while True:
        sentence = input("Enter some text or just hit Enter to quit: ")
        if sentence == "":
            break
        elif isPalindrome(sentence):
            print("It's a palindrome.")
        else:
            print("It's not a palindrome.")
main()
