##  DAY 1  ##
"""
What has tables solve:

- faster searching.
- caching data (network caching)
- indexing
- handling duplicates (removing, detecting, counting)

characterisitcs:
- doesn't matter value of n
- can be resized to handle any size of input data
"""

# 0 1 1 2 3 5 8 13 21 34 55
# fib(0): 0
# fib(1): 1
# fib(n): fib(n-1) + fib(n-2)

cache = {} # needs to be outside

def fib(n):
    if n <= 1: return n

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)
   
    return cache[n]

for i in range(100):
    print(f'{i:3} {fib(i)}')

# some solutions require additional params
# def foo(a, x, b):
#     cache[(a,x,b)] == ...

#################################################

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2
}

items = list(d.items())

# Sort by key

items.sort()

for i in items:
	print(f'{i[0]}: {i[1]}')


print()

# Sort by value

"""
def sort_by(t):
	#print(f'sort_by({repr(t)}) called!')
	return t[1]
​
items.sort(key=sort_by)
​
# ^^ same as lambda vv
"""

items.sort(key=lambda t: t[1])

for i in items:
	print(f'{i[0]}: {i[1]}')

#################################################

#plain text: HELLOWORLD
#Ciphertext: DOGGEBUEGW
encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

def encode(s):
    r = ""
    
    for c in s:
        r += encode_table[c]
    
    return r

decode_table = {}

for k, v in encode_table.items():
    decode_table[v] = k

def decode(s):
    r= ""

    for c in s:
        r += decode_table[c]

    return r

print(encode("HELLOWORLD"))
print(decode("DOGGEBEUGW"))

#################################################

def letter_count(s):
    d = {}

    for c in s:
        if not c.isalpha():
            continue
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        #or if no d[c]= 0
        #   no else, always increment

    return d

print(letter_count("aaaaabracadabraccccccdada"))

#################################################

import hashlib
import random

def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:], 16) & 0xffffffff

def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()

            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision, ({tries / buckets * 100}% full)")

how_many_before_collision(32768, 10)

#################################################

def pod(total, podcasts):
    podcast_len = {}

    for p in podcasts:
        podcast_len[p] = True

    """
    # Set version equivalent to dict, above
    podcast_len = set()

    for p in podcasts:
        podcast_len.add(p)
    """

    for p0 in podcasts:
        other_podcast_len = total - p0
        # is there a podcast of total - p0 minutes?
        if other_podcast_len in podcast_len:
            return True

    return False


"""
total == 60
p0 == 27
p1 == 60 - 27 == total - p0 == 33
"""

##  DAY 2  ##
