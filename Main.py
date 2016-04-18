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
    if (x == 'A' and y == 'U') or (x == 'U' and y == 'A') :
        return 2
    elif (x == 'G' and y == 'C') or (x == 'C' and y == 'G') :  
        return 2
    elif (x == 'G' and y == 'U') or (x == 'U' and y == 'G') :
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

# def NeedlemanWunsch (A, B, F):
#     '''
#     Remonte la matrix score F pour trouver le meilleur alignement possible
#     entre les mots A et B
#     '''
#     AlignmentA = ""
#     AlignmentB = ""
#     i = len(A) 
#     j = len(B) 
#     while (i > 0 or j > 0):
#         if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + Sub(A[i-1], B[j-1])):
#             AlignmentA = A[i-1] + AlignmentA
#             AlignmentB = B[j-1] + AlignmentB
#             i = i - 1
#             j = j - 1
#         elif (i > 0 and F[i][j] == F[i-1][j] + Del(A[i-1])) :
#             AlignmentA = A[i-1] + AlignmentA
#             AlignmentB = "-" + AlignmentB
#             i = i - 1
#         elif (j > 0 and F[i][j] == F[i][j-1] + Ins(B[j-1])) :
#             AlignmentA = "-" + AlignmentA
#             AlignmentB = B[j-1] + AlignmentB
#             j = j - 1
#     return (AlignmentA,AlignmentB)


def NeedlemanWunsch2(A, B, F):
    '''
    Remonte la matrix score F pour trouver le meilleur alignement possible
    entre les mots A et B
    '''
    cptMatch = 0
    AlignmentA = ""
    AlignmentB = ""
    i = len(A) 
    j = len(B) 
    while (i > 0 or j > 0):
        resSub = Sub(A[i-1], B[j-1])
        if resSub == 2 :
            cptMatch = cptMatch + 1
        if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] +scoreSub):
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
    return (AlignmentA,AlignmentB,cptMatch)


def rechercheMicroARN(ARN,tailleMax) :
    longueurARN = len(ARN)
    for i in range(longueurARN-tailleMax*2) :
        motActuel = ARN[i:i+tailleMax-1]
        for j in range(i+tailleMax,longueurARN-tailleMax) :
            motCompare = ARN[j:j+100]
            F = createNWMatrix(motActuel,motCompare)
            (AlignmentA,AlignmentB,cptMatch) = NeedlemanWunsch2(motActuel,motCompare,F)



(resX, resY) = Hirschberg1("AGTACGCA", "TATGC")
print(resX,resY)

# F = createNWMatrix("ACTGTAG","ACGGCTAT")
# print(NeedlemanWunsch("ACTGTAG","ACGGCTAT",F))