import hashlib
import time


def get_hash(password: str) -> str:
    """Warning HL101: MD5, SHA-1, RIPEMD-160, Whirlpool, and the SHA-256 / SHA-512 hash algorithms are all
    vulnerable to length-extension attacks and should not be used for obfuscating or protecting data. Use within
    a HMAC is not vulnerable. (From: Hashlib Documentation)."""
    return hashlib.sha256(password.encode()).hexdigest()


file_dictionnaire = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/dico.txt")  # On ouvre le dictionnaire, qu'on met dans une variable
dictionnaire = file_dictionnaire.read()  # On lit son contenu
dictionnaire = dictionnaire.splitlines()  # On met un retour à la ligne à chaque ligne

file_hash1 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash1.txt")  # Y compris pour les hashs
hash1 = file_hash1.read()

file_hash2 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash2.txt")
hash2 = file_hash2.read()

file_hash3 = open("C:/Users/Patrick/Documents/Cours/Cyber/MyJohnCracker/hash3.txt")
hash3 = file_hash3.read()


def search(dico, hash):  # Fonction search prend en compte 2 paramètres : Un dictionnaire et un hash
    i = 0 # Variable i qui va servir de repère dans les lignes
    while get_hash(dico[i]) != hash and  i < len(dico): # le get_hash(dico[i]) signifie qu'on hashe le mot de passe de chaque ligne. Tant qu'il n'a pas été trouvé, on continue de lire le dictionnaire.
        i+=1 # Lire la ligne suivante
    if i >= len(dico): # Si i est supérieur ou égal (normalement égal, mais c'est pour que le else comprenne que i doit être inférieur) à la longueur du dico, ça signifie que i a parcouru l'intégralité du dictionnaire sans trouver le hash correspondant
        print("Non trouvé") # Il ne l'a donc pas trouvé
    else: # Mais si i est inférieur à la longueur du dico, cela signifie qu'il s'est arrêté lorsqu'il a trouvé le bon mot de passe hashé. Il a donc dans sa mémoire la ligne qui correspond au mot de passe du hash, une ligne inférieure au nombre de lignes du dico
        print("Trouvé ", dico[i]) # Il l'a trouvé et il donne le mot de passe du dico en prenant comme paramètre la ligne où il se situe
    print(f'{"non " * (i >= len(dico))}trouvé') # Version branchless


search(dictionnaire, hash1)
search(dictionnaire, hash2)
search(dictionnaire, hash3)

file_hash1.close()
file_hash2.close()
file_hash3.close()
file_dictionnaire.close()
