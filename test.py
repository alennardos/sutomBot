import time
from sutom import Sutom

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://gregfresnel.free.fr/WebMotus/WebGMotus.php")
#elem = driver.find_element(By.ID, "btnStart")
#elem.click()

time.sleep(5)


ok = driver.find_element(By.ID, "clEnterA")

def testerMot(mot):
    try:
        mot = mot[:len(mot) - 1]
        mot2 = zoneText.text
        mot2 = mot2[len(mot2)-15:]
        for i in range(len(mot)):
            if mot2[i*2] == '.' or mot2[i*2] == mot[i]:
                elem = driver.find_element(By.ID, "cl"+mot[i])
                elem.click()
        ok.click()
    except:
        testerMot(mot)

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
        chargement = False
        while not chargement:
            chargement = driver.find_element(By.ID, "L" + str(i + 1) + "C0").text == sutom.mot_trouver[0]
            time.sleep(0.5)
            if driver.find_element(By.ID, "L1C1").text == ".":
                print("aaaaaaaaaaaaaaaaaaaaaaaaaaa")
                fin = True
                chargement = True
            if not fin:
                tourDeJeu(sutom, i)
                i+=1

while True:
    zoneText = driver.find_element(By.CLASS_NAME, "tabJeu")
    trouverMot()
