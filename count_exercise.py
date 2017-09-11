def count_word(filename, word):
    """ Returns how many times a given word appears in a given file."""
    try:
        with open(filename) as file_object:
            contents = file_object.read()
            word_count = contents.lower().count(word) 
    except FileNotFoundError:
        print(filename + " cannot be located.")
    else:
        return word_count
        
def count_total_words(filename):
    """ Returns how many words are in a given file."""
    try:
        with open(filename) as file_object:
            string = file_object.read()
    except FileNotFoundError:
        print(filename + " cannot be located.")
    else:
        list = string.split()
        total_word_count = len(list)
        return total_word_count
        
words_to_search_for = ['the', 'and', 'who', 'what', 'when', 'where', 'why']
# See if you can find a way to pull in text files from a given folder, or even
# better, see if you can DL them from gutenburg website and load them into 
# this list.
filenames = ['text_files\siddhartha.txt', 'text_files\little_women.txt',
            'text_files\\alice.txt', 'text_files\moby_dick.txt',
            ]

for word_to_search_for in words_to_search_for:
    title = "Appearance of '" + word_to_search_for 
    title += "' as a percentage of total words in the document: "
    print(title)
    for filename in filenames:
        total_words = count_total_words(filename)
        total_subject_words = count_word(filename, word_to_search_for)
        # See if you can adjust line below right here to load in the data into
        # a dictionary (probably nested by words_to_search_for) that you can 
        # then use to perform statistical analysis / predictive analysis
        # using r^2 and resultant line of best fit. Then pull in other word
        # counts to see if predictive model predicts size based on the selected
        # word.
        ratio = str((total_subject_words / total_words) * 100) + "%"
        print(filename + ": " + ratio)
    
