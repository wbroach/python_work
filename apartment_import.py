from apartment import Apartment

while True:
    print("Enter the information for the apartment")
    print("(press 'q' at any time to quit)")
    
    user_complex_input = input("Enter complex name: ")
    if user_complex_input.lower() == 'q':
        break
    user_building_number_input = input("Enter building number: ")
    if user_building_number_input.lower() == 'q':
        break
    user_apartment_number_input = input("Enter apartment number: ")
    if user_apartment_number_input.lower() == 'q':
        break

    our_apartment = Apartment(user_complex_input, user_building_number_input, 
        user_apartment_number_input)
    
    our_apartment.show_cleaning_status() 

    prefer_to_clean = input("\nWould you like to clean apartment " + our_apartment.make_full_apt_name() + " (y or n)? ")
    if prefer_to_clean.lower() == 'q':
        break
    elif prefer_to_clean == 'y':
        our_apartment.make_apartment_clean()
    elif prefer_to_clean == 'n':
        print("\nYou're lazy.")
    else:
        print("You need to enter y or n")
        
    our_apartment.show_cleaning_status()

    play_again = input("\nWould you to play again? (y or n)? ")
    if play_again.lower() == 'q':
        break
    elif play_again.lower() == 'y':
        continue
    elif play_again.lower() == 'n':
        break

