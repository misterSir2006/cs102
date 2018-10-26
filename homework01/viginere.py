def encrypt_vigenere(plaintext: str, keyword: str) ->str:
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    # PUT YOUR CODE HERE

    ciphertext= "";

    def encrypt(a:str,b:str)->str:

        keyS = 0
        ret = ""

        if (b.islower()):
            keyS = ord(b)-97
        elif (b.isupper()):
            keyS = ord(b)-65

        if (a.islower()):
            ret = chr(97+(ord(a)-97+keyS)%26)
        elif(a.isupper()):
            ret = chr(65+(ord(a)-65+keyS)%26)
        return ret

    for a in range(len(plaintext)):
        ciphertext += encrypt(plaintext[a],keyword[a % len(keyword)])
    
    return ciphertext


def decrypt_vigenere(ciphertext:str, keyword:str)->str:
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    # PUT YOUR CODE HERE

    plaintext= "";

    def decrypt(c:str,d:str)->str:

        keyS = 0
        ret = ""

        if (d.islower()):
            keyS = ord(d)-97
        elif(d.isupper()):
            keyS = ord(d)-65

        if (c.islower()):
            ret = chr(97+(26+ord(c)-97-keyS)%26)
        elif(c.isupper()):
            ret = chr(65+(26+ord(c)-65-keyS)%26)

        return ret


    for c in range(len(ciphertext)):
        plaintext += decrypt(ciphertext[c],keyword[c%len(keyword)])
    return plaintext



