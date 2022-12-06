import os 
import time

import glob
import shutil
import getpass

username = getpass.getuser()
#source : https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python

import requests
from requests_html import HTMLSession

## Liste d'erreur ##
##
## N404 : le dossier n'est pas trouver



# ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ #

expired_version = 'NTool-V01.exe'
version = 'NTool-V01'
last_version = 'NTool-V02.exe'

path = os.getcwd()
os.system('mode con: cols=80 lines=20')
# ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ #


def tool_update():
    
    ## Execution probable sur la version suivante.
    ## A chaque démarage on supprime l'ancienne version.
    ## Lors de la mise a jour, vue que le lancement de la nouvelle version est automatique alors celle-ci supprime la précedente.
    print('Please wait, checking for updates. 1/2')

    os.chdir(path)
    print(path) # Debug : Print cd
    try:
        os.remove(expired_version)
    except:
        print('none')

    # get last version // instalation 
    print('Please wait, checking for updates. 2/2')

    s = HTMLSession()
    link = "https://github.com/Nuxhi" # on regarde.
    link_update = "https://github.com/Nuxhi/NTool/raw/main/NTool-V02.exe" # Si une version est disponible, alors on la télécharge grace à "link_update"
    #https://github.com/Nuxhi/NTool/blob/main/README.md 
    rqt = s.get(link)
    

    #Vérification de la disponibilité des serveurs.
    if rqt.ok:
        print('Connection to the update server')
    else:
        print('[Console] : Serveur indisponible : ', rqt,'\nDirigez-vous sur notre discord !')
        time.sleep(2), main_menu()

    #Si le serveur est disponbile alors on essaye de vérifié.
    try:
        title = rqt.html.find('.p-org')[0].text
    except:
        title = ('UKN')
    
    #si la version ne correspond pas, alors on envoie une requet pour télécharger la nouvelle.
    if title != version:
        print('update disponible !\nVersion : ',title,'disponible,\nTéléchargement en cours...')
        r_upt = s.get(link_update, allow_redirects=True)
        open('README.md', 'wb').write(r_upt.content)

        time.sleep(5)
        os.startfile(last_version) # On lance la nouvelle version afin que le processus de suppression sois executer.     
        print('start', last_version)
        time.sleep(5)
        exit

    else:
        print('Aucune update disponible !')
    time.sleep(1)
    




tool_update()

def main_menu():

    os.system('cls')
    print("\n                          Bienvenu sur :", version)
    print("\n                       ╔══════════════════════════════╗")
    print("                       ║                              ║")
    print("                       ║     1.  Vider le cache       ║")
    print("                       ║                              ║")
    print("                       ║     2. Ouvrir les dossiers   ║")
    print("                       ║                              ║")
    print("                       ║     3. Gestion des mods      ║")
    print("                       ║                              ║")
    print("                       ║     4. Mise a jour du tool   ║")
    print("                       ║                              ║")
    print("                       ╚══════════════════════════════╝\n")
    choix = input(" [CONSOLE]   :  ")
    if choix == '1':
        cache_menu()

    if choix == '2':
        try:
            os.startfile("C:/Users/"+ username + "/AppData/Local/FiveM")
        except: 
            print("[Erreur N404] - FiveM n'est pas trouver")
            time.sleep(2), main_menu() 

    if choix == '4':
        tool_update() 

    return 'menu', time.sleep(2), main_menu()


def cache_menu():
    os.system('cls')
    print("\n")
    print("\n               ╔══════════════════════════════╗")
    print("               ║                              ║")
    print("               ║     1.  Vider le cache       ║")
    print("               ║                              ║")
    print("               ║     2.  Vidange extreme      ║")
    print("               ║                              ║")
    print("               ║     3.  Citizen Zero         ║")
    print("               ║                              ║")
    print("               ║     4.  Retour au menu       ║")
    print("               ║                              ║")
    print("               ╚══════════════════════════════╝\n")

    choix = input(" [CONSOLE]   :  ")
    if choix == '1':
        cache_lvl1()

    if choix == '2':
        cache_lvl2()
    
    if choix == '3':
        citizen_zero()

    if choix == '4':
        main_menu()

def cache_lvl1():
# cache_lvl1 : 
# cache_lvl1 est le premier niveau de suppression du cache de FiveM, certe celui-ci est le premier mais il reste le meillieur.
# en effet, une suppréssion calculer (plus lente) de fichier / dossier visé, on pointe notre supprésion sur ce qui joue vraiment dans le cache de FiveM

    try:
        os.chdir("C:/Users/" + username+ "/AppData/Local/FiveM/FiveM.app")
    except:
        print("[Erreur N404] - FiveM n'est pas trouver")
        time.sleep(2), main_menu() 

    try:
        os.remove("adhesive.dll")
        print("[FILE] - adhesive.dll")
    except OSError:
        pass
        print("[FILE] - adhesive.dll was not find")

    try:
        os.remove("caches.xml")
        print("[FILE] - caches.xml")
    except OSError:
        pass
        print("[FILE] - caches.xml was not find")

    
    shutil.rmtree("data", ignore_errors=True)
    if os.path.exists("data"):
        print("[FOLDER] - DATA ")
    else:
        print("[FOLDER] - DATA was not find")

    shutil.rmtree("logs", ignore_errors=True)
    if os.path.exists("logs"):
        print("[FOLDER] - LOGS ")
    else:
        print("[FOLDER] - LOGS was not find")

def cache_lvl2():
# cache_lvl2 : 
# cache_lvl2 est une suppréssion hardcore / beaucoup plus violente du cache de FiveM.
# On ne cherche plus a viser, on fait de la supprésion de masse. 
# Des bugs en jeu peuvent etre subie.

    ## fichier !
    try:
        os.chdir("C:/Users/" + username+ "/AppData/Local/FiveM/FiveM.app")
    except:
        print("[Erreur N404] - FiveM n'est pas trouver")
        time.sleep(2), main_menu() 

    try:
        os.remove("adhesive.dll")
        print("[FILE] - adhesive.dll")
    except OSError:
        pass
        print("[FILE] - adhesive.dll was not find")

    try:
        os.remove("caches.xml")
        print("[FILE] - caches.xml")
    except OSError:
        pass
        print("[FILE] - caches.xml was not find")

    #citizen-devtools.dll
    try:
        os.remove("citizen-devtools.dll")
        print("[FILE] - citizen-devtools.dll")
    except OSError:
        pass
        print("[FILE] - citizen-devtools.dll was not find")
    
    #CitizenGame.dll
    try:
        os.remove("CitizenGame.dll")
        print("[FILE] - CitizenGame.dll")
    except OSError:
        pass
        print("[FILE] - CitizenGame.dll was not find")

    #citizen-game-main.dll
    try:
        os.remove("citizen-game-main.dll")
        print("[FILE] - citizen-game-main.dll")
    except OSError:
        pass
        print("[FILE] - citizen-game-main.dll was not find")

    # 29 / 11 / 2020 -- 23:55
    #CitizenFX_SubProcess_chrome.bin
    #CitizenFX_SubProcess_game_1604
    #CitizenFX_SubProcess_game_1604_aslr
    #CitizenFX_SubProcess_game_2060
    #CitizenFX_SubProcess_game_2060_aslr
    #CitizenFX_SubProcess_game_2189
    #CitizenFX_SubProcess_game_2189_aslr
    #CitizenFX_SubProcess_game_2372
    #CitizenFX_SubProcess_game_2372_aslr
    #CitizenFX_SubProcess_game_2545
    #CitizenFX_SubProcess_game_2545_aslr
    #CitizenFX_SubProcess_game_2612
    #CitizenFX_SubProcess_game_2612_aslr
    #CitizenFX_SubProcess_game_2699
    #CitizenFX_SubProcess_game_2699_aslr

    for e in glob.glob("CitizenFX_SubProcess_game*.*"):
        print(e)
        try:
            os.remove(e)
            print("[FILE] -" + e)
        except OSError:
            pass
            print("[FILE] - * SubProcess_game not find ")
    
    #C:\Users\FABIE\AppData\Local\FiveM\FiveM.app\bin\cef

    # 29 / 11 / 2020 -- 23:55
    #citizen-resources-client
    #citizen-resources-core
    #citizen-resources-gta
    #citizen-resources-metadata-lua
    for e in glob.glob("citizen-resources*.*"):
        print(e)
        try:
            os.remove(e)
            print("[FILE] -" + e)
        except OSError:
            pass
            print("[FILE] - * citizen-resources not find ")


    ## dossier !

    shutil.rmtree("data", ignore_errors=True)
    if os.path.exists("data"):
        print("[FOLDER] - DATA ")
    else:
        print("[FOLDER] - DATA was not find")

    shutil.rmtree("logs", ignore_errors=True)
    if os.path.exists("logs"):
        print("[FOLDER] - LOGS ")
    else:
        print("[FOLDER] - LOGS was not find")

    shutil.rmtree("crashes", ignore_errors=True)
    if os.path.exists("crashes"):
        print("[FOLDER] - crashes ")
    else:
        print("[FOLDER] - crashes was not find")

# citizen_zero : 
# Objectif zero, au lieu de devoir constamment accédez au fichier de FiveM ou encore mieux, de devoir re télécharger le logiciel,
# citizen_zero simplifie la tache, on supprime simplement le dossier Citizen de FiveM

def citizen_zero():
    
    try:
        os.chdir("C:/Users/" + username+ "/AppData/Local/FiveM/FiveM.app")
    except:
        print("[Erreur N404] - FiveM n'est pas trouver")
        time.sleep(2), main_menu() 

    shutil.rmtree("citizen", ignore_errors=True)
    if os.path.exists("citizen"):
        print("[FOLDER] - citizen ")
    else:
        print("[FOLDER] - citizen was not find")



main_menu()
