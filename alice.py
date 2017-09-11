def count_words(filename):
    """Count the approximate number of words in a text file."""
    try: 
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        #~ print(filename + " cannot be located.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(filename + " has " + str(num_words) + " words in it.")
        
filenames = ['text_files\\alice.txt', 'text_files\\siddhartha.txt', 'text_files\\moby_dick.txt', 'little_women.txt']

for file_name in filenames:
    count_words(file_name)

