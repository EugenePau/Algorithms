def to_hex(letter):
    ## (str) -> (int)
    hex_num = hex(ord(letter)).replace('0x','')
    if len(hex_num) == 1:
        hex_num = '0' + hex_num
    return hex_num

def to_text(hex_num):
    ## (int) -> (str)
    return chr(int(str(hex_num),16))

def bitwise_xor(hex1,hex2):
    ## (int,int) -> (int)
    xor_num = hex(int(hex1,16) ^ int(hex2,16)).replace('0x','')
    if len(xor_num) == 1:
        xor_num = '0' + xor_num
    return xor_num


def otp_encrpyt(text,key):
    ## plaintext, plaintext -> hex
    assert len(text) == len(key)
    cipherhex = ''
    for i in range(len(text)):
        cipherhex += str(bitwise_xor(to_hex(text[i]),to_hex(key[i])))
    hex_text = ''.join([to_hex(letter) for letter in text])
    hex_key = ''.join([to_hex(letter) for letter in key])
    return cipherhex, hex_text, hex_key


def otp_decrpyt(text,key):
    ## hex, hex -> plaintext
    assert len(text) == len(key)
    recovertext = ''
    for i in range(len(text)//2):
        recovertext += to_text(bitwise_xor(text[2*i]+text[2*i+1],key[2*i]+key[2*i+1]))
    return recovertext

text = 'secret message'
key = 'my secret keys'
cipher_hex, text_hex, key_hex = otp_encrpyt(text,key)
print(cipher_hex, text_hex, key_hex)

## Show A' xor K = A
print(otp_decrpyt(cipher_hex,key_hex))

## Show A xor A' = K (Therefore you can reverse-engineering the private key after
## obtaining a message-cipher pair from a successful multiple-time pad attack
print(otp_decrpyt(cipher_hex,text_hex))


