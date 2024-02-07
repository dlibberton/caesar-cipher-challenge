def caesar_cipher(string, shift_amount):
    def shift_char(char, shift):
        if char.isalpha():
            if char.islower():
                shifted_char = chr(((ord(char) - 97 + shift) % 26) + 97)
            else:
                shifted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            return shifted_char
        else:
            return char

    encrypted_text = ""
    for char in string:
        encrypted_text += shift_char(char, shift_amount)
    return encrypted_text