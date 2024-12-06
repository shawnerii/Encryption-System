def affine_encrypt(plaintext, a, b):
    german_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß"
    m = len(german_alphabet) 
    encrypted_text = ""

    for char in plaintext.upper():
        if char in german_alphabet:
            x = german_alphabet.index(char)
            encrypted_char = (a * x + b) % m
            encrypted_text += german_alphabet[encrypted_char]
        else:
            encrypted_text += char
    return encrypted_text
if __name__ == "__main__":
    sample_text = "Von den schönsten Wesen wünschen wir uns Vermehrung, Damit die Rose der Schönheit niemals sterbe, Doch wenn der Reifere durch die Zeit vergehen soll, Möge sein zarter Erbe sein Andenken tragen: Doch du, an deine eigenen hellen Augen gebunden, Nährst die Flamme deines Lichts mit eigenem Brennstoff, Machst eine Hungersnot, wo Überfluss liegt, Du selbst dein Feind, zu deinem süßen Selbst zu grausam: Du, der du nun der frische Schmuck der Welt bist, Und einziger Verkünder des prächtigen Frühlings, Vergräbst in deiner eigenen Knospe dein Glück, Und machst, geiziger Huldiger, Verschwendung durch Sparsamkeit: Erbarme dich der Welt, oder sei dieser Vielfraß, Der das Recht der Welt verschlingt, durch das Grab und dich. Wenn vierzig Winter deine Stirn belagern werden, Und tiefe Gräben in das Feld deiner Schönheit graben, Das stolze Gewand deiner Jugend, jetzt so bewundert, Wird ein zerlumpter Rest von geringem Wert sein: Dann, gefragt, wo all deine Schönheit geblieben ist, Wo all der Schatz deiner lebhaften Tage; Zu sagen, in deinen tief versunkenen Augen, Wäre eine allesverzehrende Schande und unfruchtbarer Ruhm."
    a, b = 7, 5
    encrypted = affine_encrypt(sample_text, a, b)
    print(f"Ciphertext: {encrypted}")