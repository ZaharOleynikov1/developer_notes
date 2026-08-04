# Binary search. Exercise 1.1

def binary_search(list_n, item):
    low = 0
    height = len(list_n) - 1

    while low <= height:
        mid = (low + height) // 2
        guess = list_n[mid]
        if mid == guess:
            return guess
        if mid < guess:
            height = mid + 1
        else:
            low = mid + 1

    return None

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

binary_search(list_of_numbers, 3)