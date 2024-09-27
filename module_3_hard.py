data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    sum = 0
    new_list = []

    for element in data_structure:
        for j in element:
            new_list.append(j)
        if isinstance(element, dict):
            for i in element.values():
                new_list.append(i)

    while True:
        for element in new_list:
            if isinstance(element, int) or isinstance(element, str):
                continue
            else:
                for j in element:
                    new_list.append(j)
                if isinstance(element, dict):
                    for i in element.values():
                        new_list.append(i)
        break

    for k in new_list:
        if isinstance(k, int):
            sum += k

        if isinstance(k, str):
            sum += len(k)

    return sum


result = calculate_structure_sum(data_structure)
print(result)
