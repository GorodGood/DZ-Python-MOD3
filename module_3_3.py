def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(1991, 'Gorod', False)
print_params(2024, "octemer" )
print_params(c = 178)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = (1991, 'Gorod178', False)
values_dict = {'a': 33, 'b': 'Ivan', 'c': True}

print_params (*values_list)
print_params (**values_dict)

values_list_2= [37.1, 'Figma']
print_params(*values_list_2, 42)