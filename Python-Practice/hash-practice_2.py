"""
For an input list of integers, we wish to know which positive numbers have corresponding 
negative numbers in the list.

Example input:

[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]
Input can be in any order.

Example return value:

[ 1, 3, 4 ]
Because 1, 3, and 4 are the positive numbers that have corresponding negative 
numbers in the list.

Return value can be in any order.

Solve this problem with a hash table.

Limits:

The input list can contain approximately 5,000,000 elements.
"""

def has_negatives(a):
    # will be the list of both negatives and positives
    result = []
    # initialize cache 
    cache = {}

    # traverse through input list of number
    for num in a:
        # check if number is less than zero
        if num < 0: 
            # store value of num as negative 
            cache[-num] = num

    # traverse again
    for num in a:
         # check if a number is also in the cache (where the negatives are)
        if num in cache:
            # add number to result array
            result.append(num)

    return result

print(has_negatives([1,2,3])) # []
print(has_negatives([1,2,3,-4])) # []
print(has_negatives([-1,-2,1,2,3,4,-4])) # [1, 2, 4]