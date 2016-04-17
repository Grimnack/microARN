import numpy as np
#TP microARN Matthieu Caron et Arnaud Cojez



def NWScore(X,Y) :
    '''
    return the last line of the Needleman-Wunsch score matrix
    '''
    # initialisation du tableau Score :
    Score = np.zeros((len(X),len(Y)))
    for j in range(len(Y)) :
        Score[0][j] = Score[0][j-1] + insertion(Y[j])
    for i in range(len(X)) :
        Score

def NeedlemanWunsch(X,Y) :
    pass

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
    