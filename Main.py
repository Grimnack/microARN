import numpy as np
#TP microARN Matthieu Caron et Arnaud Cojez

def Del(x):
    return -2

def Ins(y):
    return -2

def Sub(x,y) :
    if(x == y) :
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
    AlignmentA = ""
    AlignmentB = ""
    i = len(A) - 1
    j = len(B) - 1
    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + Sub(A[i], B[j])):
            AlignmentA = A[i] + AlignmentA
            AlignmentB = B[j] + AlignmentB
            i = i - 1
            j = j - 1
        elif (i > 0 and F[i][j] == F[i-1][j] + Del(A[i])) :
            AlignmentA = A[i] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i = i - 1
        elif (j > 0 and F[i][j] == F[i][j-1] + Ins(B[j])) :
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j] + AlignmentB
            j = j - 1
    return (AlignmentA,AlignmentB)

def PartitionY(ScoreL, ScoreR) :
    return np.argmax(ScoreL.extend(ScoreR[::-1]))

def Hirschberg(X,Y, F) :
    Z=""
    W=""
    if len(X) == 0 :
        for i in range(len(Y)) :
            Z = Z + '-'
            W = W + Y[i]
    elif len(Y) == 0 :
        for i in range(len(X)) :
            Z = Z + X[i]
            W = W + '-'
    elif len(X) == 1 or len(Y) == 1 :
        (Z,W) = NeedlemanWunsch(X,Y,F)
    else :
        # ça peut foirer ici avec les entiers
        tailleX = len(X)
        midX = int(tailleX/2)
        tailleY = len(Y)
        ScoreL = NWScore(X[1:midX], Y, F)
        ScoreR = NWScore(X[tailleX:midX+1:-1],Y[::-1], F)
        midY = PartitionY(ScoreL, ScoreR)
        h1 = Hirschberg(X[1:midX], Y[1:midY], F)
        h2 = Hirschberg(X[midX+1:tailleX], Y[midY+1:tailleY], F)
        (Z,W) = (h1[0] + h2[0], h1[1] + h2[1])
    return (Z,W)

def Hirschberg1(X,Y) :
    F = createNWMatrix(X,Y)
    return Hirschberg(X,Y,F)

# (resX, resY) = Hirschberg1("AGTACGCA", "TATGC")
# print(resX,resY)

print(createNWMatrix("ACTGTAG","ACGGCTAT"))