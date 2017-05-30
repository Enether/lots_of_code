"""

10 9
2 1
3 1
4 3
5 2
6 1
7 2
8 6
9 8
10 8
"""
from collections import deque

n, m = [int(p) for p in input().split()]
root = 1
tree = {node: [] for node in range(1, n+1)}
children_count = {node: 0 for node in range(1, n+1)}
parents = {node: None for node in range(1, n+1)}

# build the graph
for _ in range(m):
    a, b = [int(p) for p in input().split()]
    tree[a].append(b)
    tree[b].append(a)

"""
We basically want to figure out how many children each node has.
This is done easily through a double loop starting from the root node.
At each iteration, we know one level more how many children each one has, starting at the lowest level with leafs
e.g
1st iteration
children_count(1) = count of his direct children + the sum of the children_count for each of his direct children.
    Since this is the first loop and all the children_count() for 2 and 3 are unitialized, his children are 2
          1  (2 children)
        /   \
(1child)2    3 (1 child)
       /      \
   (0)1        1 (0 child)
2nd iteration
    children_count for 2 and 3 are initialized, so 1 is again = count of his children + sum of children's children_count
          1  (4 children)
        /   \
(1child)2    3 (1 child)
       /      \
   (0)1        1 (0 child)
"""

for _ in range(n+1):
    # BFS to get the count of children for each node
    children = deque()
    for ch in tree[root]:
        parents[ch] = root
        children.append(ch)

    children_count[root] = len(tree[root]) + sum([children_count[nd] for nd in tree[root]])
    visited = {root}
    while len(children) > 0:
        curr_node = children.popleft()
        visited.add(curr_node)
        # calculate the current node's children count
        children_count[curr_node] = (len([nd for nd in tree[curr_node] if nd not in visited])
                                     + sum([children_count[nd] for nd in tree[curr_node] if nd not in visited]))

        for ch in tree[curr_node]:
            if ch not in visited:
                parents[ch] = curr_node
                children.append(ch)


cuts = 0
visited = set()

"""
After we have the children count for each node, it is really simple.
Whenever we encounted a child with an uneven number of children, we can easily cut him off, knowing
    that that component now has an even number of elements.
If not, we simply don't cut him off.
We always go recursively deeper to figure out if we can make more cuts until we reach teh leafs
"""


def cut_tree(curr_node):
    global cuts
    visited.add(curr_node)
    for child in tree[curr_node]:
        if child not in visited:
            # if the child has an uneven number of children, we can cut him off directly.
            if children_count[child] % 2 != 0:
                cut_tree(child)  # try to cut more recursively
                cuts += 1
            else:
                cut_tree(child)

cut_tree(root)
print(cuts)
