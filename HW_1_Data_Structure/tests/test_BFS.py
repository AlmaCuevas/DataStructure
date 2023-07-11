from BFS import UndirectedGraph, BFSTimeCounter, Queue

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 4)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test bfs visit
discovery_times = [None] * 5
finish_times = [None] * 5
bfs_tree_parents = [None] * 5
queue_to_visit = Queue()
g.bfs_visit(0, BFSTimeCounter(), discovery_times, finish_times, bfs_tree_parents, queue_to_visit)

print('BFS visit discovery and finish times given by your code.')
print('Node\t Discovery\t Finish')
for i in range(5):
    print(f'{i} \t\t {discovery_times[i]}\t\t {finish_times[i]}')

assert (discovery_times[0] == 0), f'Fail: Node 0 expected discovery time must be 0'
assert (discovery_times[1] == 1), f'Fail: Node 1 expected discovery is 1'
assert (finish_times[
            1] == 5), f'Fail: Node 1 finish time expected value is 5'
assert (discovery_times[2] == 2), f'Fail: Node 2 expected discovery is 2'
assert (finish_times[2] == 7), f'Fail: Node 2 finish time expected value is 7'
assert (discovery_times[3] == 6), f'Fail: Node 3 discovery time expected value is 6'
assert (finish_times[3] == 9), f'Fail: Node 3 finish time expected value is 8'
assert (discovery_times[4] == 3), f'Fail: Node 4 discovery time expected value is 4'
assert (finish_times[4] == 8), f'Fail: Node 4 finish time expected value is 8'

print('Success -- discovery and finish times seem correct.')
print()

print('Node\t BFS-Tree-Parent')
for i in range(5):
    print(f'{i} \t {bfs_tree_parents[i]}')

assert (bfs_tree_parents[0] == None), 'Fail: node 0 cannot have a parent (must be root)'
assert (bfs_tree_parents[1] == 0), 'Fail: node 1 parent must be 0'
assert (bfs_tree_parents[2] == 0), 'Fail: node 2 parent must be 0'
assert (bfs_tree_parents[3] == 2), 'Fail: node 3 parent must be 2'
assert (bfs_tree_parents[4] == 0), 'Fail: node 4 parent must be 0'

print('Success-- bfs parents are set correctly.')

print('Success -- 15 points!')
