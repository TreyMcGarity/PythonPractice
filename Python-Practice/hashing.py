table = [None] * 8

def hash(s):
    total = 0

    bytes = str(s).encode()

    for b in bytes:
        total += b

    return total

def get_index(s):
    value = hash(s)
    return value % len(table)

def put(key, value):
    index = get_index(key)
    table[index] = value

def get(key):
    index = get_index(key)
    value = table[index]
    
    return value

put("Trey", 626)

# print(hash("Trey"))
# print(hash("Yert")) # Makes a collision with Trey

print(table)