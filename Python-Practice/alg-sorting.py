data = [4, 2, 8, 7, 1, 9, 5, 3, 6]

# Selection Sort
def selection_sort(data):
    length = range(len(data))
    # traverse through list from first to second from last
    for i in length:
        # set current value in traverse to minimum 
        min_value = i
        # j is value to right of current value
        for j in range(i, len(data)):
            # if value is smaller than minimum value
            if data[j] < data[min_value]:
                # set value to new minimum
                min_value = j
        # save current value
        temp = data[i]
        # switch current and mininmum values
        data[i] = data[min_value]
        data[min_value] = temp
    return data
"""
[8, 5, 3, 2, 10, 7, 1, 6, 9, 4] ORIGINAL
[1, 5, 3, 2, 10, 7, 8, 6, 9, 4]
[1, 2, 3, 5, 10, 7, 8, 6, 9, 4]
[1, 2, 3, 5, 10, 7, 8, 6, 9, 4]
[1, 2, 3, 4, 10, 7, 8, 6, 9, 5]
[1, 2, 3, 4, 5, 7, 8, 6, 9, 10]
[1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] SORTED
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] END OF LOOP
"""
# print(selection_sort(data))

# Bubble Sort
def bubbleSort(data): 
    length = len(data)
  
    # traverse through list 
    for i in range(length):   
        # Last i elements are already in place 
        for j in range(0, length-1): 
            # if the value is greater than right value
            if data[j] > data[j+1]:
                #save current value
                temp = data[j]
                # switch current and right of current
                data[j] = data[j+1]
                data[j+1] = temp 
    return data

# print(bubbleSort(data))

#Quick Sort
def partition(arr):
    #get pivot
    pivot = arr[0]
    left = []
    right = []

    #separates values in array based on
    for x in arr[1:]:
        # if value is less than
        if x <= pivot:
            # go to LHS
            left.append(x)
        # or greater than
        else: 
            # go to RHS
            right.append(x)
    return left, pivot, right

def quick_sort(arr):
    # if array of self return self
    if len(arr) <= 1:
        return arr
    # otherwise, call partition on array to organize it
    # into individual parts
    left, pivot, right = partition(arr)

    # concatenates pieces together
    # while running quicksort on LHS and RHS
    return quick_sort(left) + [pivot] + quick_sort(right)
        
# print(quick_sort(data))

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    print("pre ", merged_arr)

    a = 0 # index arrA
    b = 0 # index arrB
    i = 0 # incrementing index

    # while both indexes are less than length of corresponding arrays
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            print(" arrA",arrA,"\n","arrB",arrB)
            # a is smaller, its value should be added next
            merged_arr[i] = arrA[a]
            # increment arrA's index
            a += 1
        else:
            # b is smaller, its value should be added next
            merged_arr[i] = arrB[b]
            # increment arrB's index
            b += 1
        i += 1

    # while indexes are less than individual arrs
    while a < len(arrA):
        # set value at in LHS at index a to merged array at index i
        merged_arr[i] = arrA[a]
        # increment to accommodate more than one value insertion
        a += 1
        i += 1
    # continues process same as LHS but with RHS
    while b < len(arrB):
        # set value at in RHS at index a to merged array at index i
        merged_arr[i] = arrB[b]
        # increment to accommodate more than one value insertion
        b += 1
        i += 1 
    print(a,b,i)
    print("post", merged_arr, "\n")
    return merged_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # reducing down by half until each list has 1 sorted item
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # recursive dividing on the subarrays until each only has 1 element remaining
    left = merge_sort(left)
    right = merge_sort(right)
    # compare/merge the 1 sorted item in each subarray
    arr = merge(left, right)

    return arr
"""
[4, 2, 8, 7, 1, 9, 5, 3, 6]     ORIGINAL

mid: 4          INDEX OF MIDDLE  
[4, 2, 8, 7]    LHS FROM ORIGINAL   
mid: 2          MID OF LHS
[4, 2]          LHS(2)
mid: 1          MID OF LHS AGAIN
[4]             LHS(3)
[2]             RHS
 arrA [4]
 arrB [2]

        MERGE A AND B MAKES NEW LHS
 merg [2, 4]
 ---------------------
[8, 7]          RHS FROM INDEX OF MID
mid: 1          MID OF RHS
[8]             LHS
[7]             RHS
 arrA [8]       
 arrB [7]

        MERGE A AND B MAKES NEW RHS
 merg [7, 8]
 ---------------------
 arrA [2, 4]
 arrB [7, 8]

    MERGED NEW LHS AND NEW RHS TO FINAL LHS
 merg [2, 4, 7, 8]
___________________________________________

[1, 9, 5, 3, 6] RHS FROM ORIGINAL
mid: 2          MID OF RHS
[1, 9]          LHS
mid: 1          MID OF LHS
[1]             LHS(2)
[9]             RHS
 arrA [1]
 arrB [9]

        MERGE A AND B MAKES NEW LHS
 merg [1, 9]

[5, 3, 6]       RHS FORM MID 
mid: 1          MID OF RHS
[5]             LHS
[3, 6]          RHS
mid: 1          MID OF RHS
[3]             LHS(2)
[6]             RHS(2)
 arrA [3]
 arrB [6]

        MERGE A AND B MAKES NEW B
 merg [3, 6]
  ---------------------
 arrA [5]
 arrB [3, 6]

        MERGE LHS AND RHS MAKES NEW RHS
 merg [3, 5, 6]

        MERGE arrA AND arrB
 arrA [1, 9]
 arrB [3, 5, 6]

    MERGED NEW LHS AND NEW RHS TO FINAL RHS
 merg [1, 3, 5, 6, 9]
___________________________________________

 arrA [2, 4, 7, 8]
 arrB [1, 3, 5, 6, 9]

    MERGED FINAL LHS AND FINAL RHS TO MAKE FINAL MERGED
 merg [1, 2, 3, 4, 5, 6, 7, 8, 9]

[1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
print(merge_sort(data))