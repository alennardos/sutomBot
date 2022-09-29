import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://gregfresnel.free.fr/WebMotus/WebGMotus.php")
elem = driver.find_element(By.ID, "btnStart")
elem.click()
time.sleep(1)
zoneText = driver.find_element(By.ID, "p")

def initialize():


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
            if not lettre in lettre_connue:
                lettre_faux+=lettre
            mot+='_'
            emplacementFaux+='_'
        else:
            if not lettre in lettre_connue:
                lettre_connue+=lettre
            mot+='_'
            emplacementFaux+='lettre'
    return (lettre_connue, mot, lettre_faux, emplacementFaux)

mot = resultat(1)

print(mot)

"""assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.pag"""