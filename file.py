import os
import struct
import io

# Définition d'une fonction 'xor' qui effectue l'opération XOR entre deux blocs de données.
# Elle parcourt les deux blocs (a et b) et effectue l'opération XOR sur chaque paire d'octets.
def xor(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# ---------------------------------------------------------------------------#

# Définition de la fonction 'cbc_encrypt_file' pour chiffrer un fichier en mode CBC (Cipher Block Chaining).
# Cette fonction lit le fichier source par blocs de la taille de la clé, applique un XOR avec le bloc précédent (initialisé avec le vecteur d'initialisation), puis écrit le résultat dans le fichier de sortie.
def cbc_encrypt_file(input_file, output_file, key, iv):
    block_size = len(key)    # Détermine la taille du bloc en fonction de la clé
    previous_block = iv      # Initialise avec le vecteur d'initialisation

    # Ouverture des fichiers en mode binaire
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            block = infile.read(block_size)   # Lecture d'un bloc du fichier
            if not block:                     # Si aucun bloc n'est lu, fin de la boucle
                break
            # Ajoute du padding si le bloc est plus petit que la taille de la clé
            block = block.ljust(block_size, b'\0')
            encrypted_block = xor(block, previous_block)  # Chiffre le bloc
            outfile.write(encrypted_block)                # Écrit le bloc chiffré dans le fichier de sortie
            previous_block = encrypted_block              # Mise à jour du bloc précédent

# ---------------------------------------------------------------------------#

# Définition de la fonction 'cbc_decrypt_file' pour déchiffrer un fichier chiffré en mode CBC.
# Elle lit le fichier chiffré par blocs, applique un XOR avec le bloc précédent (commençant par le vecteur d'initialisation) et écrit le résultat dans le fichier de sortie.
def cbc_decrypt_file(input_file, output_file, key, iv):
    block_size = len(key)    # Détermine la taille du bloc basée sur la longueur de la clé
    previous_block = iv      # Initialise avec le vecteur d'initialisation

    # Ouverture des fichiers en mode binaire
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            block = infile.read(block_size)   # Lecture d'un bloc du fichier
            if not block:                     # Si aucun bloc n'est lu, fin de la boucle
                break
            decrypted_block = xor(block, previous_block)  # Déchiffre le bloc
            outfile.write(decrypted_block)               # Écrit le bloc déchiffré dans le fichier de sortie
            previous_block = block                       # Mise à jour du bloc précédent pour le prochain cycle

# ---------------------------------------------------------------------------#

# Clé de chiffrement et vecteur d'initialisation.
encryption_key = b'06d47b0c838e7107e4e1cab17360a758'
iv = b'2c3135b2a77531f6a93a011fefd2e950'

# Définition des noms des fichiers : le fichier source à chiffrer, le fichier de sortie chiffré, et le fichier de sortie déchiffré.
input_filename = 'texte.txt' 
encrypted_filename = 'texte_encrypted.txt'
decrypted_filename = 'texte_decrypted.txt'

# Appel de la fonction de chiffrement sur le fichier source, création du fichier chiffré, et affichage du nom du fichier chiffré.
cbc_encrypt_file(input_filename, encrypted_filename, encryption_key, iv)
print(f'Fichier chiffré créé : {encrypted_filename}')

# Appel de la fonction de déchiffrement sur le fichier chiffré, création du fichier déchiffré, et affichage du nom du fichier déchiffré.
cbc_decrypt_file(encrypted_filename, decrypted_filename, encryption_key, iv)
print(f'Fichier déchiffré créé : {decrypted_filename}')

# Fin du code, stylé