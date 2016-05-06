#TP microARN Matthieu Caron et Arnaud Cojez
import random as r


def randNucleotide() :
    '''
    envoie au hasard un des caractères suivant : AUGC
    '''
    test = r.random()
    if test<0.25:
        return 'A'
    if test<0.50:
        return 'C'
    if test<0.75:
        return 'G'
    return 'U'

def chaineAlea(taille) :
    chaine = ""
    for i in range(taille) :
        chaine += randNucleotide()
    return chaine

def reverse(chaine) :
    return chaine[::-1]

def genereFichierTest(pathname,liaison) :
    '''
    ecris dans le fichier localisé en pathname
    '''
    f = open(pathname,'w')
    f.write("Donne de test\n")
    chaine = chaineAlea(100)
    chaine+= liaison
    chaine+= chaineAlea(10)
    chaine+= reverse(liaison)
    chaine+= chaineAlea(100)
    f.write(chaine)
    f.close()

#genereFichierTest("donneeTest.fasta","TGCACATGCACATGCACATGCACATGCACATGCACA")
