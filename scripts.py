import os
import platform
import subprocess


# # Creation de l'environnement virtual Venv et activation

version = subprocess.run(["python", "--version"], capture_output=True, text=True)


if "python 3" in version.stdout.lower():
    python = "python"
else:
    python = "python3"

createvenv = os.system(f"{python} -m venv venv")

if  platform.system() == 'Windows':
    activatevenv = os.system("source venv/Scripts/activate && pip install django")
    
else:
    
    activatevenv = os.system("source venv/bin/activate &&  pip install django")
    nomprojet = input('Entrez le nom de votre projet django : ')
    activatevenv = os.system(f"source venv/bin/activate &&  django-admin  startproject {nomprojet}")
    creationrequirement = os.system(f"source venv/bin/activate && cd {nomprojet} && pip freeze >> requirements.txt")






