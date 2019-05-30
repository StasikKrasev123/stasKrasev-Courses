list_to_filter = [1, 2, 3, 'a', 'b']
filtered_list = []

for el in list_to_filter:
    if isinstance(el, int):
        filtered_list.append(el)
