
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter.isalpha():
            shifted_index = (ord(letter) - 97 + shift_amount) % 26
            cipher_text += chr(shifted_index + 97)
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter.isalpha():
            shifted_index = (ord(letter) - 97 - shift_amount) % 26
            plain_text += chr(shifted_index + 97)
        else:
            plain_text += letter
    print(f"The decoded text is {plain_text}")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)    

if direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)