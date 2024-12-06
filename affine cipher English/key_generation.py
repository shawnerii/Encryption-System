

import random
import math

def generate_affine_keys():
    while True:
        a = random.randint(1, 25)
        if math.gcd(a, 26) == 1:
            break
    b = random.randint(0, 25)
    return a, b

if __name__ == "__main__":
    a, b = generate_affine_keys()
    print(f"Generated keys: a={a}, b={b}")