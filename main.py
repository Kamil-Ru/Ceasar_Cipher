from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, plain_shift, direction):
    cipher_text = ''
    
    if direction =='decode':
            plain_shift *= -1
      
    for letter in start_text:
        
        if letter.isalpha():
            letter_ID = alphabet.index(letter)
                    
            shiften_letter_ID = letter_ID + plain_shift
            
            if shiften_letter_ID > 25:
                    shiften_letter_ID -= 26 
            if shiften_letter_ID < 0:
                    shiften_letter_ID += 26
                    
            cipher_text += alphabet[shiften_letter_ID]
        else:
            cipher_text += letter
        
    return print(f'The {direction} text is {cipher_text}') 
        
        
while True:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'q' to quit:\n")
    if direction == 'q':
        break
    
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
    
    caesar(text,shift,direction)
    


