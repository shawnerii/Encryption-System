def affine_decrypt(ciphertext, a, b):
    german_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"
    m = len(german_alphabet)
    decrypted_text = ""
    a_inv = pow(a, -1, m)

    for char in ciphertext.upper():
        if char in german_alphabet:
            y = german_alphabet.index(char)
            decrypted_char = (a_inv * (y - b) % m)
            decrypted_text += german_alphabet[decrypted_char]
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    sample_ciphertext = "CNG ÄDG LTYOGLSDG JDLDG JVGLTYDG JBE ZGL CDEßDYEZGR, ÄFßBS ÄBD ENLD ÄDE LTYOGYDBS GBDßFWL LSDEMD, ÄNTY JDGG ÄDE EDBKDED ÄZETY ÄBD ADBS CDERDYDG LNWW, ßORD LDBG AFESDE DEMD LDBG FGÄDGPDG SEFRDG: ÄNTY ÄZ, FG ÄDBGD DBRDGDG YDWWDG FZRDG RDMZGÄDG, GHYELS ÄBD KWFßßD ÄDBGDL WBTYSL ßBS DBRDGDß MEDGGLSNKK, ßFTYLS DBGD YZGRDELGNS, JN VMDEKWZLL WBDRS, ÄZ LDWMLS ÄDBG KDBGÄ, AZ ÄDBGDß LVLLDG LDWMLS AZ REFZLFß: ÄZ, ÄDE ÄZ GZG ÄDE KEBLTYD LTYßZTP ÄDE JDWS MBLS, ZGÄ DBGABRDE CDEPVGÄDE ÄDL UEHTYSBRDG KEVYWBGRL, CDEREHMLS BG ÄDBGDE DBRDGDG PGNLUD ÄDBG RWVTP, ZGÄ ßFTYLS, RDBABRDE YZWÄBRDE, CDELTYJDGÄZGR ÄZETY LUFELFßPDBS: DEMFEßD ÄBTY ÄDE JDWS, NÄDE LDB ÄBDLDE CBDWKEFLL, ÄDE ÄFL EDTYS ÄDE JDWS CDELTYWBGRS, ÄZETY ÄFL REFM ZGÄ ÄBTY. JDGG CBDEABR JBGSDE ÄDBGD LSBEG MDWFRDEG JDEÄDG, ZGÄ SBDKD REHMDG BG ÄFL KDWÄ ÄDBGDE LTYOGYDBS REFMDG, ÄFL LSNWAD RDJFGÄ ÄDBGDE IZRDGÄ, IDSAS LN MDJZGÄDES, JBEÄ DBG ADEWZßUSDE EDLS CNG RDEBGRDß JDES LDBG: ÄFGG, RDKEFRS, JN FWW ÄDBGD LTYOGYDBS RDMWBDMDG BLS, JN FWW ÄDE LTYFSA ÄDBGDE WDMYFKSDG SFRD; AZ LFRDG, BG ÄDBGDG SBDK CDELZGPDGDG FZRDG, JHED DBGD FWWDLCDEADYEDGÄD LTYFGÄD ZGÄ ZGKEZTYSMFEDE EZYß."
    a, b = 7, 5
    decrypted = affine_decrypt(sample_ciphertext, a, b)
    print(f"Decrypted text: {decrypted}")