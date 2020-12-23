"""
Find median of 2 sorted arrays

1) what is return type? float
"""
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

# Ex. median(arr1, arr2) = 3.5

def median(arr1, arr2):
    arr1.extend(arr2)
    arr1.sort()
    total = 0
    for value in arr1:
        total += value
    median = total // len(arr1)
    return median

print(median(arr1, arr2)) # 3 need to be float