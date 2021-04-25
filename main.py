alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    # For testing
'''
text = "ezqz" #zulu
shift = 5
#mjqqt #hello
# 'ezqz' #zulu'''


# encrypt
def encrypt(encrypt_text, plain_shift):
    
    cipher_text = ''
    for letter in encrypt_text:

        letter_ID = alphabet.index(letter)
        shiften_letter_ID = letter_ID + plain_shift
        
        if shiften_letter_ID > 25:
            shiften_letter_ID -= 26
        
        cipher_text += alphabet[shiften_letter_ID]
        
    return print(f'The encoded text is {cipher_text}')


# decrypt
def decrypt(decrypt_text, plain_shift):

    cipher_text = ''
    for letter in decrypt_text:
        letter_ID = alphabet.index(letter)
        shiften_letter_ID = letter_ID - plain_shift
        
        if shiften_letter_ID < 0:
                shiften_letter_ID += 26
                
        cipher_text += alphabet[shiften_letter_ID]
        
    return print(f'The decoded text is {cipher_text}')
                
def caesar(encrypt_text = None, decrypt_text = None, plain_shift = 5):
    
    cipher_text = ''   
    
    if decrypt_text == None:
        for letter in encrypt_text:
            letter_ID = alphabet.index(letter)
            shiften_letter_ID = letter_ID + plain_shift
    
            if shiften_letter_ID > 25:
                shiften_letter_ID -= 26
    
            cipher_text += alphabet[shiften_letter_ID]
    
        return print(f'The encoded text is {cipher_text}')    
       
    elif encrypt_text == None:
        for letter in decrypt_text:
            letter_ID = alphabet.index(letter)
            shiften_letter_ID = letter_ID - plain_shift
    
            if shiften_letter_ID < 0:
                shiften_letter_ID += 26
            
            cipher_text += alphabet[shiften_letter_ID]
    
        return print(f'The decoded text is {cipher_text}')
     
     
def caesar_2(start_text, plain_shift, direction):
    cipher_text = ''
    for letter in start_text:
        letter_ID = alphabet.index(letter)
        
        if direction == 'encode':
            shiften_letter_ID = letter_ID + plain_shift
            if shiften_letter_ID > 25:
                shiften_letter_ID -= 26    
         
        elif direction =='decode':
            shiften_letter_ID = letter_ID - plain_shift
            if shiften_letter_ID < 0:
                shiften_letter_ID += 26
        
        cipher_text += alphabet[shiften_letter_ID]
        
    if direction == 'encode':
        return print(f'The encoded text is {cipher_text}') 
    else:
        return print(f'The decoded text is {cipher_text}')
     
while True:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'q' to quit:\n")
    if direction == 'q':
        break
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar_2(text,shift,direction)
    




#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# encrypt(plain_text=text, shift_amount=shift)