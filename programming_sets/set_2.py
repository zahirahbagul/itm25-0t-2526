'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    '''
    if letter == " ":
        return " "
    return chr((ord(letter)-ord("A")+shift)% 26+ord ("A"))

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    return''.join(shift_letter(char,shift)for chat in message)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    '''
    if letter == " ":
        return " "
    shift = ord (letter_shift)-ord("A")
    return shift_letter(letter, shift)

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    '''
    result=[]
    key_index=0
    for ch in message:
        if ch==" ":
            result.append(" ")
        else:
            shift = ord(key[key_index % len(key)]) - ord ("A")
            result.append(shift_letter(ch, shift))
            key_index += 1
    return ''.join(result)

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.
    '''
    while len(message) % shift != 0:
        message += "_"
    encoded= ""
    for i in range(len(message)):
        index = (i//shift) + (len(message)//shift) * (i%shift)
        encoded += message[index]
    return encoded

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    '''
    rows = len(message) // shift
    decoded= ""
    for i in range(len(message_)):
        index=(i % rows)*shift + (i// rows)
        decoded += message[index]
    return decoded
