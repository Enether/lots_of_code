n, k, x = [int(p) for p in input().split()]
chores = [int(p) for p in input().split()]
time_it_took = 0
for chore in range(n):
    left_chore_count = n-chore
    if left_chore_count <= k and x < chores[chore]:
        time_it_took += x
    else:
        time_it_took += chores[chore]
print(time_it_took)
