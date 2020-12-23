import time

start_time = time.time()

#initial list and target for search and sorts
data = [8, 5, 3, 2, 10, 7, 1, 6, 9, 4]
target = 8

#linear search O(n) //determined by size of list
def linear_search(data, target):
    # traverse through the whole list
    for i in range(len(data)):
        # if current value is target, True
        if data[i] == target:
            return True
    # if loop through whole list and no match, False
    return False

# print(linear_search(data, target))

#Iterative Binary Search
def iterative_binary_search(data, target):
    # low value is index 0 and high is index of end
    low = 0
    high = len(data) - 1

    while low <= high:
        # middle of list is low + high divided by two
        mid = (low + high) // 2
        print("\n",low, "low\n", mid, "mid\n", high, "high")
        # if target is middle value, it's True
        if target == data[mid]:
            print("equals")
            return True
        # if target is less than middle value 
        elif target < data[mid]:
            print("less than")
            # set index of high to index of middle - 1
            high = mid - 1
        # if neither
        else:
            print("greater")
            # set index of low to index of middle + 1
            low = mid + 1
    return False
"""
INDEXES:
 0 low  START OF LOOP
 4 mid
 9 high

 5 low
 7 mid
 9 high

 8 low
 8 mid
 9 high

 9 low   END OF LOOP
 9 mid
 9 high

 10 low  OUT OF LOOP
 9 mid
 9 high
False
"""
# print(iterative_binary_search(data, target))

#Recursive Binary Search
def recursive_binary_search(data, target, low, high):
    # low value is index 0 and high is index of end
    if low > high:
        return False
    else:
        # middle of list is low + high divided by two
        mid = (low + high) // 2
        # if target is middle value, it's True
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # go to top of function at new index values
            return recursive_binary_search(data, target, low , mid - 1)
        else:
            # go to top of function at new index values
            return recursive_binary_search(data, target, mid + 1 , high)

# print(recursive_binary_search(data, target, 0, len(data) - 1))

end_time = time.time()
# print (f"runtime: {end_time - start_time} seconds")