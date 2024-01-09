# Fonction pour effectuer l'opération XOR entre deux chaînes.
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

# ---------------------------------------------------------------------------#

# Fonction pour chiffrer les données en utilisant le mode CBC.
def cbc_encrypt(data, key, iv):
    encrypted = ""          # Chaîne pour le résultat chiffré
    previous_block = iv     # Initialise avec le vecteur d'initialisation

    # Boucle sur chaque bloc de la taille de la clé
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]            # Extrait le bloc actuel
        block = xor(block, previous_block)    # XOR avec le bloc précédent
        encrypted += block                    # Ajoute à la chaîne chiffrée
        previous_block = block               # Prépare le prochain bloc

    return encrypted  # Retourne le résultat chiffré

# ---------------------------------------------------------------------------#

# Fonction pour déchiffrer les données en utilisant le mode CBC.
def cbc_decrypt(data, key, iv):
    decrypted = ""          # Chaîne pour le résultat déchiffré
    previous_block = iv     # Initialise avec le vecteur d'initialisation

    # Boucle sur chaque bloc chiffré de la taille de la clé
    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]            # Extrait le bloc chiffré actuel
        decrypted += xor(block, previous_block)  # XOR avec le bloc précédent
        previous_block = block               # Mise à jour du bloc précédent

    return decrypted  # Retourne le résultat déchiffré

# ---------------------------------------------------------------------------#

# Clé de chiffrement et vecteur d'initialisation.
encryption_key = "06d47b0c838e7107e4e1cab17360a758"
iv = "2c3135b2a77531f6a93a011fefd2e950"

# Demande à l'utilisateur le texte à chiffrer.
data_to_encrypt = input("Entrez le texte à chiffrer : ")

# Chiffrement.
encrypted_data = cbc_encrypt(data_to_encrypt, encryption_key, iv)
print("Données chiffrées:", encrypted_data)

# ---------------------------------------------------------------------------#

# Demande à l'utilisateur s'il souhaite déchiffrer les données.
decrypt_choice = input("Voulez-vous déchiffrer les données ? (Oui/Non) ").strip().lower()

if decrypt_choice == "oui" or decrypt_choice == "o":
    # Déchiffrement.
    decrypted_data = cbc_decrypt(encrypted_data, encryption_key, iv)
    print("Données déchiffrées:", decrypted_data)
else:
    print("Ok dommage")

# Fin du code, stylé