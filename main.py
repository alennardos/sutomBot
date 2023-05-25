import time
from sutom import Sutom

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://gregfresnel.free.fr/WebMotus/WebGMotus.php")

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
    var = resultat(numero)
    sutom.demande(var)
    sutom.initisalisation()
    sutom.recherche()
    try:
        testerMot(sutom.liste_mot[len(sutom.liste_mot)//2])
    except:
        sutom.initisalisation()
    chargement = False
    while not chargement :
        try:
            var = resultat(numero+1)[1]
            chargement = driver.find_element(By.ID, "L" + str(numero+2) + "C0").text == sutom.mot_trouver[0] or '_' not in var
            time.sleep(0.5)
        except:
            time.sleep(0.5)
            chargement = False
    var = resultat(numero+1)[1]
    return '_' not in var


def initialize(s):
    lettre = driver.find_element(By.ID, "L1C0").text
    s.demande([lettre, lettre+"_______","","________"])
    s.initisalisation()
    s.recherche()
    testerMot(s.liste_mot[len(s.liste_mot)//2])
    chargement = False
    while not chargement:
        try:
            chargement = driver.find_element(By.ID, "L" + str(2) + "C0").text == s.mot_trouver[0]
            time.sleep(0.5)
        except:
            time.sleep(0.5)
            chargement = False
    var = resultat(1)
    return '_' not in var[1]

def trouverMot():
    sutom = Sutom()
    i = 1
    fin = initialize(sutom)
    while i<6 and not fin:
        chargement = False
        while not chargement:
            try:
                chargement = driver.find_element(By.ID, "L" + str(i + 1) + "C0").text == sutom.mot_trouver[0]
            except:
                time.sleep(1)
                chargement = False
            fin = tourDeJeu(sutom, i)
            i+=1

while True:
    chargement = False
    while not chargement:
        try:
            ok = driver.find_element(By.ID, "clEnterA")
            zoneText = driver.find_element(By.CLASS_NAME, "tabJeu")
            time.sleep(0.5)
            chargement = driver.find_element(By.ID, "L1" + "C1").text == "."
        except:
            time.sleep(0.5)
            chargement = False
    trouverMot()