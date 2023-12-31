import socket
from datetime import datetime

def domaine_vers_ip(nom_domaine):
    try:
        adresse_ip = socket.gethostbyname(nom_domaine)
        return adresse_ip
    except socket.error as e:
        return f"Erreur : {e}"

if __name__ == "__main__":
    fichier_entree = input("Entrez le nom du fichier texte contenant la liste de domaines : ")

    try:
        with open(fichier_entree, 'r') as file:
            domaines = file.readlines()
    except FileNotFoundError:
        print(f"Le fichier {fichier_entree} n'a pas été trouvé.")
        exit()

    date_du_jour = datetime.now().strftime("%Y%m%d_%H%M%S")
    fichier_sortie = f"IP_{date_du_jour}.txt"

    with open(fichier_sortie, 'w') as output_file:
        for domaine in domaines:
            domaine = domaine.strip()
            ip = domaine_vers_ip(domaine)
            if not ip.startswith("Erreur"):
                ligne_resultat = f"{ip}\n"
                print(ligne_resultat)
                output_file.write(ligne_resultat)

    print(f"Les résultats ont été enregistrés dans {fichier_sortie}.")
