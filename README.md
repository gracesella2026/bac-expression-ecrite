# Expression écrite — bac de FLE

Application d'entraînement à l'épreuve écrite de français, niveau 5 unités :
description d'une photo (80 mots, cinq mots imposés, quatre critères) et
question de réflexion ou de créativité.

20 thèmes, 3 photos par thème, avec pour chaque thème les cinq mots imposés,
les deux sujets, les trois descriptions annotées et les deux textes modèles.

L'application ne demande aucun compte, n'enregistre rien et ne fait aucun appel
réseau : tout se passe dans le navigateur de l'élève. La remise se fait par
Google Classroom (bouton **Copier**, puis coller dans le devoir).

## Contenu du dépôt

```
prepa-bac-ecrit/
├── streamlit_app.py        ← le fichier que Streamlit exécute
├── requirements.txt        ← les bibliothèques à installer
├── README.md
├── .gitattributes
├── .streamlit/
│   └── config.toml         ← thème et service des fichiers statiques
└── static/
    └── expression-ecrite-eleves.html   ← l'application (≈ 3 Mo, photos comprises)
```

Le fichier HTML est autonome : les 60 photos sont à l'intérieur. Il n'y a donc
aucun dossier d'images à envoyer à côté.

## Publier sur GitHub

1. Sur GitHub, créer un dépôt, par exemple `prepa-bac-ecrit`, **public**
   (Streamlit Community Cloud ne lit pas les dépôts privés dans l'offre gratuite).
2. Bouton **Add file → Upload files**, puis glisser le contenu de ce dossier.
   Attention : glisser *les fichiers et les dossiers*, pas le dossier
   `prepa-bac-ecrit` lui-même, sinon `streamlit_app.py` se retrouvera dans un
   sous-dossier et Streamlit ne le trouvera pas.
3. **Commit changes**.

Le dossier `.streamlit` commence par un point : certains navigateurs le
masquent. S'il n'apparaît pas après l'envoi, le créer à la main avec
**Add file → Create new file**, en tapant `.streamlit/config.toml` comme nom.

## Publier sur Streamlit

1. Aller sur https://share.streamlit.io et se connecter avec le compte GitHub.
2. **Create app → Deploy a public app from GitHub**.
3. Renseigner : dépôt `votre-compte/prepa-bac-ecrit`, branche `main`,
   fichier principal `streamlit_app.py`.
4. **Deploy**. La première mise en ligne prend deux à trois minutes.

L'adresse obtenue (`https://…streamlit.app`) est celle à donner aux élèves.

### Deux choses à savoir

- Une application Streamlit gratuite **se met en veille** après quelques jours
  sans visite. Le premier élève qui ouvre le lien doit alors cliquer sur un
  bouton de réveil et attendre une minute. Ouvrir le lien avant le cours évite
  la mauvaise surprise.
- L'application est affichée dans un cadre. Si l'affichage est trop étroit sur
  un téléphone, le lien en bas de page ouvre le fichier en plein écran, à
  l'adresse `…streamlit.app/app/static/expression-ecrite-eleves.html`.

## Autre solution : GitHub Pages

Comme l'application est un simple fichier HTML, elle peut être hébergée sans
Python, sans veille et sans cadre :

1. Créer un dépôt public.
2. Y envoyer le fichier `expression-ecrite-eleves.html` **renommé `index.html`**,
   à la racine.
3. **Settings → Pages → Source : Deploy from a branch**, branche `main`,
   dossier `/ (root)`, puis **Save**.

L'adresse `https://votre-compte.github.io/nom-du-depot/` est prête en une minute
et reste disponible en permanence.

## Mettre l'application à jour

Remplacer le fichier `static/expression-ecrite-eleves.html` sur GitHub
(**Add file → Upload files**, même nom : GitHub écrase l'ancien). Streamlit
redéploie tout seul en une minute. Sur GitHub Pages, remplacer `index.html`.
