from DFS import UndirectedGraph, DFSTimeCounter

# create the graph from problem 1A.
g = UndirectedGraph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 4)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Test DFS visit
discovery_times = [None] * 5
finish_times = [None] * 5
dfs_tree_parents = [None] * 5
dfs_back_edges = []
g.dfs_visit(0, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges)

print('DFS visit discovery and finish times given by your code.')
print('Node\t Discovery\t Finish')
for i in range(5):
    print(f'{i} \t\t {discovery_times[i]}\t\t {finish_times[i]}')

assert (discovery_times[0] == 0), f'Fail: Node 0 expected discovery time must be 0'
assert (discovery_times[1] == 1), f'Fail: Node 1 expected discovery is 1'
assert (finish_times[
            1] == 2), f'Fail: Node 1 finish time expected value is 2 (are you incrementing counter before you return from dfs_visit function and before recording finish times)'
assert (discovery_times[2] == 3), f'Fail: Node 2 expected discovery is 3'
assert (finish_times[2] == 8), f'Fail: Node 2 finish time expected value is 8'
assert (discovery_times[3] == 4), f'Fail: Node 3 discovery time expected value is 4'
assert (finish_times[3] == 7), f'Fail: Node 3 finish time expected value is 7'
assert (discovery_times[4] == 5), f'Fail: Node 4 discovery time expected value is 5'
assert (finish_times[4] == 6), f'Fail: Node 4 finish time expected value is 6'

print('Success -- discovery and finish times seem correct.')
print()

print('Node\t DFS-Tree-Parent')
for i in range(5):
    print(f'{i} \t {dfs_tree_parents[i]}')

assert (dfs_tree_parents[0] == None), 'Fail: node 0 cannot have a parent (must be root)'
assert (dfs_tree_parents[1] == 0), 'Fail: node 1 parent must be 0'
assert (dfs_tree_parents[2] == 0), 'Fail: node 2 parent must be 0'
assert (dfs_tree_parents[3] == 2), 'Fail: node 3 parent must be 2'
assert (dfs_tree_parents[4] == 3), 'Fail: node 4 parent must be 3'

print('Success-- DFS parents are set correctly.')

print()
# Filter out all trivial back eddges (i,j)  where j is simply the parent of i.
# such back edges occur because we are treating an undirected edge as two directed edges
# in either direction.
non_trivial_back_edges = [(i, j) for (i, j) in dfs_back_edges if dfs_tree_parents[i] != j]
print('Back edges are')
for (i, j) in non_trivial_back_edges:
    print(f'{(i, j)}')

assert len(
    non_trivial_back_edges) == 2, f'Fail: There must be 2 non trivial back edges -- your code reports {len(non_trivial_back_edges)}. Note that (4,0) and (4,2) are the only non trivial backedges'
assert (4, 2) in non_trivial_back_edges, '(4,2) must be a backedge that is non trivial'
assert (4, 0) in non_trivial_back_edges, '(4,3) must be a non-trivial backedges'

print('Success -- 15 points!')
