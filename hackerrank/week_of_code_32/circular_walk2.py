from collections import deque
def circ_walk(n, s, t, r_values):
    queue = deque()
    count = 0
    queue.append(s)
    visited = [False for _ in range(n)]
    added = [False for _ in range(n)]
    added[s] = True

    while queue:
        count += 1
        tmp = deque()
        while queue:
            p = queue.popleft()
            if not visited[p]:
                visited[p] = True
                start = p - r_values[p]
                end = p + r_values[p]
                for i in range(start, end+1):
                    s_new = i % n  # TODO: May not work ?
                    if s_new == t:
                        return count
                    if not visited[s_new] and not added[s_new]:
                        tmp.append(s_new)
                        added[s_new] = True
        queue = tmp
    return -1
n, s, t = [int(p) for p in input().split()]
r_0, g, seed, p = [int(p) for p in input().split()]

r_values = []
r_values.append(r_0)
for i in range(1, n):
    r_values.append((r_values[i-1]*g+seed)%p)
if r_values[0] == 0 and s != t:
    print(-1)
    exit()
if s == t:
    print(0)
    exit()
print(circ_walk(n, s, t, r_values))

"""
import java.util.*;

public class Solution {


	private static int circularWalk(int n, int s, int t, int[] r_values) {
		Queue<Integer> queue = new LinkedList<>();
		int count = 0;
		queue.add(s);
		boolean[] visited = new boolean[n];
		boolean[] added = new boolean[n]; //reduces the inner loops substantially -> makes the code O(n)
		added[s] = true;

					visited[p] = true;
					int start = p - r_values[p];
					int end = p + r_values[p];
					for (int i = start; i <= end; i++) {
						int s_new = i < 0 ? n + i : i >= n ? i % n : i;
						if (s_new == t) {
							return count;
						}
						if (!visited[s_new] && !added[s_new]) {
							tmp.add(s_new);
							added[s_new] = true;
						}
					}
				}
			}
			queue = tmp;
		}
		return  -1;
	}
}
"""