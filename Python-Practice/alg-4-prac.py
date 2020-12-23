"""
Given a sorted array of distinct non-negative, find the smallest missing element in it.
"""
data = [0, 1, 3, 6, 9, 11, 15]

def sm_mess_up(arr):
    if arr[0] != 0:
        return 0
    if arr[-1] == len(arr) -1:
        return len(arr)

    # because already sorted, binary search type method works O(log n)
    # if not sorted use linear method O(n)
    # don't try to sort then search because not worth extra work O(n log n)
    start = 0
    end = len(arr) - 1

    while start < end:
        mid = (start + end) // 2

        if arr[mid] == mid:
            start = mid + 1
        else:
            end = mid
    return start 

print("index of smallest missing element:", sm_mess_up(data))


def product_of_all_other_numbers(arr):
    temp = 1
    prod = [1 for i in range(len(arr))] 
    
    # traverse through and elements on left side excluding arr[i]  
    for i in range(len(arr)):
        prod[i] = temp 
        temp *= arr[i]
  
    temp = 1
  
    # elements on right side excluding arr[i]  
    for i in range(len(arr)-1, -1, -1):
        prod[i] *= temp 
        temp *= arr[i]

    return prod

print(product_of_all_other_numbers([4,2,3]))