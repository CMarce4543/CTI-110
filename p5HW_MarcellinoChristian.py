#Christian Marcellino
#4/20/24
#CTI-110
#P5HW
#Program will display menu, depending on user input program will calculate math, and provide responses based on input.

#This will display the greeting message to the user.

import random

def display_menu():
    print("Welcome to the Math Quiz!")
    print("Main Menu")
    print("-------------------------------")
    print("1. Addition Random Numbers.")
    print("2. Subtract Random Numbers.")
    print("3. Exit.")
          
#Calculations will start.
#User needs to input a number between 1 and 100.
#Program will add math equations. 

def add_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2
    print(f"{num1:>4}")
    print(f"+{num2:>3}\n")
    guesses = 0
    answer = '1'
    while answer != result:
        answer = int(input("Enter your answer: "))
        guesses += 1
        if answer == result:
            print(f"Congratulations!!! Your answer is correct. Number of guesses: {guesses}")
        elif answer < result:
            print("Sorry, guess is too low. Try again.")
        else:
            print("Sorry, guess is too high. Try again.")

#Program will start subtracting math problems.
                
def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1-num2
    print(f"{num1:>4}")
    print(f"-{num2:>3}\n")
    guesses = 0
    while True:
        user_answer = int(input("Enter the remainder of the subtraction: "))
        guesses += 1
        if user_answer == result:
            print(f"Congratulations! Your answer is correct. Number of guesses: {guesses}")
        elif user_answer < result:
            print("Sorry, guess is too low. Try again.")
        else:
            print("Sorry, guess is too high. Try again.")
            
            
#Main Menu options.

def main():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            add_random_numbers()
        elif choice == '2':
            subtract_random_numbers()
        elif choice == '3':
            print("Thank you for playing. Bye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
