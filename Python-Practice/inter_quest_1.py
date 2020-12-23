"""
Print out each element of the following array on a separate line, but 
this time the input array can contain arrays nested to an arbitrarily 
deep level:

['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 
0, ['{slice, owned}'], 22]

For the above input, the expected output is:

Bob
Slack
reddit
89
101
alacritty
(brackets)
5
375
0
{slice, owned}
22

You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code.
Run through the UPER problem solving framework while going through your thought process. 

Thought Process:
1) Loop through List
2) If element is a List. Loop through it
3) Print value of each element observed
"""
sample = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# for a in sample:
#     if type(a) == list:
#         for b in a:
#             if type(b) == list:
#                 for c in b:
#                     print(c)
#             else:
#                 print(b)
#     else:
#         print(a)

#recursive function
def looping(sample):
    for i in sample:
        if type(i) == list:
            for x in i:
                print(x)
        else:
            print(i)
        looping()

looping(sample)