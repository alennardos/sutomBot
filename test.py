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

sutom = Sutom()

def testerMot(mot):
    zoneText = driver.find_element(By.ID, "p")
    zoneText.send_keys(mot)
    ok.click()

def initialize():
    lettre = driver.find_element(By.ID, "L1C0").text
    sutom.demande([lettre, lettre+"_______","","________"])
    sutom.initisalisation()
    sutom.recherche()
    testerMot(sutom.liste_mot[0])

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
            if not lettre in lettre_connue:
                lettre_connue += lettre
            mot+=lettre
            emplacementFaux +='-'
        elif prop == "cb":
            if lettre not in lettre_connue and lettre not in lettre_faux:
                lettre_faux+=lettre
            mot+='_'
            emplacementFaux+='_'
        else:
            if not lettre in lettre_connue:
                lettre_connue+=lettre
            mot+='_'
            emplacementFaux+='lettre'
    return (lettre_connue, mot, lettre_faux, emplacementFaux)

def tourDeJeu(numero):
    sutom.demande(resultat(numero))
    sutom.initisalisation()
    sutom.recherche()
    testerMot(sutom.liste_mot[0])

initialize()

for i in range(1,5):
    time.sleep(3.5)
    tourDeJeu(i)

