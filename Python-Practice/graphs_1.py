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

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph: 
    def __init__(self):
        self.vertices = {} #keys of verts in graph

    def add_vertex(self, vertex):
        # add new unconnected vert
        self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        if v_to in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("nonexistent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    # breath-first traversal
    ## BEST METHOD FOR FINDING SHORTEST PATH ##
    def bft_traverse(self, starting_vertex_id):
        q = Queue()
        visited = set()

        # initialize
        q.enqueue(starting_vertex_id)

        while q.size() > 0:
            v= q.dequeue()

            if v not in visited:
                print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)
            
    # depth-first traversal
    def dft_traverse(self, starting_vertex_id):
        s = Stack()
        visited = set()

        # initialize
        s.push(starting_vertex_id)

        while s.size() > 0:
            v= s.pop()

            if v not in visited:
                print(v)

                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


g = Graph()
g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)

g.add_edge(2, 1) # line by self: makes directed
g.add_edge(1, 2) # w/ line 20: makes undirected
g.add_edge(2, 3) 
g.add_edge(3, 4) 

print(g.vertices)
g.bft_traverse(1)
g.dft_traverse(1)
