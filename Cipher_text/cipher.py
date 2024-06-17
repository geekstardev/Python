alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def cipher_convertion(text, shift, cipher_direction):
    converted_text = ""
    if cipher_direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            converted_text += alphabet[new_position]
        else:
            converted_text += char
    print(f"The {cipher_direction}ed text is {converted_text}")

from art import logo
print(logo)

play = False
while not play:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    plain_text = input("Type your message:\n").lower()
    shifts = int(input("Type the shift number:\n"))

    shifts = shifts % 26

    cipher_convertion(text=plain_text,shift=shifts,cipher_direction=direction)
    
    ans = input("If you want to continue type yes or tyoe No for exit.\n")

    if ans == "no":
        play = True
        print("Goodbye :)")
















# def encrypt(text,shift):
#     cipher_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The Encoded text is {cipher_text}")

# def decrypt(cipher_text,shift):
#     plain_text = ""
#     for i in cipher_text:
#         position = alphabet.index(i)
#         new_position = position - shift
#         new_letter = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The Encoded text is {plain_text}")

# def cipher_convertion(text,shift,direction):
#     converted_text = ""
#     for i in text:
#         position = alphabet.index(i)
#         if direction == 'decode':
#             shift *= -1
#         new_position = position + shift
#         converted_text = alphabet[new_position]
#         plain_text += new_letter
#     print(f"The {direction}ed text is {converted_text}")

# if direction == 'encode':
#     encrypt(text = plain_text,shift= shifts)
# elif direction == 'decode':
#     decrypt(cipher_text = plain_text, shift = shifts)
# else:
#     print("Entr Valid Option")