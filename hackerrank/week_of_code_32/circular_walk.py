
def fill_r_array(r: list, g, seed, p):
    for i in range(1, len(r)):
        r[i] = (r[i-1]*g + seed) % p

n, start_point, end_point = [int(p) for p in input().split()]
if start_point == end_point:
    print(0)
    exit()

zero_val, g, seed, p = [int(p) for p in input().split()]
r = [0 for _ in range(n)]
r[0] = zero_val
fill_r_array(r, g, seed, p)
if r[start_point] == 0:
    print(-1)
    exit()
if abs(end_point-start_point) <= r[start_point]:
    print(1)
    exit()
# print(r)
# print(len(r))
best_sec = float('inf')

# key: integer - the index we've visited
# value: integer - the second at which we've visited this key

best_visited = {

}

if zero_val > p-1:
    raise Exception("TANK")

# if r[start_point] == p-1:
#     # We're at the best possible point
#     pass
# else:
#     # check if we can reach end point in one swoop
#     if abs(end_point-start_point) <= r[start_point]:
#         # we can reach at once
#         print(1)
#         exit()
#
#     # go to the max value :)
max_element = max(r[1:p])




# print(seconds)
found_first = False
found_second = False
best_path = float('inf')
## TRY TO REACH IN TWO STEPS
for i in range(start_point - r[start_point], (start_point + r[start_point]) + 1):
    i %= len(r)
    if i == start_point:
        continue
    if i == end_point:
        best_path=1
    if abs(i - end_point) <= r[i] or (len(r) - i) + end_point <= r[i]:
        best_path = 2
        print(2)
        exit()
## TRY TO REACH IN TWO STEPS
def traverse(r, curr_point, end_point, second, finding_first=True):
    global best_sec, max_element, found_first, found_second, best_path
    if found_first and finding_first:
        return
    elif not finding_first and found_second:
        return

    curr_point %= len(r)
    if abs(curr_point-end_point) <= r[curr_point] or (len(r)-curr_point) + end_point <= r[curr_point]:
        # print(f'FOUND BadfadfEST PATH FOR {second+1}')

        if second + 1 < best_path:
            best_path = second + 1
        if found_first:
            found_second = True
        found_first = True
        return
    if curr_point in best_visited:
        # if we've visited the key at a second equal or greater to the current one, there is no need to recurse, since at best, we'll get the same result
        if second >= best_visited[curr_point]:
            return
        else:
            best_visited[curr_point] = second
        pass
    else:
        # print(curr_point)
        best_visited[curr_point] = second

    if curr_point == end_point:
        if second < best_sec:
            best_sec = second
        return
    poss_jumppoint = r[curr_point]
    if poss_jumppoint == 0:
        return
    max_vals = []
    for i in range(curr_point-poss_jumppoint, (curr_point+poss_jumppoint)+1):
        i %= len(r)
        if i == curr_point:
            continue
        if i == end_point:
            # print(f'FOUND BEST PATH FOR {second+1}')

            if second+1 < best_path:
                best_path = second+1
            if found_first:
                found_second = True
            found_first = True
            return
        max_vals.append((r[i%len(r)], i%len(r)))
    best_pos, best_poss = list(reversed(sorted(max_vals, key=lambda x: x[0])))[:2]
    # print(best_pos, best_poss)
    traverse(r, best_pos[1], end_point, second+1, finding_first)
    traverse(r, best_poss[1], end_point, second+1, finding_first)

max_vals = []
for i in range(start_point-r[start_point], (start_point+r[start_point])+1):
    max_vals.append((r[i], i))
best_pos, best_poss = list(reversed(sorted(max_vals, key=lambda x: x[0])))[:2]
traverse(r, best_pos[1], end_point, 1)
traverse(r, best_poss[1], end_point, 1, False)
if best_path == float('inf'):
    print(-1)
else:
    print(best_path)
# traverse(r, start_point, end_point, 0)
# if end_point in best_visited:
#     print(best_visited[end_point])
# else:
#     print(-1)
# if best_sec == float('inf'):
#     print(-1)
# else:
#     print(best_visited[end_point])
    # print(best_sec)
