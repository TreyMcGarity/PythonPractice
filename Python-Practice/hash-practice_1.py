"""
Given a package with a weight limit "limit" and a list "weights" of item weights, 
implement a function "get_indices_of_item_weights" that finds two items whose sum 
of weights equals the weight limit "limit". Your function will return a tuple of 
integers that has the following form:

(zero, one)
where each element represents the item weights of the two packages. 

--The higher valued index should be placed in the zeroth index and the smaller 
index should be placed in the "first" index.--
If such a pair doesn’t exist for the given inputs, your function should return None.

--Your solution should run in linear time.--

Example:

input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

Hints:
What if we store each weight in the input list as keys? What would be a useful thing to 
store as the value for each key?
If we store each weight's list index as its value, we can then check to see if the hash 
table contains an entry for 
"limit" - "weight". If it does, then we've found the two items whose weights sum up to the limit!
"""

def get_indices_of_item_weights(weights, length, limit) :
    # initiaize a cache
    cache = {}
    # will be increment to make representing indexes
    index = 0
    # store weights as keys and indexes as values in cache
    for weight in weights:
        cache[weight] = index
        index += 1

    # traverse and stop at end of input array
    for i in range(length):
        # key to find solution case
        key = limit - weights[i]
        # check if a solution is possible
        if key in cache:
            # return values of solution
            return (cache[key], i)


print(get_indices_of_item_weights([9], 1, 9)) # None
print(get_indices_of_item_weights([4, 4], 2, 8)) # (1, 0)
print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)) # (3, 1)