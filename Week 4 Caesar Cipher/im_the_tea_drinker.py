
def Cipher(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_text = ""
    for char in text:
        if char.isalpha():
            char_index = alphabet.find(char)
            new_index = (char_index + shift) % 26
            new_char = alphabet[new_index]
            new_text += new_char
        else:	
            new_text += char
    return new_text

print(Cipher("Hello World!", 5))