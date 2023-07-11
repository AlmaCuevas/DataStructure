# BFS. Modified DFS with Queue code.


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class BFSTimeCounter:
    def __init__(self):
        self.count = 0

    def reset(self):
        self.count = 0

    def increment(self):
        self.count = self.count + 1

    def get(self):
        return self.count


class UndirectedGraph:

    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [set() for i in range(self.n)]

    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)

    # get a set of all vertices that
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]

    # Function: bfs_visit

    def bfs_visit_children(self, i, bfs_timer, discovery_times, finish_times,
                  bfs_tree_parents, queue_to_visit):
        assert 0 <= i < self.n

        print(f"BFS for {i}")
        for j in self.adj_list[i]:
            if discovery_times[j] == None:  # Discovery of {j} doesn't exist, we'll look into its edges
                print(f"node origin i: {i}")
                print(f"edge to j: {j}")
                bfs_tree_parents[j] = i
                discovery_times[j] = bfs_timer.get()
                bfs_timer.increment()
                queue_to_visit.enqueue(j)
        finish_times[i] = bfs_timer.get()
        bfs_timer.increment()

    def bfs_visit(self, i, bfs_timer, discovery_times, finish_times,
                  bfs_tree_parents, queue_to_visit):
        queue_to_visit.enqueue(i)
        discovery_times[i] = bfs_timer.get()
        bfs_timer.increment()
        while queue_to_visit.size():
            self.bfs_visit_children(queue_to_visit.dequeue(), bfs_timer, discovery_times, finish_times,
                           bfs_tree_parents, queue_to_visit)


    # Function: bfs_traverse_graph
    # Traverse the entire graph.
    def bfs_traverse_graph(self):
        bfs_timer = BFSTimeCounter()
        discovery_times = [None] * self.n
        finish_times = [None] * self.n
        bfs_tree_parents = [None] * self.n
        queue_to_visit = Queue()
        for i in range(self.n):
            if discovery_times[i] == None:
                self.bfs_visit(i, bfs_timer, discovery_times, finish_times,
                               bfs_tree_parents, queue_to_visit)
        return (bfs_tree_parents, discovery_times, finish_times)
