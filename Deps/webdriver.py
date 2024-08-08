firefox_options = Options()
firefox_options.add_argument("--headless")  # Exécuter le navigateur en arrière-plan (optionnel)

geckodriver_path = 'Deps/geckodriver'

# Vérifier le système d'exploitation
if platform.system() == 'Windows':
    # Sous Windows, ajouter l'extension .exe
    geckodriver_path += '.exe'

# Vérifier si le fichier geckodriver existe
if not os.path.isfile(geckodriver_path):
    print(f"Erreur : Le WebDriver Gecko n'est pas trouvé !")
    print(f"Tentez d'executer Install.py")
    sys.exit(1)

# Fonction pour initialiser le WebDriver
def init_driver():
    service = Service(geckodriver_path)
    return webdriver.Firefox(service=service, options=firefox_options)
