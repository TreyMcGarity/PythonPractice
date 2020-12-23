####  LeetCode Problems  ####
from time import time

start_stamp = time()
"""
1) Given an array of integers nums and and integer target, 
return the indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
"""
def twoSum(nums, target):
    """
    :type: List[int]
    :type: int
    :rtype: List[int]
    """
    # FIRST SOLUTION: two passes
    # traverse through nums list
    # for i in range(len(nums)):
    #     # at each position traverse rest of nums list after current
    #     for j in range(i + 1, len(nums)):
    #         # print(nums[i], nums[j])
    #         # if the sum of values at i and j equal target value
    #         if (nums[i] + nums[j]) == target:
    #             # return indexes of those values in a list
    #             return [i, j]
    ## OPTIMIZED SOLUTION 
    M = {}
    for i in range(len(nums)):
        curr = nums[i]
        if curr in M:
            return [M.get(curr), i]
        M[target-curr] = i
    """
    LeetCode Summary of Solution: "O(n^2)"
    Runtime: 5164 ms, faster than 13.92% of Python online submissions for Two Sum.
    Memory Usage: 13.7 MB, less than 61.82% of Python online submissions for Two Sum.
    """
# TEST CASES
data1 = [2, 7, 11, 15]
# unsorted values
data2 = [3, 2, 4]
# duplicated value
data3 = [2, 5, 5, 11]
# print(twoSum(data1, 26))
# print(twoSum(data2, 6))
# print(twoSum(data3, 10))

"""
2) Given a "signed" integer number, reverse digits of number.
"""
def reverse(num):
    """
    :type: iumt
    :rtype: int
    """
    ## FIRST SOLUTION ##
    # # turn int into string
    # num_str = str(num)
    # # split string into list or array of separate strings
    # digits = list(num_str) # original comprehension: digits = [digit for digit in num_str]
    # # variable to hold negative sign
    # sign = ""
    # # if first element is a "-"
    # if digits[0] == "-":
    #     # save first element
    #     sign = digits[0]
    #     # remove from list or array
    # digits.pop(0)
    # # reverse list of digits
    # digits.reverse()
    # # insert negative to front of list or array
    # digits.insert(0, sign)
    # # make list of digits into one string 
    # num_str = "".join(digits)
    # # turn string into int
    # result = int(num_str)
    # # if reversed number out of bounds, don't return
    # if result > pow(2,31) or result < pow(-2,31):
    #     return 0
    # # return reversed number
    # return result
    string = str(num)
    
    if string[0] == '-':
        return int('-'+string[:0:-1])
    else:
        return int(string[::-1])

data_num1 = 102
data_num2 = -102
# print(reverse(data_num1))
# print(reverse(data_num2))


"""
Find the factorial of a given number.
// Brute Force Solution
"""
def find_factorial(number): # O(n)
    """
    type: int/float
    rtype: int/float
    """
    result = 1
    for n in range(number, 0, -1):
        result *= n
    return result

# print(find_factorial(5)) # 120

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.
// The overall run time complexity should be O(log (m+n))
"""
nums1 = [1, 3]
nums2 = [2, 7]

def findMedianSortedArrays(nums1, nums2):
    """
    type: List[int]
    type: List[int]
    rtype: float
    """
    median = 0.0
    nums1.extend(nums2)
    for i in nums1:
        median += i
    median /= len(nums1)
    return median

# print(findMedianSortedArrays(nums1, nums2))
"""
quick ex. of map
"""
def turnArrintoInt(arr1, arr2):
    return "".join(map(str, arr))

# print(turnArrintoInt(nums1))

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"
"""
Find the are length of all the words in a given sentence, not counting punctuation
"""
def avg_len_words(sentence):
    # take out punctuation
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    # get all words separate
    words = sentence.split()
    # take the sum of all the words lengths
    # divide by the number of words in the array
    # round out by the hundredths place
    return round(sum(len(word) for word in words)/len(words),2)
    
# print(avg_len_words(sentence1))
# print(avg_len_words(sentence2))

"""
Add two strings representing numbers. Sum should be a string.
"""
num1 = '364'
num2 = '1836'

def add_strings(num1,num2):
    return str(int(num1) + int(num2))
            
# print(add_strings(num1,num2))

"""
quick ex. of eval
"""
def evaluate(equation):
    return eval(equation)

# print(evaluate("8 ** 2"))

"""
Given a string, find the first non-repeating character in it and return its index. 
If it doesn't exist, return -1.
Different case of word doesn't make it a different character 
"""
def first_unique_char(word):
    # make sure letters are lowercase (same)
    word.lower()
    # dic keys = char, and values = count of char
    letters = {}
    for char in word:
        # if char not already seen
        if char not in letters:
            # add it to dic
            letters[char] = 1
        else:
            # increment count of char
            letters[char] += 1
    # traverse through possible letters
    for i in range(len(word)):
        # first one reach with 1 occurrence
        if letters[word[i]] == 1:
            # return that letter
            return i
    # none are unique
    return -1

# print(first_unique_char("alphabet"))
# print(first_unique_char("barbados"))
# print(first_unique_char("crunchy"))

def shortest_substring():
    s = "ac"
    arr = [i for i in s]
    rev_arr = [i for i in arr[::-1]]
    palindrom = []
    for i, v in enumerate(arr):
        if v == rev_arr[i]:
            palindrom.append(v)
    if palindrom == []:
        palindrom.append(arr[0])
    # print(palindrom)
    pass

"""

"""
def make_palindrom():
    pass

print(make_palindrom())

def validParetheses():
    arr = []
    validmap = {'(':')', '{':'}', '[':']'}
        
    #traverse through input
    for p in s:
        # if open sign is found
        if p in validmap.keys():
            # append the sign to the array
            arr.append(p)
        #if there is an array and p is in validmap
        elif arr and p == validmap[arr.pop()]:
            continue
        # otherwise return false
        else:
            return False
    return arr == []



# to get time elapsed printed:
end_stamp = time()
elapsed = end_stamp - start_stamp
print("time lapsed:", elapsed)