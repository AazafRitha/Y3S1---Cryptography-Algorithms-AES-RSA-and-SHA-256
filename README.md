# Y3S1---Cryptography-Algorithms-AES-RSA-and-SHA-256


This repository contains the research, implementation, and performance evaluation of three core cryptographic algorithms: **Advanced Encryption Standard (AES)**, **Rivest–Shamir–Adleman (RSA)**, and **Secure Hash Algorithm 256 (SHA-256)**.  
It was developed as part of the **IE3082 – Cryptography** module, Year 3 Semester 2, for the **B.Sc. (Hons) in Information Technology (Specializing in Cyber Security)** degree at the **Sri Lanka Institute of Information Technology (SLIIT)**.

---

## 1. Project Overview

The main objective of this assignment was to analyze and compare different cryptographic algorithms in terms of their **design principles**, **security properties**, and **performance characteristics**.  
The study covers the three main cryptographic objectives:  
- **Confidentiality** – protected using AES  
- **Integrity** – ensured using SHA-256  
- **Authentication and Key Management** – achieved through RSA  

The algorithms were selected based on modern relevance, academic importance, and industrial applications such as SSL/TLS, VPNs, disk encryption, and blockchain.

---

## 2. Group Members and Contributions

| Name | IT Number | Contribution |
|------|------------|--------------|
| J. Aazaf Ritha | Coordinated the project, implemented AES encryption/decryption, testing, and report integration |
| S. M. F. Hana | Implemented RSA algorithm, conducted RSA testing, and performance analysis |
| M. F. M. Farhan | Developed SHA-256 hashing and HMAC, performed integrity verification and analysis |
| H. M. S. H. Wijerathna | Assisted in RSA key generation and visualization of performance results |
| R. M. T. P. Rasnayake | Supported AES testing, debugging, and code refinement |

---

## 3. Selected Algorithms

### 3.1 Advanced Encryption Standard (AES)
AES is a symmetric block cipher standardized by NIST in 2001.  
It operates on 128-bit data blocks using keys of 128, 192, or 256 bits.  
The algorithm uses a **Substitution–Permutation Network (SPN)** consisting of SubBytes, ShiftRows, MixColumns, and AddRoundKey operations.

**Key Features:**
- Symmetric key encryption with high throughput
- Resistant to differential and linear cryptanalysis
- Used in TLS, VPNs, and full disk encryption (e.g., BitLocker, FileVault)

**Vulnerabilities and Countermeasures:**
- Susceptible to side-channel attacks → use constant-time implementations  
- Insecure in ECB mode → use CBC or GCM modes  
- Key management issues → use strong random key generation and secure key storage

---

### 3.2 Rivest–Shamir–Adleman (RSA)
RSA is an asymmetric encryption algorithm introduced in 1977.  
It relies on the mathematical difficulty of factoring large prime products.

**Key Generation Process:**
1. Choose two large prime numbers p and q  
2. Compute n = p × q and ϕ(n) = (p − 1)(q − 1)  
3. Select e such that gcd(e, ϕ(n)) = 1  
4. Compute d as the modular inverse of e mod ϕ(n)

**Applications:**
- Secure key exchange (used in SSL/TLS)
- Digital signatures and certificate validation
- Authentication in PKI-based systems

**Limitations:**
- Slower encryption/decryption compared to AES  
- Requires large key sizes (2048–4096 bits) for modern security

---

### 3.3 Secure Hash Algorithm (SHA-256)
SHA-256 is a one-way hash function from the SHA-2 family, standardized by NIST in FIPS 180-4.  
It outputs a 256-bit fixed-length hash and provides **collision resistance** and **data integrity**.

**Design Principles:**
- Based on the Merkle–Damgård structure  
- Uses 64 rounds of logical operations (XOR, rotation, and addition)  
- Resistant to preimage and collision attacks  

**Applications:**
- Password storage and verification  
- Blockchain transaction integrity (Bitcoin, Ethereum)  
- HMAC for message authentication

---

## 4. Implementation Details

**Programming Language:** Python 3.10  
**Libraries Used:** PyCryptodome, hashlib, hmac, os, time  

| File | Description |
|------|--------------|
| `AES_Text_Encryption.py` | Text encryption/decryption using AES-CBC with HMAC verification |
| `AES_Image_Encryption.py` | File encryption/decryption for binary data using AES-256 |
| `RSA_Text_Encryption.py` | RSA key generation, encryption, and decryption with OAEP padding |
| `SHA_256.py` | SHA-256 and HMAC-SHA-256 hashing, integrity, and tamper detection tests |
| `IT23151710_IT23255142_IT23422070_IT23306936_IT23246546.pdf` | Final academic report with detailed results and references |

---

## 5. Methodology

1. **Research Phase (Week 8):**
   - Studied the history, design, and applications of AES, RSA, and SHA-256  
   - Identified strengths, vulnerabilities, and mitigation strategies  

2. **Implementation Phase (Week 9):**
   - Implemented algorithms using Python  
   - Verified encryption/decryption correctness  

3. **Testing Phase (Week 10):**
   - Measured encryption and decryption times  
   - Tested multiple key sizes and input file types  
   - Recorded execution time, CPU, and memory usage  

4. **Final Analysis (Weeks 11–13):**
   - Compiled research, testing data, and performance graphs  
   - Compared algorithms and proposed suitable use cases  

---

## 6. Performance Results

| Algorithm | Input | Avg Encryption Time | Avg Decryption Time | Remarks |
|------------|--------|---------------------|---------------------|----------|
| AES-128 | 100 KB | 0.000594 s | 0.000585 s | Fastest for bulk data |
| RSA-2048 | Text (short message) | 0.730 ms | 4.144 ms | Balanced security and efficiency |
| SHA-256 | 10 MB | 7.5 ms | N/A | High efficiency for integrity checks |

**Summary of Findings:**
- AES achieved near-linear scalability and low latency.  
- RSA performance decreased with larger key sizes but maintained strong security.  
- SHA-256 and HMAC-SHA-256 verified integrity efficiently, with negligible overhead.

---

## 7. Analysis and Discussion

- **AES** is ideal for high-volume data encryption due to its speed and simplicity.  
- **RSA** is computationally heavy but essential for secure key management and signatures.  
- **SHA-256** ensures reliable data integrity and supports HMAC-based authentication.  
- Combining AES + RSA + SHA-256 provides a secure framework covering confidentiality, authenticity, and integrity — consistent with modern encryption architectures.

---

## 8. Evaluation Criteria Alignment

| Criteria | Description | Achieved Outcome |
|-----------|--------------|------------------|
| Research Quality | In-depth study of design, performance, and vulnerabilities | Thorough, well-cited sources |
| Implementation & Testing | Verified AES, RSA, and SHA-256 functionality | Fully functional Python scripts |
| Analysis | Comparative analysis with graphs and metrics | Detailed performance evaluation |
| Presentation | Structured documentation and report | Clear and academically formatted |

---

## 9. Tools and Resources

- Python 3.10  
- PyCryptodome, hashlib, hmac libraries  
- Jupyter and VS Code for testing  
- Microsoft Excel for data visualization  
- References from NIST, academic textbooks, and scholarly papers

---

## 10. References

1. NIST, “Advanced Encryption Standard (AES),” FIPS PUB 197, 2001.  
2. Christof Paar and Jan Pelzl, *Understanding Cryptography*, Springer, 2010.  
3. Bruce Schneier, *Applied Cryptography*, 2nd ed., Wiley, 1996.  
4. Daniel J. Bernstein, “Cache-Timing Attacks on AES,” University of Illinois, 2005.  
5. NIST, “Secure Hash Standard (SHS),” FIPS PUB 180-4, 2015.  
6. Rivest, R., Shamir, A., and Adleman, L., “A Method for Obtaining Digital Signatures and Public-Key Cryptosystems,” *Communications of the ACM*, 1978.  
7. William Stallings, *Cryptography and Network Security: Principles and Practice*, Pearson, 2017.

---

## 11. Conclusion

This project demonstrated practical proficiency in cryptographic algorithm implementation and evaluation.  
AES, RSA, and SHA-256 collectively offer a balanced framework for secure communication systems.  
The study concluded that:
- AES is optimal for data encryption in real-time systems.  
- RSA provides strong authentication for digital communication.  
- SHA-256 ensures message integrity and is widely adopted in modern applications such as blockchain.  

These results confirm that the integration of symmetric, asymmetric, and hashing algorithms forms the foundation of reliable cybersecurity mechanisms.

