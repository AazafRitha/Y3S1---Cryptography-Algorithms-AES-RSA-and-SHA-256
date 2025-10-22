# RSA_Text_Encryption.py
# Run: python RSA_Text_Encryption.py
# Make sure: pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from time import perf_counter

# ----- Generate Key Pair -----
def generate_rsa_keys(key_size=2048):
    key = RSA.generate(key_size)
    private_key = key
    public_key = key.publickey()
    return public_key, private_key

# ----- Encryption -----
def rsa_encrypt(public_key, plaintext):
    cipher = PKCS1_OAEP.new(public_key, hashAlgo=SHA256)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# ----- Decryption -----
def rsa_decrypt(private_key, ciphertext):
    cipher = PKCS1_OAEP.new(private_key, hashAlgo=SHA256)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# ----- Performance Test -----
def performance_test():
    print("Algorithm   Key Size   Trials   Avg Enc (ms)   Avg Dec (ms)   Status")
    print("---------------------------------------------------------------")
    key_sizes = [1024, 2048, 4096]
    trials = 5
    message = b"RSA Performance Test for IE3082"
    for bits in key_sizes:
        pub, priv = generate_rsa_keys(bits)
        enc_times, dec_times = [], []
        passed = True
        for _ in range(trials):
            t0 = perf_counter()
            ct = rsa_encrypt(pub, message)
            t1 = perf_counter()
            dec = rsa_decrypt(priv, ct)
            t2 = perf_counter()
            if dec != message:
                passed = False
            enc_times.append((t1 - t0) * 1000)
            dec_times.append((t2 - t1) * 1000)
        print(f"RSA-{bits:<7} {bits:<8} {trials:<7} {sum(enc_times)/trials:>10.3f}     {sum(dec_times)/trials:>10.3f}     {'Passed' if passed else 'Failed'}")

# ----- User Input Demo -----
def user_demo():
    print("\n--- User Input Encryption Demo ---")
    text = input("Enter a message to encrypt: ").encode()
    pub, priv = generate_rsa_keys(2048)
    ciphertext = rsa_encrypt(pub, text)
    decrypted = rsa_decrypt(priv, ciphertext)
    print("\n[Encryption Result]")
    print(f"Public Key (n bits): {pub.size_in_bits()}")
    print(f"Ciphertext (hex): {ciphertext.hex()[:80]}...")  # show first part
    print(f"Decrypted: {decrypted.decode()}")

if __name__ == "__main__":
    performance_test()
    user_demo()
