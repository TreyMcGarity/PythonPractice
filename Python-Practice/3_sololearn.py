import math

#print reverse string
string = "hello world"
def reverse_string(text):
    return text[::-1]
    
print(reverse_string(string))

def averageLength(text):
    cleanup  = string.translate({ord(i): None for i in ".,;!?"})
    count = 0
    words = cleanup.split()

    for word in words:
        for letters in word:
            count += 1

    return math.ceil(count / len(words))

# print(averageLength(string))

def countTinyPairs(a, b, k):
    # a goes left to right
    # b goes right to left
    # compare sum of elems at position to k
    # if sum less than k, increment pair count
    checking = 0
    count = 0
    first = 0
    second = 0
    
    while checking < len(a):
        for i in range(0, len(a), 1):
            first = a[i]
        for i in range(len(b) -1 , -1, -1):
            first = b[i]
        pair = str(first) + str(second)
        print(pair)
        if int(pair) < k:
            count += 1
        
    return count

# print(countTinyPairs([1, 2, 3], [1, 2, 3], 31))


"""
find third side length of triangle given 2 sides
"""

def pythagorean_theorem(side1, side2):
    side3 = pow(side1, 2) + pow(side2, 2)
    result = int(math.sqrt(side3))
    return result

# print(pythagorean_theorem(3,4))


"""
find 3rd angle given 2 angles
"""

def third_angle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    return angle3

# print(third_angle(90, 60)) 

"""
Law of Sines

2 angles and 1 side opposite to a given angle to solve for other side of other angle  

a / sin(A) = b / sin(B) = c / sin(C)
"""

def law_of_sine(angle1, angle2, side1):
    return side1/math.sin(math.radians(angle1)) * math.sin(math.radians(angle2))
    

# print(law_of_sine(90, 60, 5))

"""
Law of Cosine

2 sides and an angle to a given side to solve for missing side of given angle

c= sqrt[a^2+b^2﹣2abcos(C)]
"""

def law_of_cosine(side1, side2, angle1):
    return math.sqrt((math.pow(side1, 2)) * (math.pow(side2, 2)) - 2 * side1 * side2 * math.cos(angle1))
    

"""
Solving a Triangle given angle B and C and side b

find angle A and sides a and c
"""
B = 35
C = 105
b = 7

c = law_of_sine(B, C, b)
a = pythagorean_theorem(b, c)
A = third_angle(B, C)


print("given B =", B,"C =", C, "and b =", b,
    "\nA =", A, "a =", a, "c =", c)
