#Natasha Ramos-Gomez
#a4.py
#Feburary 10, 2020


def main():
    userString = input("Enter a string: ")
    print("The string length for recursive is: " + str(count_recursive(userString)))
    print("The string length for iterative is: " + str(count_iterative(userString)))
def count_recursive(userString):
    if userString == '':
        return 0
    return 1 + count_recursive(userString[1:])

def count_iterative(userString):
    count = 0
    for n in userString:
        count = 1 + count
    return count

if __name__ == '__main__':
    main()
    

        
        
        
    

    
    
