# ----------------------------------------------------------------------------------------------------------- #

                # Projet - Cryptographie par Thibaut GENET - B2 CS2 Efrei #

# ----------------------------------------------------------------------------------------------------------- #

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
        block_encrypted = xor(block, key)      # XOR avec la clé -------------- Ajouté suite au passage à l'oral
        encrypted += block                     # Ajoute à la chaîne chiffrée
        previous_block = block                 # Prépare le prochain bloc

    return encrypted 

# Fonction de déchiffrement CBC pour les chaînes de caractères
def cbc_decrypt(data, key, iv):
    decrypted = ""                              # Chaîne pour le résultat déchiffré
    previous_block = iv                         # Initialise avec le vecteur d'initialisation

    for i in range(0, len(data), len(key)):     # Boucle sur chaque bloc chiffré de la taille de la clé
        block = data[i:i+len(key)]              # Extrait le bloc chiffré actuel
        block_decrypted = xor(block, key)       # XOR avec la clé -------------- Ajouté suite au passage à l'oral
        decrypted += xor(block, previous_block) # XOR avec le bloc précédent
        previous_block = block                  # Mise à jour du bloc précédent

    return decrypted

# ----------------------------------------------------------------------------------------------------------- #

# Fonction XOR pour opération sur les octets
def xor_bytes(b1, b2):
    return bytes(a ^ b for a, b in zip(b1, b2))

# Fonction de chiffrement CBC pour les fichiers
def cbc_encrypt_file(file_in, file_out, key, iv):
    block_size = len(key)                                                                           # Taille de bloc de 16 octets (128 bits)
    previous_block = iv                                                                             # Utilisation directe du vecteur d'initialisation (IV) en tant que bytes

    with open(file_in, 'rb') as infile, open(file_out, 'wb') as outfile:                            # Ouverture des fichiers en mode binaire
        while True:                                                                                
            block = infile.read(block_size)                                                         # Lecture du fichier par blocs de 16 octets
            if not block: 
                break
            block = xor_bytes(block, previous_block)                                                # Opération XOR entre le bloc courant et le bloc précédent (IV au premier tour)
            cipher_block = xor_bytes(block, key)                                                    # Opération XOR entre le bloc courant et la clé -------------- Ajouté suite au passage à l'oral
            outfile.write(cipher_block)                                                             # Écriture du bloc chiffré dans le fichier de sortie
            previous_block = cipher_block                                                           # Mise à jour du bloc précédent

# Fonction de déchiffrement CBC pour les fichiers
def cbc_decrypt_file(file_in, file_out, key, iv):
    block_size = len(key)                                                                           # Taille de bloc de 16 octets (128 bits)
    previous_block = iv                                                                             # Utilisation directe du vecteur d'initialisation (IV) en tant que bytes

    with open(file_in, 'rb') as infile, open(file_out, 'wb') as outfile:                            # Ouverture des fichiers en mode binaire
        while True:
            block = infile.read(block_size)                                                         # Lecture du fichier par blocs de 16 octets
            if not block: 
                break
            decrypted_block = xor_bytes(block, key)                                                 # Opération XOR entre le bloc courant et la clé -------------- Ajouté suite au passage à l'oral
            plain_block = xor_bytes(decrypted_block, previous_block)                                # Opération XOR entre le bloc déchiffré et le bloc précédent (IV au premier tour)
            outfile.write(plain_block)                                                              # Écriture du bloc déchiffré dans le fichier de sortie
            previous_block = block                                                                  # Mise à jour du bloc précédent


# ----------------------------------------------------------------------------------------------------------- #


# Clé et vecteur d'initialisation (IV) pour les chaînes de caractères
encryption_key = '06d47b0c838e7107e4e1cab17360a758'
iv = '2c3135b2a77531f6a93a011fefd2e950'

# Clé et vecteur d'initialisation (IV) pour les fichiers
block_size = 16  # Taille de bloc de 16 octets (128 bits)
# Générer une clé aléatoire
encryption_file_key = os.urandom(block_size)
print("Clé de chiffrement:", encryption_file_key)
# Générer un vecteur d'initialisation (IV) aléatoire
iv_file = os.urandom(block_size)
print("Vecteur d'initialisation (IV):", iv_file)


# ----------------------------------------------------------------------------------------------------------- #

# Bonus pour que ce soit stylé
def print_separator():
    print("-" * 50)

# Affichage du menu utilisateur
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
