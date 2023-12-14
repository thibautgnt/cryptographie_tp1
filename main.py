def xor(a, b):
    return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(a, b))

def cbc_encrypt(data, key, iv):
    encrypted = ""
    previous_block = iv

    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        block = xor(block, previous_block)
        encrypted += block
        previous_block = block

    return encrypted

# Encrypt
data = "EfreiParis"
key = "HNY5PfXZ"
iv = "EpitaParis"

encrypted_data = cbc_encrypt(data, key, iv)
print("Données chiffrées:", encrypted_data)

def cbc_decrypt(data, key, iv):
    decrypted = ""
    previous_block = iv

    for i in range(0, len(data), len(key)):
        block = data[i:i+len(key)]
        decrypted += xor(block, previous_block)
        previous_block = block

    return decrypted

