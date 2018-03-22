+ Problems : each step
  + Display all the cells
  + compute all the cells



# Controllers

Le contrôleur est (pour l'instant) équivalent à la grille. Il stocke une grille encapsulée dans un objet HexaGrid.

HexaGrid possède les méthodes publiques suivantes :

+ update(ijk, data)
  + Mets à jour une case en (i,j,k) avec data
  + ijk : tuple des coordonnées hexagonales
  + data : dictionnaire de données
+ gridToHexa()
  + Renvoie la grille au format hexagonal pour les Models
+ gridToMatrix()
  + Renvoie la grille au format matriciel pour les Views

# Models

+ variables
  + alpha : constante de diffusion
  + beta : niveau de vapeur
  + gamma : constante d'addition de vapeur
  + step : compteur du nombre d'étapes (temps discret)
+ InitHexaGrid() 
  + initialisation de la grille
+ udpate(hexaGrid)
  + Mets à jour la grille hexagonale selon les règles du Modèle
  + hexaGrid : Type Grid
+ getNeighbors(hexaGrid, ijk)
  + Generator des voisins de la cellule en (i,j,k)
  + hexaGrid : Type Grid
  + ijk : tuple des coordonnées hexagonales

# Views

+ display(matrixGrid)
  + Affiche la grilles des pixels
  + matrixGrid : Type Grid
