
pre_compute = {}
from datetime import datetime
st = datetime.now()
k = 0

def get_b_indices(word):
    b_indices = []
    for idx, lt in enumerate(word):
        if lt == 'b':
            b_indices.append(idx)
    return b_indices

count = 0
def b_force(word, wanted_num):
    global count
    indices=[]
    visited = set()
    for i in range(2,(wanted_num//2)+4):
        if i > len(word):
            break
        if wanted_num % i == 0:
            first_idx = i-1
            second_idx = (wanted_num//i)-1
            if second_idx >= len(word):
                continue
            if (first_idx, second_idx) not in visited and (second_idx, first_idx) not in visited:
                # print(first_idx, second_idx)
                if word[first_idx] == 'a' and word[second_idx] == 'c' or word[first_idx] == 'c' and word[second_idx] == 'a':
                    count += 1
                    visited.add((first_idx, second_idx))
                    visited.add((second_idx, first_idx))

input()
word = input()
b_indices = get_b_indices(word)

for b_idx in b_indices:
    wanted_num = (b_idx+1)*(b_idx+1)
    b_force(word, wanted_num)
print(count)