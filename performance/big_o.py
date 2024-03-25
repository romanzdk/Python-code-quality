import timeit

n = 1_000_000
repeats = 1000
element = str(n // 2)
new_element = str(n + 1)


##### ADD
setup_list = f'''
elements = [str(i) for i in range({n})]
new_element = "{new_element}"
element = "{element}"
'''

setup_set = f'''
elements = set([str(i) for i in range({n})])
new_element = "{new_element}"
element = "{element}"
'''

stmt_list = 'elements.append(new_element)'
stmt_set = 'elements.add(new_element)'

time_list_add = timeit.timeit(stmt_list, setup=setup_list, number=repeats)
print(f"List Add Operation Time: {time_list_add:.6f}s")

time_set_add = timeit.timeit(stmt_set, setup=setup_set, number=repeats)
print(f"Set Add Operation Time: {time_set_add:.6f}s")


#### REMOVE
print()
stmt = 'elements.remove(element) if element in elements else None'

time_list_remove = timeit.timeit(stmt, setup=setup_list, number=repeats)
print(f"List Remove: {time_list_remove:.6f}s")

time_set_remove = timeit.timeit(stmt, setup=setup_set, number=repeats)
print(f"Set Remove: {time_set_remove:.6f}s")


##### IN
print()
stmt = f'_ = element in elements'

time_list_in = timeit.timeit(stmt, setup=setup_list, number=repeats)
print(f"List In: {time_list_in:.6f}s")

time_set_in = timeit.timeit(stmt, setup=setup_set, number=repeats)
print(f"Set In: {time_set_in:.6f}s")