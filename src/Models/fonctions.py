#réaliser une fonction : centrale, edge. la fonction centrale remplace le bool en argument (a supprimer) teste si une cellule est la cellule centrale, idem pour edge.
#Neighbors : determine les voisisns d'une celleule (prend un tuple de coordonnees en argument)
#NeighborsAverage : prend en argument une cellule et calcule la moyenne de ses 6 voisins

def Init(beta, mat): #beta : background vapor level
    """float*array*bool->None
    Initialise toutes les cellules"""
    for i in mat[i, j]:
        for j in mat[i, j]:
            if Centrale(mat[i,j]):
                mat[i, j]=beta
            else:
                mat[i, j]=1


def Receptive(cell, mat): #mat sera definit avant
    """cell(tuple)*array->Bool
    Renvcoie True si la cellule est receptive, false sinon"""
    i, j = cell
    if mat[i, j]>=1:
        return True
    else:
        for k in Neighbors(k, l=cell):
            for l in Neighbors(k, l=cell):
                if Neighbors(k, l)>=1:
                    return True
    return False

def UpdateState(mat, alpha, gamma): #alpha : constante de diffusion, gamma : constante ajoutee (eau provenant d'autres cellules)
    """array*float*float-> None
    Met a jour l'etat et la valeur de chaque cellule"""
    for i in mat[i, j]:
        for j in mat[i, j]:
            if Receptive(mat[i, j], mat):
                mat[i, j]=(NeighborsAverage(mat[i,j])+alpha/12*NeighborsAverage(mat[i,j]))+(mat[i, j]+gamma) #on factorisera plus tard
                #on additionne partie participant a la diffusion + partie non diffusion
            else :
                mat[i, j]=(NeighborsAverage(mat[i,j])+alpha/12*NeighborsAverage(mat[i,j])-mat[i, j])