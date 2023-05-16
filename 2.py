# Write your solution for algorithm 2 below
import random # To test with random number


def sort_lst(num):
    sorted_lst = sorted(num) # Sort the list in ascending order using the sorted() method 
    return sorted_lst # Return the sorted list

# unsorted_lst = [random.randint(-999, 999) for _ in range(10)]
unsorted_lst = [1, 5, 2, 601, 7, 57, 16, 87, 99, 27, 62, 4]
print(f"unsorted List: {unsorted_lst}")
sorted_lst = sort_lst(unsorted_lst)
print(f"sorted List: {sorted_lst}")