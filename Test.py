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

def complem(chaine) :
    """Retourne le complémentaire du Mot"""
    res = ""
    for lettre in chaine :
        if lettre == 'A' :
            res+='U'
        elif lettre == 'U' :
            res+='A'
        elif lettre == 'G' :
            res+='C'
        else :
            res+='G'
    return res

def revCompl(chaine) :
    """Retourne le reverse complémentaire du Mot"""
    return reverse(complem(chaine))

def genereFichierTest(pathname,liaison=None) :
    '''
    ecris dans le fichier localisé en pathname
    '''
    if liaison is None :
        liaison = chaineAlea(24)
    f = open(pathname,'w')
    f.write("Donne de test\n")
    chaine = chaineAlea(100)
    chaine+= liaison
    chaine+= chaineAlea(5)
    chaine+= revCompl(liaison)
    chaine+= chaineAlea(100)
    f.write(chaine)
    f.close()

genereFichierTest("donneeTest.fasta","TGCACATGCACATGCACATGCACATGCACATGCACA")
