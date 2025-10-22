# SHA_256.py
# Run: python SHA_256.py
# Requirements: Python 3.10+ (uses hashlib and hmac)

import hashlib, hmac, os, time

def sha256_hash(data: bytes) -> str:
    """Generate SHA-256 digest"""
    h = hashlib.sha256()
    h.update(data)
    return h.hexdigest()

def hmac_sha256(key: bytes, data: bytes) -> str:
    """Generate HMAC-SHA256 signature"""
    return hmac.new(key, data, hashlib.sha256).hexdigest()

def test_hash_and_hmac():
    print("=== SHA-256 / HMAC-SHA256 Implementation & Initial Testing ===")

    # Text Hash Test
    message = b"Hello IE3082 - Cryptography Test"
    digest = sha256_hash(message)
    print(f"\nPlaintext: {message.decode()}")
    print(f"SHA-256 Digest: {digest}")

    # HMAC Test
    key = b"shared_secret_key"
    tag = hmac_sha256(key, message)
    print(f"HMAC-SHA256 Tag: {tag}")

    # Tamper Test
    tampered_message = b"Hello IE3082 - Cryptography TesT"  # minor change in last character
    tampered_tag = hmac_sha256(key, tampered_message)
    print("\nTamper Detection:")
    if tag == tampered_tag:
        print("Tampering not detected (incorrect implementation).")
    else:
        print("Tampering detected successfully.")
        print("\nNote: Tampering means even a small change in the original message "
              "or data content produces a completely different digest or HMAC tag. "
              "This demonstrates SHA-256’s sensitivity and ability to ensure data integrity.")

def performance_test():
    print("\n=== SHA-256 / HMAC-SHA256 Performance Test ===")
    sizes = [100, 1024, 10_000, 100_000, 1_000_000]  # 100B to 1MB
    trials = 5
    print("Input Size (bytes) | SHA-256 Avg (ms) | HMAC-SHA256 Avg (ms)")
    print("-------------------------------------------------------------")
    for s in sizes:
        data = os.urandom(s)
        key = b"shared_secret_key"
        sha_times, hmac_times = [], []
        for _ in range(trials):
            t0 = time.perf_counter()
            sha256_hash(data)
            t1 = time.perf_counter()
            hmac_sha256(key, data)
            t2 = time.perf_counter()
            sha_times.append((t1 - t0) * 1000)
            hmac_times.append((t2 - t1) * 1000)
        print(f"{s:<18}{sum(sha_times)/trials:>12.4f}{sum(hmac_times)/trials:>20.4f}")

def user_input_demo():
    print("\n=== SHA-256 / HMAC-SHA256 User Input Demo ===")
    user_text = input("Enter a message to hash: ").encode()
    digest = sha256_hash(user_text)
    print(f"SHA-256 Digest: {digest}")

    key = b"shared_secret_key"
    tag = hmac_sha256(key, user_text)
    print(f"HMAC-SHA256 Tag: {tag}")

    verify = input("\nEnter a message to verify (to test tampering): ").encode()
    verify_tag = hmac_sha256(key, verify)

    if verify_tag == tag:
        print("Message verified successfully (integrity intact).")
    else:
        print("Message verification failed (tampering detected).")

if __name__ == "__main__":
    test_hash_and_hmac()
    performance_test()
    user_input_demo()
