"""
Grabs the precomputer numbers and prints out C++ code which builds separate vectors to one main vector.
 Done so, because some judges have a maximum length of a line limitation.
"""
from land_precomputer import numbers


def build_vector_init(vector_name, numbers) -> str:
    return f'std::vector<int> {vector_name} = {{ {", ".join(str(p) for p in numbers)} }};'


prev_idx = 0
idx = prev_idx + 2999
list_count = 0
PUSH_TO_MAIN_VECTOR_TEMPLATE = '''
for (int i = 0; i < {name}Length; i++) {{
    mainPart.push_back({name}[i]);
}}
'''
print('std::vector<int> mainPart;')
while idx <= len(numbers):
    vector_name = f'part{list_count}'

    print(build_vector_init(vector_name, numbers[prev_idx:idx]))
    print(f'int {vector_name}Length = {len(numbers[prev_idx:idx])};')
    print(PUSH_TO_MAIN_VECTOR_TEMPLATE.format(name=vector_name))

    list_count += 1
    prev_idx = idx
    idx = prev_idx + 2999

vector_name = f'part{list_count}'

print(build_vector_init(vector_name, numbers[prev_idx:]))
print(f'int {vector_name}Length = {len(numbers[prev_idx:idx])};')
print(PUSH_TO_MAIN_VECTOR_TEMPLATE.format(name=vector_name))
