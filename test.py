import time
from sutom import Sutom

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://gregfresnel.free.fr/WebMotus/WebGMotus.php")
elem = driver.find_element(By.ID, "btnStart")
elem.click()
time.sleep(1)
zoneText = driver.find_element(By.ID, "p")
ok = driver.find_element(By.ID, "ok")

def testerMot(mot):
    zoneText = driver.find_element(By.ID, "p")
    zoneText.send_keys(mot)
    ok.click()

def initialize(s):
    lettre = driver.find_element(By.ID, "L1C0").text
    s.demande([lettre, lettre+"_______","","________"])
    s.initisalisation()
    s.recherche()
    testerMot(s.liste_mot[0])

def resultat(ligne):
    lettre_connue =''
    mot=''
    lettre_faux = ''
    emplacementFaux = ''
    for i in range(8):
        elem = driver.find_element(By.ID, "L"+str(ligne)+"C"+str(i))
        prop = elem.get_attribute("class")
        lettre = elem.text
        if prop == "cr":
            if lettre in lettre_faux:
                lettre_faux = lettre_faux.replace(lettre, '')
            lettre_connue += lettre
            mot+=lettre
            emplacementFaux +='_'
        elif prop == "cb":
            if lettre not in lettre_connue and lettre not in lettre_faux:
                lettre_faux+=lettre
            mot+='_'
            emplacementFaux+=lettre
        else:
            if not lettre in lettre_connue:
                lettre_connue+=lettre
            mot+='_'
            emplacementFaux+=lettre
    return (lettre_connue, mot, lettre_faux, emplacementFaux)

def tourDeJeu(sutom, numero):
    sutom.demande(resultat(numero))
    sutom.initisalisation()
    sutom.recherche()
    try:
        testerMot(sutom.liste_mot[0])
    except:
        print("Error")
        sutom.initisalisation()
def trouverMot():
    sutom = Sutom()
    initialize(sutom)
    i = 1
    fin = False
    while i<6 and not fin:
        time.sleep(3.5)
        sutom.demande(resultat(i))
        if '_' in sutom.get_mot_trouver():
            tourDeJeu(sutom, i)
            i+=1
        else:
            break

for i in range(15):
    trouverMot()
    time.sleep(5)
