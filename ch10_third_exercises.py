## Exercise 10-6 and 10-7 below:  

#~ print("Give me two numbers and I will add them for you.")
#~ print("Press 'q' at any time to exit.")

#~ while True:
    
    #~ first_number = input("First number: ")
    #~ if first_number.lower() == 'q':
        #~ break
    #~ second_number = input("Second number: ")
    #~ if second_number.lower() == 'q':
        #~ break
    
    #~ try:
        #~ total = int(first_number) + int(second_number)
    #~ except ValueError:
        #~ print("Please provide a numerical value.")
    #~ else:
        #~ print("The sum of these numbers is " + str(total) + ".")

#~ ## Exercises 10-8 and 10-9:
#~ def write_pet_name(filename, petnames = []):
    #~ """Writes the names provided in the argument petnames to a txt file"""
    #~ with open(filename, 'w') as file_object:
        #~ for petname in petnames:
            #~ file_object.write(str(petname).title()+ "\n")

#~ def print_pet_name(filename):
    #~ """Prints the name of the pets listed in the file"""
    #~ try:    
        #~ with open(filename) as file_object:
            #~ contents = file_object.read()
    #~ except FileNotFoundError:
        #~ print("This file is not available.")
        #~ pass
    #~ else:
        #~ print(contents)

#~ filename_cats = 'cats.txt'
#~ filename_dogs = 'dogs.txt'
#~ cat_names = ['simon', 'maine coon', 'bigger maine coon']
#~ dog_names = ['belle', 'callie', 'josie', 'hank']

#~ write_pet_name(filename_cats, cat_names)
#~ write_pet_name(filename_dogs, dog_names)
#~ print_pet_name(filename_cats)
#~ print_pet_name(filename_dogs)

## Exercise 10-10:

def count_word(filename, word):
    """ Determines how many times a given word appears in a given file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            word_count = contents.lower().count(word) 
    except FileNotFoundError:
        print(filename + " cannot be located.")
    else:
        message = filename + " has the word " + "'" + word + "' in it " 
        message += str(word_count) + " times."
        print(message)
        
word_to_search_for = 'the'
filenames = ['text_files\siddhartha.txt', 'text_files\little_women.txt',
            'text_files\\alice.txt', 'text_files\moby_dick.txt',
            ]

for filename in filenames:
    count_word(filename, word_to_search_for)













