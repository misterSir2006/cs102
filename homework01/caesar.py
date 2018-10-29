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
    for ab in plaintext:
        if ('a' <= ab <= 'z') or ('A' <= ab <= 'Z'):
            ans = ord(ab) + 3
            if (ans > ord('Z')) and (ans < ord('a')) or (ans > ord('z')):
                ans -= 26
            ciphertext += chr(ans)
        else:
            ciphertext += ab
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
    for ab in ciphertext:
        if ('a' <= ab <= 'z') or ('A' <= ab <= 'Z'):
            ans = ord(ab) - 3
            if (ans < ord('a')) and (ans > ord('Z')) or (ans < ord('A')):
                ans += 26
            plaintext += chr(ans)
        else:
            plaintext += ab
    return plaintext
