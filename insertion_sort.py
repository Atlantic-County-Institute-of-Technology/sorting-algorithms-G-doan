# Code for Insertion Sort Function

import time  # Import to add time for the user to know how long it will take to sort list
import os


def insertion_sort1(numbers):
    original_numbers = str(numbers)
    # To clear old text above
    os.system('cls' if os.name == 'nt' else 'clear')
    # Variables for loop count and Sorting Actions
    lc = 0
    sc = 0
    # Variable to get the start time
    time_start = time.time()
    for i in range(1, len(numbers)):
        # To +1 every time it loops
        lc = lc + 1
        temp = numbers[i]  # Making the target element a temp to move to correct position
        j = i - 1  # Last element in sorted list
        # To move the numbers to the right one
        while j >= 0 and temp < numbers[j]:
            # To +1 every time it loops
            lc = lc + 1
            numbers[j + 1] = numbers[j]
            j = j - 1
        # Place the temp in correct sorted position
        numbers[j + 1] = temp
        # To +1 every time a sorting action occurs
        sc = sc + 1
    # Variable to get the end time
    time_end = time.time()
    # Variable to get the time it takes to run
    elapsed_time = time_end - time_start
    # Code to print the un/Sorted list and time taken for user
    print(f"Unsorted List: {original_numbers}")
    print(f"Insertion Sorted List: {numbers}\n")
    print(f"Time taken: {elapsed_time:.2f}s")
    # Print the number of sorting actions and loops executed
    print(f"Loop Count: {lc}\n"
          f"Sorting Actions: {sc}\n")
    return numbers
