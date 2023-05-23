key = b'\x66'
with open('/Users/admin/Desktop/notdangerous.dat', 'rb') as f:
    encrypted_data = f.read()
decrypted_data = bytes([b ^ key[i % len(key)] for i, b in enumerate(encrypted_data)])
with open('decrypted.dat', 'wb') as f:
    f.write(decrypted_data)
