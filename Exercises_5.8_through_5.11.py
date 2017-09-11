usernames = ['admin', 'tom', 'dick', 'harry', 'steve']
del usernames[:]
    
if len(usernames) == 0:
    print("We need to find some users!")
else:
    for username in usernames:
        if username == 'admin':
            print("Hello " + username.title() + ", " + "would you like to see a status report?")
        else:
            print("Hello " + username.title() + ", " + "thank you for logging in again.")


### EXERCISE 5-10
current_users = ['admin', 'tom', 'RICH', 'harry', 'steve']
new_users = ['jerry', 'kramer', 'rich', 'batman', 'Steve']

# creates a list comprehension to make comparison case insensitive
comparison_list = [current_user.lower() for current_user in current_users]

#~ #ALTERNATE: use a for loop to create a case-insensitive comparison list for new users
#~ for current_user in current_users:
    #~ comparison_list.append(current_user.lower())
    
for new_user in new_users:
    if new_user.lower() in comparison_list:
        print("I'm sorry, you will need to enter a new username")
    else:
        print("This username is available.")

## EXERCISE 5-11
ordinals = [value for value in range(1,10)]

for ordinal in ordinals:
    if ordinal == 1:
        print(str(ordinal) + "st")
    elif ordinal == 2:
        print(str(ordinal) + "nd")
    elif ordinal == 3:
        print(str(ordinal) + "rd")
    elif ordinal >= 4:
        print(str(ordinal) + "th")


