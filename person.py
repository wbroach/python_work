def build_person(first_name, last_name, age = ''):
    person_dict = {'first': first_name, 'last': last_name}
    if age:
        person_dict['age'] = age
    
    return person_dict
    
musician = build_person('jimi','hendrix',27)
print(musician)        
    
