"""
defines a function for Caesar shift ciphers, to be used as a script callable
from the terminal
"""

def caesar(text, shift, output_path = None):

    if shift<0:
        shift = 26 + shift

    lower = list('abcdefghijklmnopqrstuvwxyz')
    upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    cipher_text = ""

    for char in text:
        if char in lower:
            plain_num = lower.index(char)
            cipher_num = (plain_num + shift) % 26
            cipher_char = lower[cipher_num]
            cipher_text += cipher_char

        elif char in upper:
            plain_num = upper.index(char)
            cipher_num = (plain_num + shift) % 26
            cipher_char = upper[cipher_num]
            cipher_text += cipher_char

        else:
            cipher_text += char

    if output_path == None:
        print(cipher_text)
    else:
        try:
            with open(output_path, 'x') as file_out:
                file_out.write(cipher_text)
        except FileExistsError:
            print(f"Error: The file '{output_path}' already exists.")

def substitution(text, substitution, output_path = None):

    alphabet = list(' abcdefghijklmnopqrstuvwxyz.,:;!?')

    if type(substitution) == str:
        key = list(substitution)
    elif type(substitution) == list:
        key = substitution

    cipher_text = ""
    for char in text:
        if char in alphabet and alphabet.index(char) <= len(key):
            index = alphabet.index(char)
            cipher_text += key[index]
        else:
            cipher_text += char

    if output_path == None:
        print(cipher_text)
    else:
        try:
            with open(output_path, 'x') as file_out:
                file_out.write(cipher_text)
        except FileExistsError:
            print(f"Error: The file '{output_path}' already exists.")
