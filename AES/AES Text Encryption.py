# AES Text Encryption.py
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import HMAC, SHA256
import time

# Encryption with AES-CBC + HMAC
def aes_encrypt(key, mac_key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext, AES.block_size))
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(cipher.iv + ct_bytes)
    return cipher.iv, ct_bytes, h.digest()

# Decryption with integrity check
def aes_decrypt(key, mac_key, iv, ciphertext, tag):
    h = HMAC.new(mac_key, digestmod=SHA256)
    h.update(iv + ciphertext)
    h.verify(tag)   # raises ValueError if tampered
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return pt

# Performance test
def performance_test():
    print("Algorithm   Input Size   Trials   Avg Enc (s)   Avg Dec (s)   Status")
    print("----------------------------------------------------------------------")

    key_sizes = [16, 24, 32]  # AES-128, AES-192, AES-256
    input_sizes = [100, 1024, 10*1024, 100*1024]
    trials = 5

    for key_size in key_sizes:
        key = get_random_bytes(key_size)
        mac_key = get_random_bytes(32)  # HMAC-SHA256 key
        for size in input_sizes:
            data = get_random_bytes(size)
            enc_times, dec_times = [], []
            passed = True

            for _ in range(trials):
                start = time.perf_counter()
                iv, ct, tag = aes_encrypt(key, mac_key, data)
                enc_times.append(time.perf_counter() - start)

                start = time.perf_counter()
                try:
                    dec = aes_decrypt(key, mac_key, iv, ct, tag)
                    if dec != data: passed = False
                except ValueError:  # tamper detected
                    passed = False
                dec_times.append(time.perf_counter() - start)

            print(f"AES-{key_size*8:<7} {size/1024 if size>=1024 else size:<10}{'KB' if size>=1024 else 'B'}"
                  f" {trials:<6} {sum(enc_times)/trials:.6f}      {sum(dec_times)/trials:.6f}      {'Passed' if passed else 'Failed'}")

if __name__ == "__main__":
    # Run performance test
    performance_test()

    print("\n--- User Input Encryption Demo ---")
    message = input("Enter a message to encrypt: ").encode()
    user_key = get_random_bytes(32)    # AES-256
    mac_key  = get_random_bytes(32)

    iv, ciphertext, tag = aes_encrypt(user_key, mac_key, message)
    decrypted = aes_decrypt(user_key, mac_key, iv, ciphertext, tag)

    print("\n[Encryption Result]")
    print(f"Key (hex): {user_key.hex()}")
    print(f"IV  (hex): {iv.hex()}")
    print(f"Ciphertext (hex): {ciphertext.hex()}")
    print(f"HMAC Tag (hex): {tag.hex()}")
    print(f"Decrypted: {decrypted.decode()}")
