current_users = ['matthew', 'MARK', 'LUKE', 'john', 'jesus']
new_users = ['Peter', 'Paul', 'MARK', 'John', 'dave']
comp_list = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in comp_list:
        print("I'm sorry, but you will need to enter a new user name.")
    else:
        print("This username is available.")
        
