class Sutom:

    def __init__(self):
        self.file = open('dictionnaire.txt', 'r')
        self.max = 386264
        self.mot = 'A'
        self.total = 0
        self.lettre_connue = ''
        self.nb_lettre_connue = 0
        self.mot_trouver = ''
        self.lettre_faux = ''
        self.nb_lettre_faux = 0
        self.emplacement_faux = ''
        self.liste = False
        self.liste_mot = []
        self.nb_lettre = 0
        self.trouver = False

    def demande(self):
        global lettre_connue
        lettre_connue = input('lettre connue')
        global nb_lettre_connue
        nb_lettre_connue = len(lettre_connue)
        global mot_trouver
        mot_trouver = input('mot (_ pour les lettres vide)')
        global nb_lettre
        nb_lettre = len(mot_trouver)
        global lettre_faux
        lettre_faux = input('lettre faux')
        global nb_lettre_faux
        nb_lettre_faux = len(lettre_faux)
        global emplacement_faux
        emplacement_faux = input('lettres mauvais emplacement (_ pour les lettres vide')

    def initisalisation(self):
        global mot
        mot = 'A'
        global total
        total = 0

    def recherche(self, mot, nb_lettre, lettre_connue, nb_lettre_connue, mot_trouver, lettre_faux, nb_lettre_faux, emplacement_faux):
        i=0
        global parcour
        global liste
        global total
        global max
        global liste_mot
        while chr(ord(mot[0])-1)<mot_trouver[0] and i < max:
            if (liste):
                mot = liste_mot[i]
            else:
                mot = file.readline()
            if(len(mot) == nb_lettre+1):
                res = True
                j = 0
                while res and j<nb_lettre_connue:
                    res = lettre_connue[j] in mot
                    j+=1
                if (res):
                    j = 0
                    while res and j < nb_lettre_faux:
                        res = lettre_faux[j] not in mot
                        j += 1
                if (res):
                    j = 0
                    while res and j<nb_lettre:
                        if (mot_trouver[j] !='_'):
                            res = mot_trouver[j] == mot[j]
                        if (res):
                            if (emplacement_faux[j] != '_'):
                                res = emplacement_faux[j] != mot[j]
                        j+=1
                if (res):
                    total +=1
                    liste_mot.append(mot)
                    print(mot)
            i+=1
        max = total
        liste_mot = liste_mot[len(liste_mot)-total:]
        liste = True
        print(total)

    parcour = 0
    while not trouver:
        demande()
        initisalisation()
        recherche( mot, nb_lettre, lettre_connue, nb_lettre_connue, mot_trouver, lettre_faux, nb_lettre_faux, emplacement_faux)
        trouver = int(input('trouver ? 1 = oui / 0 = non'))
        parcour+=1


    print('fin')
    file.close()
    quit()
