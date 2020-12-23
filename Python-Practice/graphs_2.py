"""
Given two words (begin_word and end_word), and a dictionary's word list, return
the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not
a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
"""
words = set()

with open("./words.txt") as f:
    for w in f:
        w = w.strip()
        words.add(w)

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

def get_neighbors(word):
    neighbors = []

    for w in words:
        if len(w) == len(words):
            diff_count = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1:
                neighbors.append(w)

def bfs(start, end):
    q = Queue()
    visited = set()
    q.enqueue([start])

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v in visited:
            visited.add(v)
            if v == end:
                return path
            for neighbor in self.get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
    return None


print(bfs("hit", "cog"))