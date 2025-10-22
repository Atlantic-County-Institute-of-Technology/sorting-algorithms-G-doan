# Code for the Selection Sort Function

import time  # Import to add time for the user to know how long it will take to sort list
import os


def selection_sort1(numbers):
    original_numbers = str(numbers)
    # To clear old text above
    os.system('cls' if os.name == 'nt' else 'clear')
    # Variables for loop count and Sorting Actions
    lc = 0
    sc = 0
    # Variable to get the start time
    time_start = time.time()
    for i in range(len(numbers)):
        # To +1 every time it loops
        lc = lc + 1
        # Code to fine the smallest number in unsorted list
        min_idx = i
        for j in range(i + 1, len(numbers)):
            # To +1 every time it loops
            lc = lc + 1
            # To check and make the min index the smallest number if j is smaller
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        # Code to swap the smallest element with the first element
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        # To +1 every time a sorting action occurs
        sc = sc + 1
    # Variable to get the end time
    time_end = time.time()
    # Variable to get the time it takes to run
    elapsed_time = time_end - time_start
    # code to print the un/sorted list, and time taken for user
    print(f"Unsorted List: {original_numbers}")
    print(f"Selection Sorted List: {numbers}\n")
    print(f"Time taken: {elapsed_time:.2f}s")
    # Print the number of sorting actions and loops executed
    print(f"Loop Count: {lc}\n"
          f"Sorting Actions: {sc}\n")
    return numbers
