def chocolate_feast():
    print('please provide three integers followed by a type of chocolate, separated by commas and spaces (ex. 6, 2, 2, sugar free):')
    response = input()
    cash = int(response.split(', ')[0])
    price = int(response.split(', ')[1])
    wrappers_needed = int(response.split(', ')[2])
    type = response.split(', ')[3]

    choc_dict = {
        'milk': 0,
        'dark': 0,
        'white': 0,
        'sugar free': 0
    }

    wrappers_available = {
        'milk': 0,
        'dark': 0,
        'white': 0,
        'sugar free': 0
    }

    initial_purchase = cash / price
    choc_dict[type] = initial_purchase
    wrappers_available[type] = initial_purchase

    def most_wrappers():
        max_value = max(wrappers_available.values())
        most_wrappers = [
            k for k, v in wrappers_available.items() if v == max_value]
        return most_wrappers

    while wrappers_available[type] >= wrappers_needed:
        choc_dict[type] += wrappers_available[type] // wrappers_needed
        wrappers_available[type] = wrappers_available[type] % wrappers_needed
        wrappers_available[type] += 1
        if type == 'milk' or type == 'white':
            choc_dict['sugar free'] += 1
            wrappers_available['sugar free'] += 1
        if type == 'sugar free':
            choc_dict['dark'] += 1
            wrappers_available['dark'] += 1
        if wrappers_available[type] < wrappers_needed:
            type = most_wrappers()[0]

    final_list = []
    for key, value in choc_dict.items():
        final_list.append(f'{key} {str(value)[0]}')

    answer = ', '.join(final_list)
    print(answer)


chocolate_feast()
