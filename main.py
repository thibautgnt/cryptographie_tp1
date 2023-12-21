# Fonction pour effectuer l'opération XOR entre deux chaînes.
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

# Fonction pour chiffrer les données en utilisant le mode CBC.
def cbc_encrypt(data, key, iv):
    encrypted = ""
    previous_block = iv

    # Traite le message par blocs de la taille de la clé.
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        block = xor(block, previous_block)
        encrypted += block
        previous_block = block

    return encrypted

# Fonction pour déchiffrer les données en utilisant le mode CBC.
def cbc_decrypt(data, key, iv):
    decrypted = ""
    previous_block = iv

    # Traite les données chiffrées par blocs.
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        decrypted += xor(block, previous_block)
        previous_block = block

    return decrypted

# Demande à l'utilisateur le texte à chiffrer.
data_to_encrypt = input("Entrez le texte à chiffrer : ")

# Demande à l'utilisateur la clé de chiffrement.
encryption_key = input("Entrez la clé de chiffrement : ")

# Demande à l'utilisateur le vecteur d'initialisation (IV).
iv = input("Entrez le vecteur d'initialisation (IV) : ")

# Chiffrement.
encrypted_data = cbc_encrypt(data_to_encrypt, encryption_key, iv)
print("Données chiffrées:", encrypted_data)

# Demande à l'utilisateur s'il souhaite déchiffrer les données.
decrypt_choice = input(" Voulez-vous déchiffrer les données ? (Oui/Non) ").strip().lower()

if decrypt_choice == "oui" or decrypt_choice == "o":
    # Déchiffrement.
    decrypted_data = cbc_decrypt(encrypted_data, encryption_key, iv)
    print("Données déchiffrées:", decrypted_data)
else:
    print("Ok dommage.")