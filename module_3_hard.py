def check_sum(data_structure):
    sum = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            sum += check_sum(key)
            sum += check_sum(value)
    # иначе - список,кортэж,множества
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            sum += check_sum(item)
            # иначе - целое число и число с плавающей запятой
    elif isinstance(data_structure, (int, float)):
        sum += data_structure
        # иначе  - функция len
    elif isinstance(data_structure, str):
        sum += len(data_structure)

    return sum

# Условия задачи
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = check_sum(data_structure)
print(result)