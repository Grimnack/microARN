import numpy as np
#TP microARN Matthieu Caron et Arnaud Cojez



def NWScore(X,Y) :
    '''
    return the last line of the Needleman-Wunsch score matrix
    '''
    # initialisation du tableau Score :
    Score = np.zeros((len(X)+1,len(Y)+1))
    for j in range(1,len(Y)+1) :
        Score[0][j] = Score[0][j-1] + Ins(Y[j])
    for i in range(1,len(X)+1) :
        Score[i][0] = Score[i-1][0] + Del(X[i])
        for j in range(1,len(Y)+1) :
            scoreSub = Score[i-1][j-1] + Sub(X[i],Y[j])
            scoreDel = Score[i-1][j] + Del(X[i])
            scoreIns = Score[i][j-1] + Ins(Y[j])
            Score[i][j] = max(scoreSub,scoreIns,scoreDel)
    for j in range(len(Y)+1) :
        LastLine(j) = Score[len(X)][j]
    return LastLine


def needlemanWunsch (A, B):
    AlignmentA = ""
    AlignmentB = ""
    i = len(A)
    j = len(B)
    while (i > 0 or j > 0):
        if (i > 0 and j > 0 and F(i,j) == F(i-1,j-1) + S(Ai, Bj)):
            AlignmentA = A[i] + AlignmentA
            AlignmentB = B[j] + AlignmentB
            i = i - 1
            j = j - 1
        else if (i > 0 and F(i,j) == F(i-1,j) + d) :
            AlignmentA = A[i] + AlignmentA
            AlignmentB = "-" + AlignmentB
            i = i - 1
        else (j > 0 and F(i,j) == F(i,j-1) + d) :
            AlignmentA = "-" + AlignmentA
            AlignmentB = B[j] + AlignmentB
            j ← j - 1
    return (AlignmentA,AlignmentB)

def Hirschberg(X,Y) :
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
        (Z,W) = NeedlemanWunsch(X,Y)
    else :
        # ça peut foirer ici avec les entiers 
        tailleX = len(X)
        mid = int(tailleX/2)
        tailleY = len(Y)
        ScoreL = NWScore()
    