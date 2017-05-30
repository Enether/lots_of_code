n, m = [int(p) for p in input().split()]
graph = {nd: [] for nd in range(1, n+1)}
for _ in range(m):
    a, b = [int(p) for p in input().split()]
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
vis_time = {key: None for key in graph.keys()}
low_time = {key: None for key in graph.keys()}
parents = {key: None for key in graph.keys()}



# start_node = 3
time = 0
articulation_points = []


def dfs_ap(node, vis_time, low_time, parents, visited, articulation_points):
    """
    Linear time recursive algorithm
    :param node: The current node
    :param vis_time: A dictionary holding the visited (time of discovery) for each node
    :param low_time: A dictionary holding the low_time for each node
    :param parents: A dictionary holding the parent of each node
    :param visited: A set holding all the nodes we've traversed through
    :param articulation_points: A list of all the currently found articulation points
    """
    global time
    is_articulation_point = False
    vis_time[node] = time
    low_time[node] = time
    visited.add(node)
    real_children_count = 0
    for child in graph[node]:
        if parents[node] == child:  # We're trying to visit the node we came from
            continue

        if child not in visited:
            real_children_count += 1
            parents[child] = node
            time += 1
            dfs_ap(child, vis_time, low_time, parents, visited, articulation_points)
            if parents[node] is not None and low_time[child] >= vis_time[node]:
                is_articulation_point = True
            low_time[node] = min(low_time[node], low_time[child])
        else:
            low_time[node] = min(low_time[node], vis_time[child])

    if is_articulation_point or (parents[node] is None and real_children_count >= 2):
        articulation_points.append(node)
# calculate articulation points

visited = set()
for node in range(1, n+1):
    if node not in visited:
        time = 0
        visited.add(node)
        dfs_ap(node, vis_time, low_time, parents, visited, articulation_points)
articulation_points = set(articulation_points)

query_count = int(input())
for _ in range(query_count):
    curr_q = int(input())
    if curr_q in articulation_points:
        print('Satisfied {}'.format(len(graph[curr_q])))
    else:
        print('Not Satisfied')