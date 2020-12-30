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

def third_side(side1, side2):
    side3 = pow(side1, 2) + pow(side2, 2)
    result = int(math.sqrt(side3))
    return result

print(third_side(3,4))


"""
find 3rd angle given 2 angles
"""

def third_angle(angle1, angle2):
    angle3 = 180 - angle1 - angle2
    return angle3

print(third_angle(90, 60)) 

