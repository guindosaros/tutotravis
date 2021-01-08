# txt1 = "jeirhivmelihlzibasjkugqbsklkflbnlbltfblfgbldflmfdbjloùsmxpmumlumlumplupmluzssxzsdxsxdzckorivjhrvbleciohekugvejeocizhxlzkjjabhcguevgroivhnrcoirhvcksdbnkccsmclsljzlsckjcbdjldcknskj"
# txt2 = "ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"
# txt3 = "ACCTAGCCATG"

# def compt_deco(message="Cette action est impossible"):
#     def decorator(function):
#         def deco(txt, nbr=2):
#             if len(txt) <= nbr:
#                 print(message)
#             else:
#                 return function(txt, nbr)
#         return deco
#     return decorator

# @compt_deco()
# def compte_mots_n_lettres(txt, nbr=2):
#     lst_double = [txt[i:i+nbr] for i in range(0, len(txt)) if len(txt[i:i+nbr]) == nbr]
#     result = [{lt: lst_double.count(lt)} for lt in set(lst_double)]
#     print(f"\n\n\nMots de {nbr} lettres\n")

#     for i in result:
#         print("\t:=> ", i)

# compte_mots_n_lettres(txt2, nbr=2)
# compte_mots_n_lettres(txt2, nbr=3)
# compte_mots_n_lettres(txt3, nbr=32)

# https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/2-functions/3-decorators/



import subprocess, os

#==========================================================================================================================================================
py = subprocess.run(["python", "--version"], capture_output=True, text=True)

if "python 3" in py.stdout.lower():
    python = "python"
else:
    python = "python3"


creation_environnement_virtuel = subprocess.run([f"{python}", "-m", "venv", "venv2"])

creation_environnement_virtuel = subprocess.run([f"{python}", "-m", "venv", "venv2"], shell=False, check=False, capture_output=True, text=True)

installation_packages_utiles = os.system('source venv2/bin/activate && pip install django pillow')

creation_du_projet = os.system('source venv2/bin/activate && django-admin startproject MyDjangoProject')

creation_du_requirements = subprocess.run(["touch", "requirements.txt"])

ajout_des_packages_au_requirements = os.system("echo django >> requirements.txt")
ajout_des_packages_au_requirements = os.system("echo pillow >> requirements.txt")

# #==========================================================================================================================================================
