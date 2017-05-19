import math

input()
word = input()

import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True
def get_indices(word, wanted_letter):
    b_indices = []
    for idx, lt in enumerate(word):
        if lt == wanted_letter:
            if wanted_letter == 'c':
                if is_prime(idx):
                    b_indices.append(idx)
                # else:
                #     print(f'{idx} IS NOT PRIME')
            else:
                b_indices.append(idx)
    return b_indices

count = 0

def find_b_and_c(b_idc, c_idc, a_indices):
    global count
    a_indices = set(a_indices)

    for b_idx in b_idc:
        for c_idx in c_idc:
            a_idx = (-c_idx + b_idx ** 2 + 2 * b_idx) / (c_idx + 1)
            # print(c_idx)
            if int(a_idx) != a_idx:
                continue
            if a_idx in a_indices:
                count += 1
                # print(c_idx, a_idx)

def find_b_and_a(a_indices, b_indices, c_indices):
    global count
    c_indices = set(c_indices)
    for b_idx in b_indices:
        for a_idx in reversed(a_indices):
            c_idx = (-a_idx + b_idx**2 + 2*b_idx) / (a_idx+1)
            # print(c_idx)
            if int(c_idx) != c_idx:
                continue
            if c_idx >= len(word):
                # print('BREACK')
                # print(a_idx, b_idx)
                # return
                break
            # print(c_idx)
            if c_idx in c_indices:
                count += 1
        # print('########################3')

def find_a_and_c(a_indices, b_indices, c_indices):
    global count
    b_indices = set(b_indices)
    for a_idx in a_indices:
        for c_idx in c_indices:
            new_idx = (a_idx+1) * (c_idx+1)
            j = math.sqrt(new_idx)
            root = math.sqrt(new_idx)
            if int(root + 0.5) ** 2 == new_idx:
                new_idx = int(root)-1
                # if new_idx >= len(word):
                #     break
                if new_idx in b_indices:
                    count+=1

a_indices = get_indices(word, 'a')
b_indices = get_indices(word, 'b')

c_indices = set(get_indices(word, 'c'))
if len(b_indices) == 0 or len(c_indices) == 0 or len(a_indices) == 0:
    print(0)
    exit()
lengz = {}
lengz[len(a_indices)] = ['a']
if len(b_indices) not in lengz:
    lengz[len(b_indices)] = ['b']
else:
    lengz[len(b_indices)].append('b')
if len(c_indices) not in lengz:
    lengz[len(c_indices)] = ['c']
else:
    lengz[len(c_indices)].append('c')
lengths = sorted([len(a_indices), len(b_indices), len(c_indices)])
min_len, sec_min_len = lengths[0], lengths[1]
if min_len == sec_min_len:
    first, sec = lengz[min_len][0], lengz[sec_min_len][1]
    words = [first, sec]
else:
    first, sec = lengz[min_len][0], lengz[sec_min_len][0]
    words = [first, sec]
if 'a' in words:
    if 'b' in words:
        # A AND B
        # print('A AND B')
        find_b_and_a(a_indices, b_indices, c_indices)
        pass
    else:
        # A AND C
        find_a_and_c(a_indices, b_indices, c_indices)
        pass
else:
    # B AND C
    find_b_and_c(b_indices, c_indices, a_indices)

print(count)