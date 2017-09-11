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

# Commented out, see line 57            
#~ results_dict = {}
#~ internal_results_dict = {}

for word_to_search_for in words_to_search_for:
    title = "\nAppearance of '" + word_to_search_for 
    title += "' as a percentage of total words in the document: "
    print(title)
    for filename in filenames:
        total_words = count_total_words(filename)
        total_subject_words = count_word(filename, word_to_search_for)
        # See if you can adjust line below right here to load in the data into
        # a dictionary (probably nested by words_to_search_for...note I have done this in v2) that you can 
        # then use to perform statistical analysis / predictive analysis
        # using r^2 and resultant line of best fit. Then pull in other word
        # counts to see if predictive model predicts size based on the selected
        # word.
        
        # Might also consider building a website that predicts how long it will
        # take you to read a given gutenberg book given the size of book as 
        # well as reading speed as predicted by a timer. 
        ratio = str((total_subject_words / total_words) * 100) + "%"
        print(filename + ": " + ratio)
    
    
## All stuff from here below is wrong, hence commented out. This is your next step...also see lines 32-34...maybe use OrderedDict?
        #~ internal_results_dict[filename] = ratio
    
    #~ results_dict[title] = internal_results_dict
        

#~ for key, value in results_dict.items():
    #~ print("\n" + key + "\n")
    #~ print(value)
