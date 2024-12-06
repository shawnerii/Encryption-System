import math
import time
from decryption import affine_decrypt

def brute_force_affine(ciphertext):
    start_time = time.time()
    common_words = ["THE", "AND", "OF", "TO", "A", "IN", "THAT", "IS", "IT", "AS", "OR" , "SO", "THEN"]

    for a in range(1, 26):
        if math.gcd(a, 26) == 1:
            for b in range(26):
                decrypted_text = affine_decrypt(ciphertext, a, b)              
                match_count = sum(1 for word in common_words if word in decrypted_text)
                if match_count >= 10:
                    end_time = time.time()
                    time_taken = end_time - start_time
                    return {
                        "a": a,
                        "b": b,
                        "decrypted_text": decrypted_text,
                        "time_taken": time_taken
                    }
    return None

if __name__ == "__main__":
    sample_ciphertext = "ZHSI ZAOHUMR KHUARWHUM GU PUMOHU ONKHUAMU, RJAR RJUHUFQ FUAWRQ'M HSMU IOEJR NUBUH POU, FWR AM RJU HOXUH MJSWDP FQ ROIU PUKUAMU, JOM RUNPUH JUOH IOEJR FUAH JOM IUISHQ: FWR RJSW KSNRHAKRUP RS RJONU SGN FHOEJR UQUM, ZUUP'MR RJQ DOEJR'M ZDAIU GORJ MUDZ-MWFMRANROAD ZWUD, IAYONE A ZAIONU GJUHU AFWNPANKU DOUM, RJQ MUDZ RJQ ZSU, RS RJQ MGUUR MUDZ RSS KHWUD: RJSW RJAR AHR NSG RJU GSHDP'M ZHUMJ SHNAIUNR, ANP SNDQ JUHADP RS RJU EAWPQ MXHONE, GORJON RJONU SGN FWP FWHOUMR RJQ KSNRUNR, ANP RUNPUH KJWHD IAY'MR GAMRU ON NOEEAHPONE: XORQ RJU GSHDP, SH UDMU RJOM EDWRRSN FU, RS UAR RJU GSHDP'M PWU, FQ RJU EHABU ANP RJUU. GJUN ZSHRQ GONRUHM MJADD FUMOUEU RJQ FHSG, ANP POE PUUX RHUNKJUM ON RJQ FUAWRQ'M ZOUDP, RJQ QSWRJ'M XHSWP DOBUHQ MS EAVUP SN NSG, GODD FU A RARRUHUP GUUP SZ MIADD GSHRJ JUDP: RJUN FUONE AMYUP, GJUHU ADD RJQ FUAWRQ DOUM, GJUHU ADD RJU RHUAMWHU SZ RJQ DWMRQ PAQM; RS MAQ GORJON RJONU SGN PUUX MWNYUN UQUM, GUHU AN ADD-UARONE MJAIU, ANP RJHOZRDUMM XHAOMU."
    result = brute_force_affine(sample_ciphertext)
    if result:
        print(f"Found plaintext: {result['decrypted_text']}")
        print(f"Keys: a={result['a']}, b={result['b']}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")
    else:
        print("No valid decryption found.")