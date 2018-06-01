input()
word = input()
used_combinations = set()
used_letters = set()

best_len = 0
for idx, char_1 in enumerate(word):
    if char_1 in used_letters:
        continue
    leftover_arr = word[idx+1:]
    if len(leftover_arr) == 1:
        leftover_arr += ''
    for idx_2, char_2 in enumerate(leftover_arr):
        curr_len = 0
        if char_2 == '':
            continue
        if char_1 == char_2:
            break
        if char_2 in used_letters:
            continue
        if (char_1, char_2) in used_combinations or char_1 == char_2:
            continue  # already used this combination
        used_combinations.add((char_1, char_2))
        used_combinations.add((char_2, char_1))
        curr_len += 2
        is_valid = True
        current_char = char_1
        other_char = char_2

        leftover_arr_2 = leftover_arr[idx_2+1:]
        if len(leftover_arr_2) == 1:
            leftover_arr_2 += ''
        for char_3 in leftover_arr_2:
            if char_3 == '':
                continue
            if char_3 == other_char:
                is_valid = False
                break
            elif char_3 == current_char:
                curr_len += 1
                current_char, other_char = other_char, current_char

        if is_valid and curr_len > best_len:
            best_len = curr_len

    used_letters.add(char_1)
print(best_len)
