# Gavin Doan
# Created: 10/8/25
# Last Edited: 10/22/25
# Description: Sorting Algorithms(Allows use to choose preferred sorting choice)

# Imports needed for the code to work
import os  # Import needed for text clear
import random  # Import needed for random number generator
import inquirer3  # Import needed for the menu to look nice
from bubble_sort import bubble_sort1  # Import needed for Bubble Sort
from insertion_sort import insertion_sort1  # Import needed for Insertion Sort
from selection_sort import selection_sort1  # Import needed for Selection Sort


# Function to allow user to selection the range and min/max input of list
def integer_input(context):
    valid = True
    while valid:
        try:
            entry = int(input(context))
            if entry == int(entry):
                valid = False
                return entry
            # else:
            #     print("! ERROR. Please enter a numeric value")
        except:
            print("! ERROR. Please enter a numeric value")


def range_input(context):
    valid = True
    while valid:
        try:
            entry = int(input(context))
            if entry > 0:
                valid = False
                return entry
            else:
                print("! ERROR. Please enter a Positive value")
        except:
            print("! ERROR. Please enter a numeric value")


def main():
    while True:

        # Code for the menu
        questions = [
            inquirer3.List('menu',
                           message="What would you like to do?",
                           choices=['Exit', 'Use Bubble Sort', 'Use Insertion Sort', 'Use Selection Sort'])
        ]
        answers = inquirer3.prompt(questions)
        select = "{}".format(answers['menu'])
        # Code for what the user selects
        match select:
            case "Exit":  # If User selects Exit
                exit()
            case "Use Bubble Sort":  # If User selects Bubble Sort
                # Inputs to allow the user to select min number
                min_num = integer_input("Minimum number for random list: ")
                # Inputs to allow user to select max number
                max_num = integer_input("Maximum number for random list: ")
                # Input to allow user to select length of the list
                list_length = range_input("Length of random list: ")
                if min_num <= max_num:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Code to generate list
                    numbers = [random.randint(min_num, max_num) for i in range(list_length)]
                    # Print to show user the unsorted list
                    # Calling on the Bubble Sort Function to sort the list
                    bubble_sort1(numbers)
                else:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERROR! Please make sure Minimum value is less than Maximum value\n")
            case "Use Insertion Sort":  # If User selects Insertion Sort
                # Inputs to allow the user to select min number
                min_num = integer_input("Minimum number for random list: ")
                # Inputs to allow user to select max number
                max_num = integer_input("Maximum number for random list: ")
                # Input to allow user to select length of the list
                list_length = range_input("Length of random list: ")
                if min_num <= max_num:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Code to generate list
                    numbers = [random.randint(min_num, max_num) for i in range(list_length)]
                    # Calling on the Bubble Sort Function to sort the list
                    insertion_sort1(numbers)
                else:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERROR! Please make sure minimum value is less than Maximum\n")
            case "Use Selection Sort":  # If User selects Selection Sort
                # Inputs to allow the user to select min number
                min_num = integer_input("Minimum number for random list: ")
                # Inputs to allow user to select max number
                max_num = integer_input("Maximum number for random list: ")
                # Input to allow user to select length of the list
                list_length = range_input("Length of random list: ")
                if min_num <= max_num:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    # Code to generate list
                    numbers = [random.randint(min_num, max_num) for i in range(list_length)]
                    # Calling on the Bubble Sort Function to sort the list
                    selection_sort1(numbers)
                else:
                    # To clear old text above
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nERROR! Please make sure minimum value is less than Maximum\n")


if __name__ == "__main__":
    main()
