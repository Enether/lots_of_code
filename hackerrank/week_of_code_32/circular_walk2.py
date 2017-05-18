

def fill_r_array(r: list, g, seed, p):
    for i in range(1, len(r)):
        r[i] = (r[i-1]*g + seed) % p
def get_min_steps(s):
    global r
    for i in range(len(r)):
        if dp[i] == float('inf'):
            start = j - r[i]
            end = j + r[i]
            for i in range(start, end+1):
                if i < 0:
                    s_new = n + i
                else:
                    if i >= n:
                        s_new = i % n
                    else:
                        s_new = i
                # s_new = i % n
                if dp[s_new] != float('inf'):
                    dp[i] = min(1+dp[s_new], dp[i])
    if dp[s] == float('inf'):
        get_min_steps(s)

n, s, t = [int(p) for p in input().split()]
if s == t:
    print(0)
    exit()

zero_val, g, seed, p = [int(p) for p in input().split()]
r = [0 for _ in range(n)]
r[0] = zero_val
fill_r_array(r, g, seed, p)
if r[s] == 0:
    print(-1)
    exit()
if abs(t-s) <= r[s]:
    print(1)
    exit()

dp = [0 for _ in range(n)]
for j in range(n):
    start = j - r[s]
    end = j + r[s]
    dp[j] = float('inf')
    for i in range(start, end+1):
        s_new = n%i
        if s_new == t:
            dp[j] = 1
    dp[t] = 0
    if dp[s] == float('inf'):
        get_min_steps(s)
    if dp[s] == float('inf'):
        print(-1)
    else:
        print(dp[s])
