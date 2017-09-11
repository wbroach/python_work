from random import shuffle

key = {}
message = 'Encode this message.'
coded_message = ''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

code_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y' 
                , 'z']
                
punctuation = ['.', '?', '!']

shuffle(code_alphabet)

for i in alphabet:
    key[i] = code_alphabet[alphabet.index(i)]
    
for i in punctuation:
    key[i] = i
    
for i in range(0, len(message)):
    letter = message[i]
    if letter != ' ' and not letter.istitle(): 
        code_letter = key[letter]
        coded_message += code_letter
    elif letter.istitle():
        code_letter = key[letter.lower()]
        coded_message += code_letter.title()
    else:
        code_letter = ' ' 
        coded_message += code_letter
        
print(coded_message)
