def encrypt_caesar(plaintext: str) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ''
    for govn in plaintext:
        if ('a' <= govn <= 'z') or ('A' <= govn <= 'Z'):
            anus = ord(govn) + 3
            if (anus > ord('Z')) and (anus < ord('a')) or (anus > ord('z')):
                anus -= 26
            ciphertext += chr(anus)
        else:
            ciphertext += govn
    return ciphertext


def decrypt_caesar(ciphertext: str) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for govn in ciphertext:
        if ('a' <= govn <= 'z') or ('A' <= govn <= 'Z'):
            anus = ord(govn) - 3
            if (anus < ord('a')) and (anus > ord('Z')) or (anus < ord('A')):
                anus += 26
            plaintext += chr(anus)
        else:
            plaintext += govn
    return plaintext
