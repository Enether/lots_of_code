# 1056 - 1065
# 50102 - 50120
# 10987652 - 1256789

el = input()

left_ptr = float('inf')
right_ptr = len(el) - 1

curr_right_ptr = len(el) - 1
"""
Basically, find the bigger left index we can swap to create a smaller number
i.e 10982 - we want to find out that 0 and 2 are the numbers to swap, i.e 1 and 4
    10561 - we want to find out that 5 and 6 are the numbers to swap, i.e idx 2 and 3
"""
while curr_right_ptr > 0:
    curr_element = int(el[curr_right_ptr])
    curr_left_ptr = -1

    for i in reversed(range(0, curr_right_ptr)):
        if int(el[i]) < curr_element:
            curr_left_ptr = i
            break

    if curr_left_ptr != -1 and left_ptr < curr_left_ptr:
        left_ptr = curr_left_ptr
        right_ptr = curr_right_ptr

    curr_right_ptr -= 1

if left_ptr == float('-inf'):
    print(-1)
    exit()
el = list(el)
el[right_ptr], el[left_ptr] = el[left_ptr], el[right_ptr]
print(''.join(el[:left_ptr + 1] + sorted(el[left_ptr + 1:])))