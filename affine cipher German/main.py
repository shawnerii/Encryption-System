from key_generation import generate_affine_keys
from encryption import affine_encrypt
from decryption import affine_decrypt
from brute_force import brute_force_affine

a, b = generate_affine_keys()
print(f"Generated keys: a={a}, b={b}")

plaintext = "Von den schönsten Wesen wünschen wir uns Vermehrung, Damit die Rose der Schönheit niemals sterbe, Doch wenn der Reifere durch die Zeit vergehen soll, Möge sein zarter Erbe sein Andenken tragen: Doch du, an deine eigenen hellen Augen gebunden, Nährst die Flamme deines Lichts mit eigenem Brennstoff, Machst eine Hungersnot, wo Überfluss liegt, Du selbst dein Feind, zu deinem süßen Selbst zu grausam: Du, der du nun der frische Schmuck der Welt bist, Und einziger Verkünder des prächtigen Frühlings, Vergräbst in deiner eigenen Knospe dein Glück, Und machst, geiziger Huldiger, Verschwendung durch Sparsamkeit: Erbarme dich der Welt, oder sei dieser Vielfraß, Der das Recht der Welt verschlingt, durch das Grab und dich."

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