

def affine_decrypt(ciphertext, a, b):
    decrypted_text = ""
    a_inv = pow(a, -1, 26)
    for char in ciphertext.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            decrypted_char = (a_inv * (y - b)) % 26
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == "__main__":
    sample_ciphertext = "BSN PUN MKJRNMRUN GUMUN GVNMKJUN GOH WNM BUHIUJHWNE, PAIOR POU HSMU PUH MKJRNJUOR NOUIADM MRUHFU, PSKJ GUNN PUH HUOZUHU PWHKJ POU VUOR BUHEUJUN MSDD, IREU MUON VAHRUH UHFU MUON ANPUNYUN RHAEUN: PSKJ PW, AN PUONU UOEUNUN JUDDUN AWEUN EUFWNPUN, NFJHMR POU ZDAIIU PUONUM DOKJRM IOR UOEUNUI FHUNNMRSZZ, IAKJMR UONU JWNEUHMNSR, GS VFUHZDWMM DOUER, PW MUDFMR PUON ZUONP, VW PUONUI MVMMUN MUDFMR VW EHAWMAI: PW, PUH PW NWN PUH ZHOMKJU MKJIWKY PUH GUDR FOMR, WNP UONVOEUH BUHYVNPUH PUM XHFKJROEUN ZHVJDONEM, BUHEHFFMR ON PUONUH UOEUNUN YNSMXU PUON EDVKY, WNP IAKJMR, EUOVOEUH JWDPOEUH, BUHMKJGUNPWNE PWHKJ MXAHMAIYUOR: UHFAHIU POKJ PUH GUDR, SPUH MUO POUMUH BOUDZHAMM, PUH PAM HUKJR PUH GUDR BUHMKJDONER, PWHKJ PAM EHAF WNP POKJ. GUNN BOUHVOE GONRUH PUONU MROHN FUDAEUHN GUHPUN, WNP ROUZU EHFFUN ON PAM ZUDP PUONUH MKJRNJUOR EHAFUN, PAM MRSDVU EUGANP PUONUH TWEUNP, TURVR MS FUGWNPUHR, GOHP UON VUHDWIXRUH HUMR BSN EUHONEUI GUHR MUON: PANN, EUZHAER, GS ADD PUONU MKJRNJUOR EUFDOUFUN OMR, GS ADD PUH MKJARV PUONUH DUFJAZRUN RAEU; VW MAEUN, ON PUONUN ROUZ BUHMWNYUNUN AWEUN, GFHU UONU ADDUMBUHVUJHUNPU MKJANPU WNP WNZHWKJRFAHUH HWJI."
    a, b = 5, 0 
    decrypted = affine_decrypt(sample_ciphertext, a, b)
    print(f"Decrypted text: {decrypted}")