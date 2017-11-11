"""
Given a string, determine in O(N) time the index of the one character you need to remove for the string to become a palindrome
"""
a = 'akbba'
a = 'abbka'
a = 'abbak'
a = 'kabba'
a = 'abbbzba'
a = 'abzbbba'

# 1. Reverse the string
reversed_a = ''.join(reversed(a))

# 2. Compare indices, once you get something different, that's it

def find_difference(a, reversed_a):
    idx_to_find = None
    for idx in range(len(a)):
        if a[idx] != reversed_a[idx]:
            idx_to_find = idx
            break
            # return idx, a[idx]
    # find which of it is
    idx_a, idx_b = idx_to_find, len(a) - idx_to_find - 1
    old_a = a
    a = a[:idx_a] + a[idx_a+1:]
    if a == ''.join(reversed(a)):
        return idx_a, old_a[idx_a]
    else:
        print(idx_b)
        return idx_b, old_a[idx_b]

print(find_difference(a, reversed_a))