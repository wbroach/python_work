favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
    
#~ for name in sorted(favorite_languages.keys()):
    #~ print(name.title() + ", thank you for taking the poll.")

print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print("\t" + language.title())
