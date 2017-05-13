a, b, c = [int(p) for p in input().split()]
_ = input()
arr = [int(p) for p in input().split()]
mp = {}
summ = 0
for i, num in enumerate(arr):
    if num not in mp:
        mp[num] = 0
    mp[num] += 1
    if num > b and num < c:
        summ += 1
print(summ)


