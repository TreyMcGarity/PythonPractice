"""
Add up and print the sum of the all of the minimum elements of each inner array:
[[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
The expected output is given by:
4 + -1 + 9 + -56 + 201 + 18 = 175
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. 
Run through the UPER problem solving framework while going through your thought process.
"""
array = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# smallest_numbers list
smallest_numbers = []
# result integer
result = 0

# traverse main list
for i in array:
    # check if element is list
    if type(i) == list:
        # if list has 1 element
        if len(i) == 1:
            # add element to smallest_numbers
            smallest_numbers.append(i[0])
            # prevents fall through and messing with indices
            continue
        for a in range(len(i) - 1):
            # save first element
            smallest = i[a]
            # check if next element is smaller
            if i[a] > i[a + 1]:
                # replace that element as smaller
                smallest = i[a + 1]
        # add smallest to smallest_numbers
        smallest_numbers.append(smallest)
    # otherwise, add lone element to smallest_numbers
    else:
        smallest_numbers.append(i)

# traverse smallest_numbers list
for x in smallest_numbers:    
    # add element until end
    result += x

# print result
print(result)