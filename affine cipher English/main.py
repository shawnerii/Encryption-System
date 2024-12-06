from key_generation import generate_affine_keys
from encryption import affine_encrypt
from decryption import affine_decrypt
from brute_force import brute_force_affine

a, b = generate_affine_keys()
print(f"Generated keys: a={a}, b={b}")

plaintext = "From fairest creatures we desire increase, That thereby beauty's rose might never die, But as the riper should by time decease, His tender heir might bear his memory: But thou contracted to thine own bright eyes, Feed'st thy light's flame with self-substantial fuel, Making a famine where abundance lies, Thy self thy foe, to thy sweet self too cruel: Thou that art now the world's fresh ornament, And only herald to the gaudy spring, Within thine own bud buriest thy content, And tender churl mak'st waste in niggarding: Pity the world, or else this glutton be, To eat the world's due, by the grave and thee. When forty winters shall besiege thy brow, And dig deep trenches in thy beauty's field, Thy youth's proud livery so gazed on now, Will be a tattered weed of small worth held: Then being asked, where all thy beauty lies, Where all the treasure of thy lusty days; To say within thine own deep sunken eyes, Were an all-eating shame, and thriftless praise."
ciphertext = affine_encrypt(plaintext, a, b)
print(f"Ciphertext: {ciphertext}")

decrypted_text = affine_decrypt(ciphertext, a, b)
print(f"Decrypted text: {decrypted_text}")

print("\nBrute-forcing the ciphertext:")
result = brute_force_affine(ciphertext)
if result:
    print(f"Found plaintext: {result['decrypted_text']}")
    print(f"Keys: a={result['a']}, b={result['b']}")
    print(f"Time taken: {result['time_taken']:.4f} seconds")
else:
    print("No valid decryption found.")