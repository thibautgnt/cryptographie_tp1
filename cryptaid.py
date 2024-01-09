# Importation des modules
import os # Pour les opérations sur les fichiers
import struct # Pour les opérations sur les octets
import io # Pour les opérations sur les fichiers

# ----------------------------------------------------------------------------------------------------------- #

# Fonction XOR pour opération bit à bit
def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b)) 

# Fonction de chiffrement CBC pour les chaînes de caractères
def cbc_encrypt(data, key, iv):
    encrypted = ""                             # Chaîne pour le résultat chiffré
    previous_block = iv                        # Initialise avec le vecteur d'initialisation

    for i in range(0, len(data), len(key)):    # Boucle sur chaque bloc de la taille de la clé
        block = data[i:i+len(key)]             # Extrait le bloc actuel
        block = xor(block, previous_block)     # XOR avec le bloc précédent
        encrypted += block                     # Ajoute à la chaîne chiffrée
        previous_block = block                 # Prépare le prochain bloc

    return encrypted 

# Fonction de déchiffrement CBC pour les chaînes de caractères
def cbc_decrypt(data, key, iv):
    decrypted = ""                              # Chaîne pour le résultat déchiffré
    previous_block = iv                         # Initialise avec le vecteur d'initialisation

    for i in range(0, len(data), len(key)):     # Boucle sur chaque bloc chiffré de la taille de la clé
        block = data[i:i+len(key)]              # Extrait le bloc chiffré actuel
        decrypted += xor(block, previous_block) # XOR avec le bloc précédent
        previous_block = block                  # Mise à jour du bloc précédent

    return decrypted

# ----------------------------------------------------------------------------------------------------------- #

# Fonction XOR pour opération sur les octets
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b)) # zip() permet de grouper les éléments de deux listes en une seule liste de tuples

# Fonction de chiffrement CBC pour les fichiers
def cbc_encrypt_file(input_file, output_file, key, iv_file):
    block_size = len(key)                                                               # Détermine la taille du bloc en fonction de la clé
    previous_block = iv_file                                                            # Initialise avec le vecteur d'initialisation

    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:          # Ouverture des fichiers en mode binaire
        while True:                                                                     # Boucle sur chaque bloc du fichier
            block = infile.read(block_size)                                             # Lecture d'un bloc du fichier
            if not block:                                                               # Si aucun bloc n'est lu, fin de la boucle
                break 
            block = block.ljust(block_size, b'\0')                                      # Ajoute du padding si le bloc est plus petit que la taille de la clé
            encrypted_block = xor_bytes(block, previous_block)                          # Chiffre le bloc
            outfile.write(encrypted_block)                                              # Écrit le bloc chiffré dans le fichier de sortie
            previous_block = encrypted_block                                            # Mise à jour du bloc précédent

# Fonction de déchiffrement CBC pour les fichiers
def cbc_decrypt_file(input_file, output_file, key, iv_file):
    block_size = len(key)                                                               # Détermine la taille du bloc en fonction de la clé
    previous_block = iv_file                                                            # Initialise avec le vecteur d'initialisation
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:          # Ouverture des fichiers en mode binaire
        while True:                                                                     # Boucle sur chaque bloc du fichier
            block = infile.read(block_size)                                             # Lecture d'un bloc du fichier
            if not block:                                                               # Si aucun bloc n'est lu, fin de la boucle
                break
            decrypted_block = xor_bytes(block, previous_block)                          # Déchiffre le bloc
            outfile.write(decrypted_block)                                              # Écrit le bloc déchiffré dans le fichier de sortie
            previous_block = block                                                      # Mise à jour du bloc précédent pour le prochain cycle

# ----------------------------------------------------------------------------------------------------------- #

# Clé de chiffrement et vecteur d'initialisation
            
encryption_key = '06d47b0c838e7107e4e1cab17360a758'
iv = '2c3135b2a77531f6a93a011fefd2e950'

encryption_file_key = b'06d47b0c838e7107e4e1cab17360a758'
iv_file = b'2c3135b2a77531f6a93a011fefd2e950'

# ----------------------------------------------------------------------------------------------------------- #

# Bonus pour que ce soit stylé
def print_separator():
    print("-" * 50)

# Affichage du menu utilisateur avec une présentation améliorée
print_separator()
print("Ça chiffre ou ça déchiffre aujourd'hui chef ?")
print_separator()
print("Que souhaitez-vous faire ?")
print("  1 - Chiffrer du texte")
print("  2 - Déchiffrer du texte")
print("  3 - Chiffrer un fichier")
print("  4 - Déchiffrer un fichier")
print("  5 - Rien du tout ...")
print_separator()
choice = input("Entrez votre choix (1, 2, 3, 4 ou 5) : ")

if choice == '1' or choice == '2':
    data_to_encrypt = input("Entrez le texte à chiffrer : ")
    encrypted_data = cbc_encrypt(data_to_encrypt, encryption_key, iv)
    print("Données chiffrées:", encrypted_data)
    decrypt_choice = input("Voulez-vous déchiffrer les données ? (Oui/Non) ").strip().lower()
    if decrypt_choice in ["oui", "o"]:
        decrypted_data = cbc_decrypt(encrypted_data, encryption_key, iv)
        print("Données déchiffrées:", decrypted_data)

elif choice == '3' or choice == '4':
    input_filename = 'texte.txt' # On peut même mettre une image
    encrypted_filename = 'texte_encrypted.txt'
    decrypted_filename = 'texte_decrypted.txt'
    cbc_encrypt_file(input_filename, encrypted_filename, encryption_file_key, iv_file)
    print(f'Fichier chiffré créé : {encrypted_filename}')
    cbc_decrypt_file(encrypted_filename, decrypted_filename, encryption_file_key, iv_file)
    print(f'Fichier déchiffré créé : {decrypted_filename}')

else:
    print("Ciao !")