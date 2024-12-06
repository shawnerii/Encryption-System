import math
import time
from decryption import affine_decrypt

def brute_force_affine(ciphertext):
    start_time = time.time()
    common_words = ["DER", "DIE", "UND", "IN", "ZU", "MIT", "AUF", "IST", "DES", "SIE", "VON", "NICHT", "DAS"]

    m = 30
    for a in range(1, m):
        if math.gcd(a, m) == 1:
            for b in range(m):
                decrypted_text = affine_decrypt(ciphertext, a, b)
                match_count = sum(1 for word in common_words if word in decrypted_text)
                if match_count >= 5:
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

    sample_ciphertext = "CNG ÄDG LTYOGLSDG JDLDG JVGLTYDG JBE ZGL CDEßDYEZGR, ÄFßBS ÄBD ENLD ÄDE LTYOGYDBS GBDßFWL LSDEMD, ÄNTY JDGG ÄDE EDBKDED ÄZETY ÄBD ADBS CDERDYDG LNWW, ßORD LDBG AFESDE DEMD LDBG FGÄDGPDG SEFRDG: ÄNTY ÄZ, FG ÄDBGD DBRDGDG YDWWDG FZRDG RDMZGÄDG, GHYELS ÄBD KWFßßD ÄDBGDL WBTYSL ßBS DBRDGDß MEDGGLSNKK, ßFTYLS DBGD YZGRDELGNS, JN VMDEKWZLL WBDRS, ÄZ LDWMLS ÄDBG KDBGÄ, AZ ÄDBGDß LVLLDG LDWMLS AZ REFZLFß: ÄZ, ÄDE ÄZ GZG ÄDE KEBLTYD LTYßZTP ÄDE JDWS MBLS, ZGÄ DBGABRDE CDEPVGÄDE ÄDL UEHTYSBRDG KEVYWBGRL, CDEREHMLS BG ÄDBGDE DBRDGDG PGNLUD ÄDBG RWVTP, ZGÄ ßFTYLS, RDBABRDE YZWÄBRDE, CDELTYJDGÄZGR ÄZETY LUFELFßPDBS: DEMFEßD ÄBTY ÄDE JDWS, NÄDE LDB ÄBDLDE CBDWKEFLL, ÄDE ÄFL EDTYS ÄDE JDWS CDELTYWBGRS, ÄZETY ÄFL REFM ZGÄ ÄBTY. JDGG CBDEABR JBGSDE ÄDBGD LSBEG MDWFRDEG JDEÄDG, ZGÄ SBDKD REHMDG BG ÄFL KDWÄ ÄDBGDE LTYOGYDBS REFMDG, ÄFL LSNWAD RDJFGÄ ÄDBGDE IZRDGÄ, IDSAS LN MDJZGÄDES, JBEÄ DBG ADEWZßUSDE EDLS CNG RDEBGRDß JDES LDBG: ÄFGG, RDKEFRS, JN FWW ÄDBGD LTYOGYDBS RDMWBDMDG BLS, JN FWW ÄDE LTYFSA ÄDBGDE WDMYFKSDG SFRD; AZ LFRDG, BG ÄDBGDG SBDK CDELZGPDGDG FZRDG, JHED DBGD FWWDLCDEADYEDGÄD LTYFGÄD ZGÄ ZGKEZTYSMFEDE EZYß."
    result = brute_force_affine(sample_ciphertext)
    if result:
        print(f"Found plaintext: {result['decrypted_text']}")
        print(f"Keys: a={result['a']}, b={result['b']}")
        print(f"Time taken: {result['time_taken']:.4f} seconds")
    else:
        print("No valid decryption found.")