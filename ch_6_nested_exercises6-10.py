favorite_numbers = {
    'julia': [7, 12, 72],
    'will': [9, 3, 14],
    'nancy': [19, 16, 6],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + ":")
    
    for number_list in numbers:
        print(number_list)
