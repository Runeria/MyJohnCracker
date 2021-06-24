import hashlib
import time


def get_hash(password: str) -> str:
    """Warning HL101: MD5, SHA-1, RIPEMD-160, Whirlpool, and the SHA-256 / SHA-512 hash algorithms are all
    vulnerable to length-extension attacks and should not be used for obfuscating or protecting data. Use within
    a HMAC is not vulnerable. (From: Hashlib Documentation)."""
    return hashlib.sha256(password.encode()).hexdigest()


file_dictionnaire = open(
    "C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/dico.txt")  # On ouvre le dictionnaire, qu'on met dans une variable
dictionnaire = file_dictionnaire.read()  # On lit son contenu
dictionnaire = dictionnaire.splitlines()  # On met un retour à la ligne à chaque ligne

file_hash1 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash1.txt")  # Y compris pour les hashs
hash1 = file_hash1.read()
hash1 = hash1.splitlines()

file_hash2 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash2.txt")
hash2 = file_hash2.read()
hash2 = hash2.splitlines()

file_hash3 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash3.txt")
hash3 = file_hash3.read()
hash3 = hash3.splitlines()


def search(dico, hash):
    i = 0
    while i < len(dico) and get_hash(dico[i]) != hash:
        i+=1
    if i > len(dico):
        print("Non trouvé")
    else:
        print("Trouvé")


search(dictionnaire, hash1)
search(dictionnaire, hash2)
search(dictionnaire, hash3)

file_hash1.close()
file_hash2.close()
file_hash3.close()
file_dictionnaire.close()
