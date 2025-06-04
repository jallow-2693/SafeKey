import os
import json
import base64
import csv
import getpass
import secrets
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def generate_key_from_password(password: bytes, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password))


def save_salt(salt, filename="salt.bin"):
    with open(filename, "wb") as f:
        f.write(salt)


def load_salt(filename="salt.bin"):
    with open(filename, "rb") as f:
        return f.read()


def save_vault(data: dict, key: bytes, filename="vault.enc"):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(filename, "wb") as f:
        f.write(encrypted)


def load_vault(key: bytes, filename="vault.enc") -> dict:
    if not os.path.exists(filename):
        print("Coffre initialisé.")
        return {}
    try:
        with open(filename, "rb") as f:
            encrypted_data = f.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())
    except Exception:
        print("Erreur : mot de passe incorrect ou fichier corrompu.")
        exit()


def check_password_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])
    if length >= 12 and score == 4:
        return "fort"
    elif length >= 8 and score >= 3:
        return "moyen"
    else:
        return "faible"


def generate_strong_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))


def add_password(vault: dict):
    site = input("Nom du site : ").strip()
    username = input("Nom d'utilisateur : ").strip()
    choice = input("Générer un mot de passe aléatoire ? (o/n) : ").strip().lower()

    if choice == "o":
        password = generate_strong_password()
        print(f"Mot de passe généré : {password}")
    else:
        password = getpass.getpass("Mot de passe : ").strip()

    strength = check_password_strength(password)
    print(f"Force du mot de passe : {strength}")

    tags = input("Tags (séparés par des virgules, ex: pro,email) : ").strip().lower().split(',')

    vault[site] = {
        "username": username,
        "password": password,
        "tags": [tag.strip() for tag in tags if tag.strip()]
    }

    print(f"Mot de passe pour {site} ajouté.")


def show_passwords(vault: dict):
    if not vault:
        print("Aucun mot de passe enregistré.")
        return
    print("\nMots de passe enregistrés :")
    for site, creds in vault.items():
        tags = ", ".join(creds.get("tags", []))
        print(f"{site} : {creds['username']} / {creds['password']} (Tags : {tags})")


def delete_password(vault: dict):
    site = input("Nom du site à supprimer : ").strip()
    if site in vault:
        del vault[site]
        print(f"Mot de passe pour {site} supprimé.")
    else:
        print("Site non trouvé.")


def modify_password(vault: dict):
    site = input("Nom du site à modifier : ").strip()
    if site not in vault:
        print("Site non trouvé.")
        return

    creds = vault[site]
    print(f"Identifiant actuel : {creds['username']}")
    new_username = input("Nouveau nom d'utilisateur (laisser vide pour conserver) : ").strip()
    if new_username:
        creds["username"] = new_username

    change_pwd = input("Modifier le mot de passe ? (o/n) : ").strip().lower()
    if change_pwd == "o":
        password = getpass.getpass("Nouveau mot de passe : ").strip()
        strength = check_password_strength(password)
        print(f"Force du mot de passe : {strength}")
        creds["password"] = password

    new_tags = input("Nouveaux tags (laisser vide pour conserver) : ").strip().lower()
    if new_tags:
        creds["tags"] = [tag.strip() for tag in new_tags.split(',') if tag.strip()]

    print(f"Mot de passe pour {site} modifié.")
    vault[site] = creds


def search_password(vault: dict):
    search_term = input("Recherche par nom ou tag : ").strip().lower()
    found = False
    for site, creds in vault.items():
        if search_term in site.lower() or search_term in [tag.lower() for tag in creds.get("tags", [])]:
            tags = ", ".join(creds.get("tags", []))
            print(f"{site} : {creds['username']} / {creds['password']} (Tags : {tags})")
            found = True
    if not found:
        print("Aucun résultat.")


def export_data(vault: dict):
    if not vault:
        print("Aucune donnée à exporter.")
        return

    format_choice = input("Format d'export (json/csv) : ").strip().lower()
    if format_choice == "json":
        with open("export.json", "w") as f:
            json.dump(vault, f, indent=4)
        print("Données exportées vers export.json")
    elif format_choice == "csv":
        with open("export.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["site", "username", "password", "tags"])
            for site, creds in vault.items():
                writer.writerow([site, creds["username"], creds["password"], ",".join(creds.get("tags", []))])
        print("Données exportées vers export.csv")
    else:
        print("Format non pris en charge.")


def main():
    if os.path.exists("salt.bin"):
        salt = load_salt()
        password = getpass.getpass("Entrez votre mot de passe maître : ").encode()
        key = generate_key_from_password(password, salt)
    else:
        password = getpass.getpass("Créez un mot de passe maître : ").encode()
        salt = os.urandom(16)
        key = generate_key_from_password(password, salt)
        save_salt(salt)
        save_vault({}, key)
        print("Coffre initialisé avec succès.")
        return

    vault = load_vault(key)
    print("Coffre chargé avec succès.")

    while True:
        print("\nMenu")
        print("1. Ajouter un mot de passe")
        print("2. Voir les mots de passe")
        print("3. Supprimer un mot de passe")
        print("4. Modifier un mot de passe")
        print("5. Rechercher un mot de passe")
        print("6. Exporter les données")
        print("7. Quitter")

        choice = input("Choix : ").strip()

        if choice == "1":
            add_password(vault)
            save_vault(vault, key)
        elif choice == "2":
            show_passwords(vault)
        elif choice == "3":
            delete_password(vault)
            save_vault(vault, key)
        elif choice == "4":
            modify_password(vault)
            save_vault(vault, key)
        elif choice == "5":
            search_password(vault)
        elif choice == "6":
            export_data(vault)
        elif choice == "7":
            print("Fermeture du gestionnaire.")
            break
        else:
            print("Option invalide.")


if __name__ == "__main__":
    main()
