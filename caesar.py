import string

plaintext = input("Введите строку, которую хотите зашифровать - ")

def encrypt_caesar(govn: str) -> str:
    """
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    word = []

    for i in range (0, len(govn)):
        word.append(govn[i])
    
    for i in range (0, len(govn)):
        if word[i] == "z":
            word[i] = "c"
        elif word[i] == "y":
            word[i] = "b"
        elif word[i] == "x":
            word[i] = "a"
        elif word[i] == "Z":
            word[i] = "C"
        elif word[i] == "Y":
            word[i] = "B"
        elif word[i] == "X":
            word[i] = "A"
        elif ord(word[i]) >= 65 and ord(word[i]) <= 90 or ord(word[i]) >= 97 and ord(word[i]) <= 122:
            word[i] = chr(ord(word[i]) + 3)

    ciphertext = ""
    for i in range (0, len(govn)):
        ciphertext += word[i]
    return ciphertext

def decrypt_caesar(govn: str) -> str:
    """
    >>> decrypt_caesar("SBWKRQ", 3)
    'PYTHON'
    >>> decrypt_caesar("sbwkrq", 3)
    'python'
    >>> decrypt_caesar("Sbwkrq3.6", 3)
    'Python3.6'
    >>> decrypt_caesar("", 3)
    ''
    """

    word = []
    
    for i in range (0, len(govn)):
        word.append(govn[i])
    
    for i in range (0, len(govn)):
        if word[i] == "c":
            word[i] = "z"
        elif word[i] == "b":
            word[i] = "y"
        elif word[i] == "a":
            word[i] = "x"
        elif word[i] == "C":
            word[i] = "Z"
        elif word[i] == "B":
            word[i] = "Y"
        elif word[i] == "A":
            word[i] = "X"
        elif ord(word[i]) >= 65 and ord(word[i]) <= 90 or ord(word[i]) >= 97 and ord(word[i]) <= 122:
            word[i] = chr(ord(word[i]) - 3)

    ciphertext = ""
    for i in range (0, len(govn)):
        ciphertext += word[i]
    return ciphertext

print("Ваша зашифрованная строка - ", encrypt_caesar(plaintext))
decode = input("Введите строку, которую хотите расшифровать - ")
print("Ваша расшифрованная строка - ", decrypt_caesar(decode))
