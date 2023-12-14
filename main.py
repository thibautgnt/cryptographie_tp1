# Fonction pour effectuer l'opération XOR entre deux chaînes.
def xor(a, b):
    # Convertit les caractères des chaînes en valeurs ASCII, effectue XOR entre chaque paire de caractères,
    # et reconvertit le résultat en caractère. Le tout est assemblé en une seule chaîne.
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

# Fonction pour chiffrer les données en utilisant le mode CBC.
def cbc_encrypt(data, key, iv):
    encrypted = ""  # Chaîne pour stocker le résultat chiffré.
    previous_block = iv  # Initialise avec le vecteur d'initialisation (IV).

    # Traite le message par blocs de la taille de la clé.
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]  # Sélectionne un bloc de données.
        block = xor(block, previous_block)  # Chiffre le bloc avec XOR en utilisant le bloc précédent.
        encrypted += block  # Ajoute le bloc chiffré au résultat.
        previous_block = block  # Met à jour le bloc précédent pour le prochain tour.

    return encrypted

# Chiffrement.
data = "EfreiParis" # Données à chiffrer.
key = "HNY5PfXZ" # Clé de chiffrement.
iv = "EpitaParis" # Vecteur d'initialisation (IV).

encrypted_data = cbc_encrypt(data, key, iv) # Chiffre les données.
print("Données chiffrées:", encrypted_data) # Affiche le résultat chiffré.

# Fonction pour déchiffrer les données en utilisant le mode CBC.
def cbc_decrypt(data, key, iv):
    decrypted = ""  # Chaîne pour stocker le résultat déchiffré.
    previous_block = iv  # Initialise avec le vecteur d'initialisation (IV).

    # Traite les données chiffrées par blocs.
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]  # Sélectionne un bloc de données chiffrées.
        decrypted += xor(block, previous_block)  # Déchiffre le bloc avec XOR en utilisant le bloc précédent.
        previous_block = block  # Met à jour le bloc précédent pour le prochain tour.

    return decrypted

# Déchiffrement.
decrypted_data = cbc_decrypt(encrypted_data, key, iv) # Déchiffre les données.
print("Données déchiffrées:", decrypted_data) # Affiche le résultat déchiffré.