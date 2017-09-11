## %%% Begin Exercise 3-4
dinner_guests = []
dinner_guests.append('george')
dinner_guests.append('thomas')
dinner_guests.append('john')
#print(dinner_guests)
greeting = 'dear '
invite_body = 'Please accept my invitation to dinner.'
#print(greeting.title() + dinner_guests[0].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[1].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[2].title() + ',\n' + invite_body + "\n")
## %%% End Exercise 3-4
## %%% Begin Exercise 3-5
#decline_invite = dinner_guests[-1]
#print(decline_invite.title() + " is unable to attend the dinner." + "\n")
dinner_guests[-1] = 'martin'
#print(greeting.title() + dinner_guests[0].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[1].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[2].title() + ',\n' + invite_body + "\n")
# %%% End Exercise 3-5
# %%% Begin Exercise 3-6
greeting = "hello again, "
more_space = 'It appears that we have more space at the dinner table.'
#print(greeting.title() + dinner_guests[0].title() + '\n' + more_space + "\n")
#print(greeting.title() + dinner_guests[1].title() + '\n' + more_space + "\n")
#print(greeting.title() + dinner_guests[2].title() + '\n' + more_space + "\n")
dinner_guests.insert(0, 'bill')
#print(dinner_guests)
dinner_guests.insert(2, 'barack')
#print(dinner_guests)
dinner_guests.append('hillary')
#print(dinner_guests)
greeting = 'dear '
#print(greeting.title() + dinner_guests[0].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[1].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[2].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[3].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[4].title() + ',\n' + invite_body + "\n")
#print(greeting.title() + dinner_guests[5].title() + ',\n' + invite_body + "\n")
# %%% End Exercise 3-6
# %%% Begin Exercise 3-7
cancellation = 'I can only invite two people to dinner\n'
print(cancellation)
uninvited = dinner_guests.pop()
decline_message = "I regret to inform you that I must uninvite you for dinner."
print(greeting.title() + uninvited.title()+ ","  + '\n' + decline_message+ '\n' ) 
uninvited = dinner_guests.pop()
print(greeting.title() + uninvited.title()+ ","  + '\n' + decline_message+ '\n' )
uninvited = dinner_guests.pop()
print(greeting.title() + uninvited.title()+ ","  + '\n' + decline_message+ '\n' )
uninvited = dinner_guests.pop()
print(greeting.title() + uninvited.title()+ ","  + '\n' + decline_message+ '\n' )
still_invited = 'You will be pleased to know that you are still invited for dinner.'
print(greeting.title() + dinner_guests[0].title()+ ","  + '\n' + still_invited+ '\n' )
print(greeting.title() + dinner_guests[-1].title()+ ","  + '\n' + still_invited+ '\n' )
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)
print(len(dinner_guests))
