

def affine_encrypt(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext.upper():
        if char.isalpha(): 
            x = ord(char) - ord('A')
            encrypted_char = (a * x + b) % 26
            encrypted_text += chr(encrypted_char + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text


if __name__ == "__main__":
    sample_text = "Von den schönsten Wesen wünschen wir uns Vermehrung, Damit die Rose der Schönheit niemals sterbe, Doch wenn der Reifere durch die Zeit vergehen soll, Möge sein zarter Erbe sein Andenken tragen: Doch du, an deine eigenen hellen Augen gebunden, Nährst die Flamme deines Lichts mit eigenem Brennstoff, Machst eine Hungersnot, wo Überfluss liegt, Du selbst dein Feind, zu deinem süßen Selbst zu grausam: Du, der du nun der frische Schmuck der Welt bist, Und einziger Verkünder des prächtigen Frühlings, Vergräbst in deiner eigenen Knospe dein Glück, Und machst, geiziger Huldiger, Verschwendung durch Sparsamkeit: Erbarme dich der Welt, oder sei dieser Vielfraß, Der das Recht der Welt verschlingt, durch das Grab und dich. Wenn vierzig Winter deine Stirn belagern werden, Und tiefe Gräben in das Feld deiner Schönheit graben, Das stolze Gewand deiner Jugend, jetzt so bewundert, Wird ein zerlumpter Rest von geringem Wert sein: Dann, gefragt, wo all deine Schönheit geblieben ist, Wo all der Schatz deiner lebhaften Tage; Zu sagen, in deinen tief versunkenen Augen, Wäre eine allesverzehrende Schande und unfruchtbarer Ruhm."
    a, b = 6, 1  # Example keys
    encrypted = affine_encrypt(sample_text, a, b)
    print(f"Ciphertext: {encrypted}")