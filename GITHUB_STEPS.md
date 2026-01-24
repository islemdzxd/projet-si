# Mettre le projet TransportPro sur GitHub — étape par étape

---

## Prérequis

- **Git** installé sur ton PC : [https://git-scm.com/download/win](https://git-scm.com/download/win)  
  Vérifier : ouvrir PowerShell et taper `git --version`. Si une version s’affiche, c’est bon.

- **Compte GitHub** : [https://github.com](https://github.com) — créé et connecté.

---

## Étape 1 — Ouvrir le bon dossier

1. Ouvre **PowerShell** ou **Invite de commandes**.
2. Va dans le dossier de ton projet (racine, où se trouvent `README.md`, `MANUEL_UTILISATION.md` et le dossier `transport_delivery`) :

```powershell
cd C:\Users\lenovo\Downloads\transport_delivery
```

*(Si ton projet est ailleurs, remplace le chemin.)*

---

## Étape 2 — Vérifier qu’il n’y a pas déjà un dépôt Git

Tape :

```powershell
git status
```

- Si tu vois **« not a git repository »** → passe à l’étape 3.  
- Si `git status` affiche des fichiers → un dépôt Git existe déjà : tu peux aller à l’**Étape 5** (créer le dépôt sur GitHub et pousser).

---

## Étape 3 — Initialiser le dépôt Git

```powershell
git init
```

Tu dois voir : `Initialized empty Git repository in ...`

---

## Étape 4 — Ajouter tous les fichiers et faire un premier commit

```powershell
git add .
git commit -m "TransportPro - Projet initial"
```

Le `.` après `git add` signifie « tous les fichiers du dossier ».  
Le fichier `.gitignore` à la racine évite d’ajouter `__pycache__`, `venv`, `node_modules`, etc.

---

## Étape 5 — Créer le dépôt sur GitHub

1. Va sur **https://github.com** et connecte-toi.
2. Clique sur le **+** en haut à droite → **New repository**.
3. Renseigne :
   - **Repository name :** `transport_delivery` (ou un autre nom, par ex. `transport-pro`).
   - **Description :** (optionnel) *Gestion des livraisons - Django + React*.
   - **Public**.
   - Ne coche **pas** « Add a README », **pas** « Add .gitignore », **pas** « Choose a license ».
4. Clique sur **Create repository**.

---

## Étape 6 — Relier ton dossier au dépôt GitHub

Sur la page du dépôt créé, GitHub affiche des commandes. Tu peux utiliser celles-ci (en remplaçant `VOTRE_USERNAME` par ton identifiant GitHub et `transport_delivery` par le nom du dépôt si différent) :

```powershell
git remote add origin https://github.com/VOTRE_USERNAME/transport_delivery.git
git branch -M main
git push -u origin main
```

**Exemple** si ton compte est `dupont` et le dépôt `transport_delivery` :

```powershell
git remote add origin https://github.com/dupont/transport_delivery.git
git branch -M main
git push -u origin main
```

- Si on te demande **utilisateur** et **mot de passe** :  
  - Utilisateur = ton identifiant GitHub.  
  - Mot de passe = un **Personal Access Token** (plus possible d’utiliser l’ancien mot de passe du compte).  
    → [https://github.com/settings/tokens](https://github.com/settings/tokens) : *Generate new token (classic)*, coche au moins `repo`, génère, copie le token et colle-le quand Git demande le mot de passe.

---

## Étape 7 — Vérifier sur GitHub

Ouvre `https://github.com/VOTRE_USERNAME/transport_delivery` dans ton navigateur.  
Tu dois voir : `README.md`, `MANUEL_UTILISATION.md`, le dossier `transport_delivery/`, etc.

---

## Dépannage rapide

| Problème | Piste de solution |
|----------|-------------------|
| `git` inconnu | Installer Git : [https://git-scm.com/download/win](https://git-scm.com/download/win) |
| `remote origin already exists` | `git remote remove origin` puis refaire `git remote add origin ...` |
| Erreur d’authentification au `git push` | Utiliser un **Personal Access Token** comme mot de passe, pas le mot de passe du compte |
| « Failed to push » / « Permission denied » | Vérifier que le dépôt existe et que l’URL `origin` est correcte : `git remote -v` |

---

## Plus tard : enregistrer d’autres changements

Après avoir modifié des fichiers :

```powershell
cd C:\Users\lenovo\Downloads\transport_delivery
git add .
git commit -m "Description de tes changements"
git push
```
