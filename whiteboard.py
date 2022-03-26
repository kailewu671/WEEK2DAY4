# You must implement a function that return the difference between the biggest and the smallest value in a list(lst) received as parameter.

# The list(lst) contains integers, that means it may contain some negative numbers.

# The list will always have a minimum of 2 elements

# The list(lst) is not sorted

# max_diff([1, 2, 3, 4]) # return 3, because 4 - 1 == 3
# max_diff([1, 2, 3, -4]) # return 7, because 3 - (-4) == 7

def max_diff(nums):
    min(nums)
    max(nums)
    x = max(nums)- min(nums)
    return x 
print(max_diff([2,7,4,9])) 