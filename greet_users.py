def greet_users(usernames):
    for name in usernames:
        print("Hello, " + name.title() + "!")
        
users = ['matthew', 'mark', 'luke', 'john']
greet_users(users)
