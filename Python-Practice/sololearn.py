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

print(averageLength(string))