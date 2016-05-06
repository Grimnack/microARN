import numpy as np
import Mot
#TP microARN Matthieu Caron et Arnaud Cojez

def Del(x):
    return -2

def Ins(y):
    return -2

# def Sub(x,y) :
#     if(x == y) :
#         return 2
#     else :
#         return -1

def Sub(x,y) :
    if (x == 'A' and (y == 'U' or y == 'T')) or ((x == 'U' or y == 'T') and y == 'A') :
        return 2
    elif (x == 'G' and y == 'C') or (x == 'C' and y == 'G') :
        return 2
    elif (x == 'G' and (y == 'U' or y == 'T')) or ((x == 'U' or y == 'T') and y == 'G') :
        return 2
    else :
        return -1

def createNWMatrix(X, Y) :
    # initialisation du tableau Score :
    Score = np.zeros((len(X) + 1,len(Y) + 1))
    # initialisation des bords du tableau
    for i in range(len(Score)) :
        Score[i][0] = i * -2
    for j in range(len(Score[0])) :
        Score[0][j] = j * -2
    # Calcul de la matrix score
    for i in range(1,len(X)+1) :
        for j in range(1,len(Y)+1) :
            scoreSub = Score[i-1][j-1] + Sub(X[i-1],Y[j-1])
            scoreDel = Score[i-1][j] + Del(X[i-1])
            scoreIns = Score[i][j-1] + Ins(Y[j-1])
            Score[i][j] = max(scoreSub,scoreIns,scoreDel)
    return Score


def NWScore(X, Y, Score) :
    '''
    return the last line of the Needleman-Wunsch score matrix
    '''
    LastLine = [0] * len(Y)
    for j in range(len(Y)) :
        LastLine[j] = Score[len(X)][j]
    return LastLine

def NeedlemanWunsch (A, B, F):
    '''
    Remonte la matrix score F pour trouver le meilleur alignement possible
    entre les mots A et B
    '''
    AlignmentA = ""
    AlignmentB = ""
    i = len(A)
    j = len(B)
    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + Sub(A[i-1], B[j-1])):
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            i = i - 1
            j = j - 1
        elif (i > 0 and F[i][j] == F[i-1][j] + Del(A[i-1])) :
            AlignmentA = A[i-1] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i = i - 1
        elif (j > 0 and F[i][j] == F[i][j-1] + Ins(B[j-1])) :
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j-1] + AlignmentB
            j = j - 1
    return (AlignmentA,AlignmentB)

def compteDebut(mot) :
    res = 0
    for i in range(len(mot)) :
        if mot[i] != '.' :
            return res
        res +=1
    return res

def compteFin(mot) :
    res = 0
    taille = len(mot)
    i = taille - 1
    while i >= 0 :
        if mot[i] != '.' :
            return res
        res +=1
        i = i - 1
    return res

def compteBoucleTerminale(motA, motB) :
    return compteFin(motA) + compteDebut(motB)

def NeedlemanWunsch2 (A, B, F, minAppariement=3, maxBoucle=3, maxBoucleTerminale=8):
    '''
    Remonte la matrix score F pour trouver le meilleur alignement possible
    entre les mots A et B
    '''
    AlignmentA = ""
    AlignmentB = ""
    i = len(A)
    j = len(B)
    boucleCouranteA = 0
    appariementCourantA = 0
    boucleCouranteB = 0
    appariementCourantB = 0
    while (i > 0 or j > 0):

        if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + Sub(A[i-1], B[j-1])):
            AlignmentA = AlignmentA + "("
            AlignmentB = ")" + AlignmentB
            i = i - 1
            j = j - 1
            boucleCouranteA = 0
            boucleCouranteB = 0
            appariementCourantA += 1
            appariementCourantB += 1
            if boucleCouranteA > maxBoucle :
                print("fail n0")
                return (None, None)
                if boucleCouranteB > maxBoucle :
                    print("fail n1")
                    return (None, None)
        elif (i > 0 and F[i][j] == F[i-1][j] + Del(A[i-1])) :
            AlignmentB = "." + AlignmentB
            i = i - 1
            boucleCouranteB += 1
            boucleCouranteA = 0
            if appariementCourantB < minAppariement and not appariementCourantB == 0:
                print("fail n2")
                return (None, None)
            appariementCourantB = 0
        elif (j > 0 and F[i][j] == F[i][j-1] + Ins(B[j-1])) :
            AlignmentA =  AlignmentA + "."
            j = j - 1
            boucleCouranteA += 1
            boucleCouranteB = 0
            if appariementCourantA < minAppariement and not appariementCourantA == 0:
                print("fail n3")
                return (None, None)
            appariementCourantA = 0
        print(boucleCouranteA)
        print(boucleCouranteB)
        print(AlignmentA,AlignmentB)
    if compteBoucleTerminale(AlignmentA, AlignmentB) <= maxBoucleTerminale :
        return (AlignmentA + AlignmentB)
    else :
        return (None, None)

#def NeedlemanWunsch2(A, B, F, matchMin):
#    '''
#    Remonte la matrix score F pour trouver le meilleur alignement possible
#    entre les mots A et B
#    '''
#    cptMatch = 0
#    SerieActuelle = 0
#    minSerie = None
#    MisMatchSerieActuelle = 0
#    maxSerie = 0
#    AlignmentA = ""
#    AlignmentB = ""
#    i = len(A)
#    j = len(B)
#    while (i > 0 or j > 0):
#        resSub = Sub(A[i-1], B[j-1])
#        if resSub == 2 :
#            maxSerie = max(maxSerie,MisMatchSerieActuelle)
#            MisMatchSerieActuelle = 0
#            if MisMatchSerieActuelle > 3 :
#                return None
#            SerieActuelle = SerieActuelle + 1
#            cptMatch = cptMatch + 1
#        else :
#            MisMatchSerieActuelle = MisMatchSerieActuelle + 1
#            if minSerie is None :
#                minSerie = SerieActuelle
#            else :
#                minSerie = min(minSerie,SerieActuelle)
#                if minSerie < 3 :
#                    return None
#            SerieActuelle = 0
#        if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] +scoreSub):
#            AlignmentA = A[i-1] + AlignmentA
#            AlignmentB = B[j-1] + AlignmentB
#            i = i - 1
#            j = j - 1
#        elif (i > 0 and F[i][j] == F[i-1][j] + Del(A[i-1])) :
#            AlignmentA = A[i-1] + AlignmentA
#            AlignmentB = "-" + AlignmentB
#            i = i - 1
#        elif (j > 0 and F[i][j] == F[i][j-1] + Ins(B[j-1])) :
#            AlignmentA = "-" + AlignmentA
#            AlignmentB = B[j-1] + AlignmentB
#            j = j - 1
#    if cptMatch < matchMin :
#        return None
#    return (AlignmentA,AlignmentB)




def main(texte, tailleMax, validation) :
    '''
    parcours le texte et cherche les microARN dans le texte

    ENTREE
    texte : la chaine de caractère à parcourir
    dans lequel on va chercher les tiges boucles

    tailleMax : longueur max de la tige boucles

    validation : le nombre minimum de paires pour valider une tige boucles

    SORTIE
    la liste [(tige boucle, indice)]
    '''
    tailleTexte = len(texte)
    res = []
    for i in range(tailleTexte-tailleMax/2) :
        trouve = False
        tailleActuel = 50
        while not trouve and tailleActuel>=24:
            mot1 = Mot(texte[i:i+tailleActuel])
            mot2 = Mot(texte[i+tailleActuel:i+tailleMax])
            revCompl = mot1.revCompl()
            #rechercher le revCompl dans le mot2
            F = createNWMatrix(revCompl,mot2)
            resultat = NeedlemanWunsch2(revCompl,mot2,F)
            if cptMatch >= 24 :
                res.append(resultat,i)
                trouve = True
            else :
                tailleActuel = tailleActuel -1


# F = createNWMatrix("ACTGTAG","ACGGCTAT")
# print(NeedlemanWunsch("ACTGTAG","ACGGCTAT",F))

#F = createNWMatrix("AGGGACUCUGGAGUUCACACU","UCCCUGAGACCUCAAGUGUGA")
#print(NeedlemanWunsch("AGGGACUCUGGAGUUCACACU","UCCCUGAGACCUCAAGUGUGA",F, 3, 3, 8))

# F = createNWMatrix("AGGGACUAUGGGUUCAAGCCU","UCCCUGAGACCUCAAGUGUGA")
# print("AGGGACUAUGGGUUCAAGCCU" + "UCCCUGAGACCUCAAGUGGGA")
# print(NeedlemanWunsch2("AGGGACUAUGGGUUCAAGCCU","UCCCUGAGACCUCAAGUGGGA",F, 3, 3, 8))

motA = "AAAAAAAAAAAAAA"
motB = "AAAAAAAAAAAAAUUUUUUUAAAAUUUAUUUU"

F = createNWMatrix(motA,motB)
print(motA + motB)
print(NeedlemanWunsch2(motA,motB,F))
