# SafeKey

SafeKey est un gestionnaire de mots de passe local, simple, sécurisé et open source, écrit en Python. Il permet de stocker, gérer et retrouver facilement vos mots de passe, tout en assurant leur chiffrement grâce à des techniques modernes et éprouvées.

---

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exportation des données](#exportation-des-données)
- [Sécurité](#sécurité)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

---

## Fonctionnalités

- **Chiffrement fort** : Utilisation de l’algorithme Fernet (AES) et PBKDF2 pour sécuriser le coffre et les mots de passe.
- **Stockage local** : Les données sont stockées chiffrées sur votre machine, jamais en ligne.
- **Ajout, modification, suppression de mots de passe**
- **Recherche par nom ou par tag**
- **Vérification de la force du mot de passe**
- **Générateur de mots de passe robustes**
- **Export des données** au format JSON ou CSV
- **Interface en ligne de commande** simple et intuitive

---

## Installation

### 1. Pré-requis

- **Python 3.7 ou plus récent**
- **Git** (optionnel, pour cloner le projet)

### 2. Cloner le projet

```bash
git clone https://github.com/jallow-2693/SafeKey.git
cd SafeKey
```

### 3. Installer les dépendances

Assurez-vous d’avoir `pip` installé, puis lancez :

```bash
pip install -r requirements.txt
```

---

## Utilisation

Lancez le gestionnaire avec la commande suivante :

```bash
python password.py
```

### Premier lancement

- Vous serez invité à créer un **mot de passe maître** : il sert à chiffrer et déchiffrer vos données. **Ne le perdez pas !**

### Menus & Options

Après avoir entré votre mot de passe maître, vous verrez ce menu :

```
Menu
1. Ajouter un mot de passe
2. Voir les mots de passe
3. Supprimer un mot de passe
4. Modifier un mot de passe
5. Rechercher un mot de passe
6. Exporter les données
7. Quitter
```

#### 1. Ajouter un mot de passe

- Entrez le site, l’identifiant, et choisissez de générer un mot de passe fort ou d’utiliser le vôtre.
- Ajoutez des tags pour retrouver facilement le mot de passe (ex : pro, perso, email...).

#### 2. Voir les mots de passe

- Affiche la liste de tous vos mots de passe enregistrés.

#### 3. Supprimer un mot de passe

- Supprime un mot de passe d’un site spécifique.

#### 4. Modifier un mot de passe

- Modifie l’identifiant, le mot de passe ou les tags d’un site.

#### 5. Rechercher un mot de passe

- Recherche par nom de site ou par tag.

#### 6. Exporter les données

- Exportez toutes vos données en **JSON** ou en **CSV** pour les sauvegarder ou les importer ailleurs.

#### 7. Quitter

- Ferme le programme.

---

## Exportation des données

- **JSON** : Structure complète et lisible par d’autres outils.
- **CSV** : Peut être ouvert dans Excel, LibreOffice, etc.

Les fichiers exportés ne sont **pas chiffrés** : manipulez-les avec précaution !

---

## Sécurité

- **Chiffrement** : Les mots de passe sont chiffrés avec Fernet (AES), la clé est dérivée de votre mot de passe maître via PBKDF2 et un salt aléatoire.
- **Local uniquement** : Aucun envoi en ligne, tout reste sur votre disque.
- **Attention** : Ce gestionnaire est destiné à un usage personnel et local. Pour un usage professionnel ou critique, un audit sécurité approfondi est recommandé.

---

## Contribution

Les contributions sont les bienvenues !

### Comment contribuer

1. Forkez ce dépôt
2. Créez une branche (`git checkout -b ma-feature`)
3. Faites vos modifications (+ tests si possible)
4. Envoyez une pull request 🚀

### Suggestions d'améliorations

- Ajout de tests unitaires
- Interface graphique (Tkinter, PyQt, etc.)
- Prise en charge de plusieurs coffres
- Synchronisation optionnelle (cloud/local réseau)
- Meilleur masquage des mots de passe à l’affichage
- Support multilingue

### Bonnes pratiques

- Respectez le style du code existant (PEP8).
- Expliquez vos changements dans la PR.
- Soyez bienveillant dans vos échanges !

---

## Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Contact

Pour toute question, suggestion ou signalement de bug, ouvrez une **issue** sur GitHub ou contactez-moi :  
[github.com/jallow-2693](https://github.com/jallow-2693)

---

**Bon usage et merci pour vos contributions !** 🗝️
