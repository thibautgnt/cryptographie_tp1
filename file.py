import os
import struct
import io

# Définition d'une fonction 'xor_bytes' qui effectue l'opération XOR entre deux blocs de données.
# Elle parcourt les deux blocs (a et b) et effectue l'opération XOR sur chaque paire d'octets.
def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Définition de la fonction 'cbc_encrypt_file' pour chiffrer un fichier en mode CBC (Cipher Block Chaining).
# Cette fonction lit le fichier source par blocs de la taille de la clé, applique un XOR avec le bloc précédent (initialisé avec le vecteur d'initialisation), puis écrit le résultat dans le fichier de sortie.
def cbc_encrypt_file(input_file, output_file, key, iv):
    block_size = len(key)
    previous_block = iv
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile: # Ouverture des fichiers en mode binaire, lecture (rb) et écriture (wb)
        while True:
            block = infile.read(block_size)
            if not block:
                break
            block = block.ljust(block_size, b'\0')  # Padding si nécessaire
            encrypted_block = xor_bytes(block, previous_block)
            outfile.write(encrypted_block)
            previous_block = encrypted_block

# Définition de la fonction 'cbc_decrypt_file' pour déchiffrer un fichier chiffré en mode CBC.
# Elle lit le fichier chiffré par blocs, applique un XOR avec le bloc précédent (commençant par le vecteur d'initialisation) et écrit le résultat dans le fichier de sortie.
def cbc_decrypt_file(input_file, output_file, key, iv):
    block_size = len(key)
    previous_block = iv
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile: # Ouverture des fichiers en mode binaire, lecture (rb) et écriture (wb)
        while True:
            block = infile.read(block_size)
            if not block:
                break
            decrypted_block = xor_bytes(block, previous_block)
            outfile.write(decrypted_block)
            previous_block = block

# Définition de la clé de chiffrement. La clé est un bloc d'octets utilisé dans l'algorithme de chiffrement.
encryption_key = b'06d47b0c838e7107e4e1cab17360a758'

# Définition du vecteur d'initialisation (IV). Il est utilisé pour introduire de l'aléatoire dans le processus de chiffrement.
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