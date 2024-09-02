ciphertext = 'vpf hinf sqwirk eidjlyb czxa tziuomg'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def decode(cipher,key,alphabet):
    decrypt = ''
    for letter in cipher:
        if letter == ' ':
            decrypt += letter
        else:
            decrypt += alphabet[key.find(letter)]
    return decrypt
    
for shift in range(26):
    key = alphabet[shift:] + alphabet[:shift]
    print(decode(ciphertext,key,alphabet))
