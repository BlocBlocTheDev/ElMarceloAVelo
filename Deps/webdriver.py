firefox_options = Options()
firefox_options.add_argument("--headless")  # Exécuter le navigateur en arrière-plan (optionnel)

# Chemin vers le GeckoDriver (adapté à votre environnement)
geckodriver_path = 'Deps/geckodriver.exe'

# Fonction pour initialiser le WebDriver
def init_driver():
    service = Service(geckodriver_path)
    return webdriver.Firefox(service=service, options=firefox_options)
