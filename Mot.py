class Mot(object):
    """Classe représentant un mot sous forme d'ARN"""
    def __init__(self, chaine):
        super(Mot, self).__init__()
        self.chaine = chaine

    def __str__(self) :
        return self.chaine

    def __eq__(self, other) :
        return self.chaine == other.chaine

    def __hash__(self) :
        return hash(self.chaine)


    def reverse(self) :
        """Retourne le reverse du Mot"""
        return Mot(self.chaine[::-1])

    def complem(self) :
        """Retourne le complémentaire du Mot"""
        res = ""
        for lettre in self.chaine :
            if lettre == 'A' :
                res+='U'
            elif lettre == 'U' :
                res+='A'
            elif lettre == 'G' :
                res+='C'
            else :
                res+='G'
        return Mot(res)

    def revCompl(self) :
        """Retourne le reverse complémentaire du Mot"""
        return self.complem().reverse()

    def algoNaif(self,mot,normal=True,reverse=False,complem=False,revCompl=False) :
        """
        Renvoie l'indice des occurences du Mot donné dans le Mot courant.
        Utilise un algorithme de recherche naïf
        """
        lesMots = []
        res = []

        #initialisation de la liste de mots à rechercher. (permet de prendre en compte les reverse et/ou complémentaires )
        if normal :
            lesMots.append(mot)
        if reverse :
            lesMots.append(mot.reverse())
        if complem :
            lesMots.append(mot.complem())
        if revCompl :
            lesMots.append(mot.revCompl())

        #algorithme naïf
        n = len(self.chaine)
        m = len(mot.chaine)

        j = 0
        for motTest in lesMots :
            for i in range(n-m+1) :
                trouve = True
                for j in range(m) :
                    if not motTest.chaine[j] == self.chaine[i+j] :
                        trouve = False
                        break
                if trouve :
                    res.append(i)

        return res

    def algoKMP(self,mot,normal=True,reverse=False,complem=False,revCompl=False) :
        """
        Renvoie l'indice des occurences du Mot donné dans le Mot courant.
        Utilise un algorithme de recherche Knuth-Morris-Pratt
        """
        lesMots = []
        res = []

        #initialisation de la liste de mots à rechercher. (permet de prendre en compte les reverse et/ou complémentaires )
        if normal :
            lesMots.append(mot)
        if reverse :
            lesMots.append(mot.reverse())
        if complem :
            lesMots.append(mot.complem())
        if revCompl :
            lesMots.append(mot.revCompl())

        #algorithme Knuth-Morris-Pratt
        n = len(self.chaine)
        m = len(mot.chaine)

        for motTest in lesMots :

            longestPrefixSuffixArray = self.getLongestPrefixSuffixArray(motTest)
            i = 0
            j = 0

            while i < n:
                if motTest.chaine[j] == self.chaine[i] :
                    i += 1
                    j += 1

                if j == m :
                    res.append(i - j)
                    j = longestPrefixSuffixArray[j - 1]

                elif i < n and motTest.chaine[j] != self.chaine[i] :
                    if j != 0 :
                        j = longestPrefixSuffixArray[j - 1]
                    else :
                        i += 1
        return res

    def getLongestPrefixSuffixArray(self, mot):
        """
        Préparation du tableau utilisé par algoKMP
        """
        n = len(self.chaine)
        m = len(mot.chaine)
        longestPrefixSuffixArray = [0] * m
        oldPrefixSuffixLength = 0

        i = 1

        while i < m :
            if mot.chaine[i] == mot.chaine[oldPrefixSuffixLength] :
                oldPrefixSuffixLength += 1
                longestPrefixSuffixArray[i] = oldPrefixSuffixLength
                i+=1
            else :
                if oldPrefixSuffixLength != 0 :
                    oldPrefixSuffixLength = longestPrefixSuffixArray[oldPrefixSuffixLength - 1]
                else :
                    longestPrefixSuffixArray[i] = 0
                    i += 1

        return longestPrefixSuffixArray

    def occurencesMotsTailleN(self, N) :
        """
        Retourne les occurences de tous les sous-mots de taille N présents dans le Mot courant
        Utilise un algorithme de recherche naïf
        """
        n = len(self.chaine)
        mapMot = {}
        for i in range(n-N+1) :
            mot = Mot(self.chaine[i:i+N])
            if(not mot in mapMot ):
                mapMot[mot] = [-1]
        for mot in mapMot :
            mapMot[mot] = self.algoNaif(mot, normal=True, revCompl=True)
        return mapMot

    def occurencesMotsTailleNKMP(self, N) :
        """
        Retourne les occurences de tous les sous-mots de taille N présents dans le Mot courant
        Utilise l'algorithme de recherche Knuth-Morris-Pratt
        """
        n = len(self.chaine)
        mapMot = {}
        for i in range(n-N+1) :
            mot = Mot(self.chaine[i:i+N])
            if(not mot in mapMot ):
                mapMot[mot] = [-1]
        for mot in mapMot :
            mapMot[mot] = self.algoKMP(mot, normal=True, revCompl=True)
        return mapMot


def printMapMot(mapMot):
    """Imprime une map contenant un mot et le nombre de ses occurences"""
    for key, value in mapMot.items() :
        print('key = ' + str(key) + '### value = ' + str(value) )

def printPlot(mapMot,pathname) :
    """
    Écrit les coordonnées des occurences données dans le fichier "pathname"
    Permet de dessiner un dotplot
    """
    f = open(pathname,'w')
    for mot,liste in mapMot.items() :
        for i in liste :
            for j in liste :
                f.write(str(i)+'\t'+str(j)+'\n')
    f.close()

def lecture(pathname) :
    """Crée un Mot contenu dans le fichier pathname"""
    f = open(pathname,'r')
    #premiere ligne osef
    f.readline()
    chaine = ""
    for ligne in f :
        chaine += ligne.rstrip()
    f.close()
    # print(chaine)
    return Mot(chaine)




# Tests
def testModifsMots() :
    """Teste si les modificateurs du mot (reverse, complem, revCompl) agissent comme prévu"""
    print("Test modificateurs")
    mot = Mot("ACAUAG")
    print("chaine : ACAUAG")
    print("reverse : ", mot.reverse())
    print("complem : ", mot.complem())
    print("revCompl : ", mot.revCompl())

def testAlgoNaif() :
    """Teste l'algorithme de recherche naïf"""
    print("Test algoNaif")
    mot = Mot("AA")
    text = Mot("AACGUAACGGAA")
    print("mot : ",mot)
    print("text : ", text)
    print ("occurences : ",text.algoNaif(mot))

def testAlgoKMP() :
    """Teste l'algorithme Knuth-Morris-Pratt"""
    print("Test algoKMP")
    mot = Mot("AA")
    text = Mot("AACGUAACGGAA")
    print("mot : ",mot)
    print("text : ", text)
    print ("occurences : ",text.algoKMP(mot))

def testLecture() :
    """Teste si la lecture d'un fichier fonctionne"""
    print("Test Lecture")
    mot = lecture("donneeTest.fasta")
    print(mot)

def createPlotNaif(fileIn, fileOut, N) :
    """
    Crée un dotplot fileOut contenant les occurences des sous-mots de taille N dans le fichier fileIn
    Utilise l'algorithme Naïf
    """
    print("Création de DotPlot -- Naïf", fileIn)
    print("Lecture du fichier", fileIn)
    mot = lecture(fileIn)
    print("Recherche (Naïf) des sous mots de taille", N)
    mapMot = mot.occurencesMotsTailleN(N)
    print("Écriture des résultats dans", fileOut)
    printPlot(mapMot, fileOut)

def createPlotKMP(fileIn, fileOut, N) :
    """
    Crée un dotplot fileOut contenant les occurences des sous-mots de taille N dans le fichier fileIn
    Utilise l'algorithme Knuth-Morris-Pratt
    """
    print("Création de DotPlot -- KMP", fileIn)
    print("Lecture du fichier", fileIn)
    mot = lecture(fileIn)
    print("Recherche (KMP) des sous mots de taille", N)
    mapMotKMP = mot.occurencesMotsTailleNKMP(N)
    print("Écriture des résultats dans", fileOut)
    printPlot(mapMotKMP, fileOut)

# # Décommenter ces lignes pour lancer les tests
# testModifsMots()
# testAlgoNaif()
# testAlgoKMP()
# testLecture()


#createPlotNaif("data-mirna/ARNmessager-1.fasta", "occurencesARN.dat", 6)
#createPlotKMP("data-mirna/ARNmessager-1.fasta", "occurencesARNKMP.dat", 6)

#createPlotKMP("donneeTest.fasta", "occurencesARNKMP.dat", 2)
