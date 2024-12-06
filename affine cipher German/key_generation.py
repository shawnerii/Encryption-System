import random
import math

def generate_affine_keys():
    m = 30
    while True:
        a = random.randint(1, m - 1)
        if math.gcd(a, m) == 1:
            break
    b = random.randint(0, m - 1)
    return a, b

if __name__ == "__main__":
    a, b = generate_affine_keys()
    print(f"Generated keys for German alphabet: a={a}, b={b}")

