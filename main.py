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

# Chiffrement.
data = "EfreiParis"
key = "HNY5PfXZ"
iv = "EpitaParis"

encrypted_data = cbc_encrypt(data, key, iv)
print("Données chiffrées:", encrypted_data)

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

# Déchiffrement.
decrypted_data = cbc_decrypt(encrypted_data, key, iv)
print("Données déchiffrées:", decrypted_data)
