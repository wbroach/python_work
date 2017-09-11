def get_formatted_name(first_name, last_name, middle_name = ''):
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()
    
musician_1 = get_formatted_name('jimi', 'hendrix')
musician_2 = get_formatted_name('john', middle_name = 'lee', last_name = 'hooker')
    
print(musician_1)
print(musician_2)
