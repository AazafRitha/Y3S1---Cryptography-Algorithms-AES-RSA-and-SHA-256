# AES Image Encryption.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256
import os

def aes_file_encrypt(enc_key, mac_key, file_path):
    with open(file_path, 'rb') as f:
        data = f.read()

    cipher = AES.new(enc_key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))

    # Compute HMAC over IV + ciphertext
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(cipher.iv + ciphertext)
    tag = h.digest()

    encrypted_file = file_path + ".enc"
    with open(encrypted_file, 'wb') as f:
        f.write(cipher.iv + ciphertext + tag)

    print(f"File encrypted successfully: {encrypted_file}")
    return encrypted_file

def aes_file_decrypt(enc_key, mac_key, encrypted_file):
    with open(encrypted_file, 'rb') as f:
        blob = f.read()

    iv, rest = blob[:16], blob[16:]
    ciphertext, tag = rest[:-32], rest[-32:]

    # Verify HMAC
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(iv + ciphertext)
    h.verify(tag)   # raises ValueError if tampered

    cipher = AES.new(enc_key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    decrypted_file = encrypted_file.replace(".enc", "_dec")
    with open(decrypted_file, 'wb') as f:
        f.write(plaintext)

    print(f"File decrypted successfully: {decrypted_file}")
    return decrypted_file

def main():
    file_path = input("Enter the full path of the file to encrypt: ").strip()
    if not os.path.exists(file_path):
        print("File not found.")
        return

    enc_key = get_random_bytes(32)   # AES-256
    mac_key = get_random_bytes(32)   # HMAC key
    print(f"AES Key (hex): {enc_key.hex()}")
    print(f"MAC Key (hex): {mac_key.hex()}")

    enc_file = aes_file_encrypt(enc_key, mac_key, file_path)
    dec_file = aes_file_decrypt(enc_key, mac_key, enc_file)

if __name__ == "__main__":
    main()
