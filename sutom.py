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

    def demande(self, res):
        self.lettre_connue = res[0]
        self.nb_lettre_connue = not len(self.lettre_connue)
        self.mot_trouver = res[1]
        self.nb_lettre = len(self.mot_trouver)
        self.lettre_faux = res[2]
        self.nb_lettre_faux = len(self.lettre_faux)
        self.emplacement_faux = res[3]

    def initisalisation(self):
        self.mot = 'A'
        self.total = 0

    def recherche(self):
        i=0
        while chr(ord(self.mot[0])-1)< self.mot_trouver[0] and i < self.max:
            if (self.liste):
                mot = self.liste_mot[i]
            else:
                mot = self.file.readline()
            if(len(mot) == self.nb_lettre +1):
                res = True
                j = 0
                while res and j< self.nb_lettre_connue:
                    res = self.lettre_connue[j] in mot
                    j+=1
                if (res):
                    j = 0
                    while res and j < self.nb_lettre_faux:
                        res = self.lettre_faux[j] not in mot
                        j += 1
                if (res):
                    j = 0
                    while res and j< self.nb_lettre:
                        if (self.mot_trouver[j] != '_'):
                            res = self.mot_trouver[j] == mot[j]
                        if (res):
                            if (self.emplacement_faux[j] != '_'):
                                res = self.emplacement_faux[j] != mot[j]
                        j+=1
                if (res):
                    total +=1
                    self.liste_mot.append(mot)
            i+=1
        max = total
        liste_mot = self.liste_mot[len(self.liste_mot) - total:]
        liste = True
        print(total)