favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#~ # To loop key-value pairs
#~ for name, language in favorite_languages.items():
    #~ print(name.title() + "'s favorite language is " + language.title() + ".")

#~ # print keys only. Remember key is the default:
#~ for name in favorite_languages.keys():
    #~ print(name.title())

friends = ['phil', 'sarah', 'erin']
for name in favorite_languages.keys():
    
    if name in friends:
        print("Hi " + name.title() +
        ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")
    
for friend in friends:
    if friend not in favorite_languages.keys():
        print(friend.title() + ", please take our poll!")
