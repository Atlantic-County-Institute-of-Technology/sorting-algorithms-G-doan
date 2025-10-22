# Code for Bubble Sort Function

import time  # Import to add time for the user to know how long it will take to sort list
import os


def bubble_sort1(numbers):
    original_numbers = str(numbers)
    # To clear old text above
    os.system('cls' if os.name == 'nt' else 'clear')
    # Variables for loop count and Sorting Actions
    lc = 0
    sc = 0
    # Variable to get the start time
    time_start = time.time()
    # Code to sort the list
    for i in range(len(numbers) - 1):
        # To +1 every time it loops
        lc = lc + 1
        for j in range(len(numbers) - i - 1):
            # To +1 every time it loops
            lc = lc + 1
            if numbers[j] > numbers[j + 1]:
                # To +1 every time a sorting action occurs
                sc = sc + 1
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    # Variable to get the end time
    time_end = time.time()
    # Variable to get the time it takes to run
    elapsed_time = time_end - time_start
    # Code to print the Un/Sorted list and time take for the user
    print(f"Unsorted List: {original_numbers}")
    print(f"Bubble Sorted List: {numbers}\n")
    print(f"Time taken: {elapsed_time:.2f}s")
    # Print the number of sorting actions and loops executed
    print(f"Loop Count: {lc}\n"
          f"Sorting Actions: {sc}\n")
    return numbers
