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