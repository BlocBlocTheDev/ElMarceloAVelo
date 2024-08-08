# El Marcelo A Velo

## Projet de récupération automatique des données des stations de vélo en libre service "Le Marcel à Vélo" de [Troyes Champagne Métropole](https://troyes-champagne-metropole.fr/)

---

## Utilisations

Vous pouvez utiliser ce projet comme bon vous semble, mais vous devez inclure le créateur originel dans tout fork, copie, etc...

### Fichiers du projet

- **`Main.py`**  
  Affiche toutes les stations avec :
  - Nombre de vélos disponibles
  - Places disponibles
  - Détails sur les vélos tels que :
    - Identifiant
    - Pourcentage de batterie
    - Autonomie en km
    - Disponibilité (Disponible si le vélo ne sert pas lui-même de station)

- **`FindBike.py`**  
  Permet de rechercher un vélo spécifique à l'aide de son identifiant sur toutes les stations. Si trouvé, affiche :
  - Station du vélo
  - Identifiant
  - Pourcentage de batterie
  - Autonomie en km
  - Disponibilité (Disponible si le vélo ne sert pas lui-même de station)

- **`Custom.py`**  
  Template pour vous aider à utiliser le projet.

---

## Comment s'en servir ?

### Étape initiale : Installer les dépendances

Le projet nécessite les dépendances suivantes :
- [GeckoDriver](https://github.com/mozilla/geckodriver) (Webdriver Firefox de Mozilla)
- [Selenium](https://github.com/SeleniumHQ/selenium) (Pour contrôler le Webdriver)
- [MySQL-Connector-Python](https://github.com/mysql/mysql-connector-python) *(Optionnel)*

Toutes ces dépendances sont automatiquement installées en exécutant le script `Install.py`.

> La version de GeckoDriver sera sélectionnée en fonction de votre système et architecture.

### Scripts

- **`Main.py`**  
  Ce script affiche les détails sur toutes les stations et les vélos sur chaque station. Aucune intervention requise de votre part.

- **`FindBike.py`**  
  Recherche un vélo parmi toutes les stations et affiche ses détails et sa localisation. Le script vous demande l'identifiant du vélo que vous souhaitez rechercher. Après un moment, soit le vélo est trouvé et ses détails sont affichés, soit il est introuvable.
