poll_results = {}

poll_active = True

while poll_active:
    user_name = input("\nPlease enter your name: ")
    poll_response = input("What is your dream vacation? ")
    
    poll_results[user_name] = poll_response
    
# Allow while loop to turn off
    repeat = input("Would you like to let another person respond? (y/n) ")
    
    if repeat == 'n':
        poll_active = False
        
print("\n--- Poll Results ---")

for user, location in poll_results.items():
    print(user + " would like to visit " + location + ".")
