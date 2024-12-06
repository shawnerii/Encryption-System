Affine Cipher Implementation, Encryption, Decryption, and Hacking in Python

The Affine Cipher encryption and decryption formulas are:
• Encryption: E(x) = (a * x + b) mod 26
• Decryption: D(y) = a^(-1) * (y - b) mod 26
where:
• x is the position of the plaintext letter,
• y is the position of the ciphertext letter,
• a and b are constants, and a must be coprime with 26 for a modular inverse to exist.

Important note before running the affine cipher: since the folder “affine cipher” is in the same
directory as “affine cipher German” and the name of the python text files are similar when
running the main.py there might be some errors, changing the path of one folder so that they
do not have the same directory would solve the issue.
