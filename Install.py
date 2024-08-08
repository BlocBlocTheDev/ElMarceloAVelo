import os
import platform
import subprocess
import sys
import urllib.request
import zipfile
import tarfile
import shutil

# Function to install Python packages
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Function to determine system details and download geckodriver
def download_geckodriver():
    system = platform.system()
    architecture = platform.architecture()[0]
    processor = platform.processor()

    # Define base URL for geckodriver downloads
    base_url = "https://github.com/mozilla/geckodriver/releases/download/v0.35.0/"
    file_name = ""
    
    if system == "Windows":
        if architecture == "32bit":
            file_name = "geckodriver-v0.35.0-win32.zip"
        elif architecture == "64bit":
            if "ARM" in processor:
                file_name = "geckodriver-v0.35.0-win-aarch64.zip"
            else:
                file_name = "geckodriver-v0.35.0-win64.zip"
    
    elif system == "Darwin":  # macOS
        if "ARM" in processor:
            file_name = "geckodriver-v0.35.0-macos-aarch64.tar.gz"
        else:
            file_name = "geckodriver-v0.35.0-macos.tar.gz"
    
    elif system == "Linux":
        if architecture == "32bit":
            file_name = "geckodriver-v0.35.0-linux32.tar.gz"
        elif architecture == "64bit":
            if "ARM" in processor:
                file_name = "geckodriver-v0.35.0-linux-aarch64.tar.gz"
            else:
                file_name = "geckodriver-v0.35.0-linux64.tar.gz"

    if not file_name:
        print("Système d'exploitation ou Architechture non supporté.")
        return

    download_url = base_url + file_name
    file_path = os.path.join("Deps", file_name)

    if not os.path.exists("Deps"):
        os.makedirs("Deps")

    print(f"Téléchargement du driver {file_name}...")
    urllib.request.urlretrieve(download_url, file_path)

    print(f"Extraction du driver {file_name}...")
    if file_name.endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall("Deps")
    elif file_name.endswith(".tar.gz"):
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall("Deps")

    print(f"Nettoyages en cours...")
    os.remove(file_path)

# Main function
def main():
    packages = [
        "selenium",
        "mysql-connector-python"
    ]

    # Install required packages
    for package in packages:
        try:
            __import__(package.split(' ')[0])
        except ImportError:
            print(f"Installation de {package}...")
            install(package)
        else:
            print(f"{package} est déjà installé.")

    # Download and install geckodriver
    download_geckodriver()

if __name__ == "__main__":
    main()