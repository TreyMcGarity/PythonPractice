####CodingBat Problems####

"""
You are driving a little too fast, and a police officer stops you.
Write code to compute the result, encoded as an int value: 0=no ticket, 
1=small ticket, 2=big ticket. 

If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2.

Unless it is your birthday -- on that day, your 
speed can be 5 higher in all cases.
"""

def caught_speeding(speed, is_birthday):
  """
  Thought Process:
    func(Two params) (two inputs) first=int, second=boolean
    If birthday <= 85 and > 80 return 1
    If speed > 80 return 2
    If birthday <= 65 and > 60 return 0
    If speed > 60 return 1
    Else return 0
  """
  if speed > 80:
    if is_birthday == False:
      return 2
    elif is_birthday == True and speed > 85:
      return 2
    elif is_birthday == True and speed <= 85:
      return 1
  elif speed > 60:
    if is_birthday == False:
      return 1
    elif is_birthday == True and speed > 65:
      return 1
    else:
      return 0
  else:
    return 0

# print(caught_speeding(86, True))


"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
"""
def sorta_sum(a, b):
  """
  Thought Process:

  Proof:

  """
  x = a + b
  if x in list(range(10, 20)): 
    return 20
  else:
    return x
# print(sorta_sum(6, 1))
# print(sorta_sum(6, 4))


"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
"""
def date_fashion(you, other):
  """
  Thought Process:

  
  Proof:

  """
  if you >= 8 or other >= 8:
    return 2
  if you <= 2 or other <= 2:
    return 0
  else:
    return 1

# print(date_fashion(4, 6))

"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
"""
def near_ten(num):
  """
  Thought Process:
  1) take num mod by 10
  2) if value 0,1,2 or 8,9 return True
  3) else return False
  
  Proof:
  1) 12%10 = 2 (pass)
  2) 19%10 = 9 (pass)
  3) 17%10 = 3 (fail)
  """
  if num % 10 <= 2:
    return True
  elif num % 10 >= 8 and num % 10 <= 9:
    return True
  else:
    return False

# print(near_ten(-9))

"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
"""
def in1to10(n, outside_mode):
  """
  Thought Process:
  1)check first input value and second input value
  2)if first is 1-10 and second is false return true
  3)if first is not 1-10 and second is false return false
  4)if first is 1-10 and second is true return false
  5)if first is not 1-10 and second is true return true
  
  Proof:
  1) (5, false) = true
  2) (15, false) = false
  3) (5, true) = false
  4) (15, true) = true
  """
  if outside_mode == False:
    if n >= 1 and n <= 10:
      return True
    else:
      return False
  elif outside_mode == True:
    if n > 1 and n < 10:
      return False
    else:
      return True
  
# print(in1to10(5, False))
# print(in1to10(15, False))
# print(in1to10(5, True))
# print(in1to10(15, True))

"""
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
"""
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

# print(first_last6([1, 2, 6]))
# print(first_last6([6, 1, 2, 3]))
# print(first_last6([13, 6, 1, 2, 3]))

"""
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
"""
def same_first_last(nums):
  """
  Thought Process:
  length is 0 return false
  length is 1 first is last return true
  check nums[0] and nums[-1] are equal
  """
  if len(nums) == 0:
    return False
  if nums[0] == nums[-1]:
    return True
  else:
    return False

# print(same_first_last([])) #False
# print(same_first_last([1, 2, 3])) #False
# print(same_first_last([1, 2, 3, 1])) #True
# print(same_first_last([1, 2, 1])) #True
