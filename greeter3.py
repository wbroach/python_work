def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
    
while True:
    print("\nPlease tell me your name (enter 'q' at any time to quit) ")
    
    f_name = input('First name: ')
    if f_name.lower() == 'q':
        break
        
    l_name = input('Last name: ')
    if l_name.lower() == 'q':
        break
        
    greeting_name = get_formatted_name(f_name, l_name)
    print("Hello, " + greeting_name + "!")
