## Importation des bibliothèques utiles
import matplotlib.pyplot as plt
import random


## Définition de la taille du labyrinthe par l'utilisateur
print(" Projet informatique : génération aléatoire de labyrinthes,  MALLEVAYS Lucas et SION Emmanuel", "\n")
m=int(input("Hauteur du labyrinthe : "))
n=int(input("Largeur du labyrinthe : "))

print("Veuillez attendre la génération du labyrinthe...")








def Liste_Dispo(i,j,t,L1,T,m,n):
    '''prend en entrée des float et renvoie une liste de cases disponibles en fonction des coordonnées des cases'''

    Liste_CasesVoisines_Disponibles=[]
    if i>0 and L1[i-1][j] and T[i-1][j]!=t:
        Liste_CasesVoisines_Disponibles = Liste_CasesVoisines_Disponibles+[[i-1,j]]
    if i<m-1 and L1[i+1][j] and T[i+1][j]!=t:
        Liste_CasesVoisines_Disponibles = Liste_CasesVoisines_Disponibles+[[i+1,j]]
    if j>0 and L1[i][j-1] and T[i][j-1]!=t:
        Liste_CasesVoisines_Disponibles = Liste_CasesVoisines_Disponibles+[[i,j-1]]
    if j<n-1 and L1[i][j+1] and T[i][j+1]!=t:
        Liste_CasesVoisines_Disponibles = Liste_CasesVoisines_Disponibles+[[i,j+1]]
    return Liste_CasesVoisines_Disponibles






def Abat_Mur(Liste_CasesVoisines_Disponibles,i,j,t,L1,L2,T):
    ''' prend en entrée la liste de cases voisines disponibles, les listes des murs et des float. 
        Cette fonction abat les murs et réindexe les tableaux des coordonnées des cases'''

    w=len(Liste_CasesVoisines_Disponibles)  
    if w>0:
        # Si il il y a des cases voisines disponibles :
        q=random.randint(0,w-1)
        # On prend une case dans cette liste au hasard et on compare les coordonnées avec la case d'avant
        i0=Liste_CasesVoisines_Disponibles[q][0]
        j0=Liste_CasesVoisines_Disponibles[q][1]
        #On abat les murs si les conditions sont respectées
        if i0<i:
            L1[i0][j]=False
        elif i0>i:
            L1[i][j]=False
        elif j0<j:
            L2[i][j0]=False
        elif j0>j:
            L2[i][j]=False
        # On réindexe les coordonnées
        t0=T[i0][j0]
        if t<t0:
            a=t
            b=t0
        else:
            a=t0
            b=t
        for g in range(m):
            for h in range(n):
                if T[g][h]==b:
                    T[g][h]=a





# On définit en tout premier lieu le labyrinthe, et on définit l'entrée en bas à gauche et la sortie en haut à droite (c'est arbitraire)
def Labyrinthe(m,n):
    ''' prend en entrée 2 float et crée 2 listes de murs : verticaux (L2) et horizontaux (L1);
        False = mur qui est abattu'''

    L1=[n*[True] for k in range(m)]
    L2=[n*[True] for k in range(m)]
    L1[m-1][0]=False
    L2[0][n-1]=False

# On définit le tableau pour compter les cases
    T=[n*[0] for k in range(m)]
    cases=0
    for i in range(m):
        for j in range(n):
            T[i][j] = cases
            cases = cases+1
# On définit la liste des coordonnées des cases
    L_Cases=[]
    for i in range(m):
        for j in range(n):
            L_Cases = L_Cases+[[i,j]]

# Si le nombre de cases est positif, c'est à dire si il y a des cases dans le labyrinthe :
    while cases>0:
        p = random.randint(0,cases-1)
        i = L_Cases[p][0]
        j = L_Cases[p][1]
        t = T[i][j]

        Liste_CasesVoisines_Disponibles=Liste_Dispo(i,j,t,L1,T,m,n)
        Abat_Mur(Liste_CasesVoisines_Disponibles,i,j,t,L1,L2,T)

# Si il n'y a pas de cases disponibles, on supprime l'élément que l'on a choisi
        if len(Liste_CasesVoisines_Disponibles)<1:
            L_Cases.pop(p)

# On attribue à cases une nouvelle valeur
        cases=len(L_Cases)
    return L1,L2






def ResolutionLabyrinthe(L1,L2):
    ''' prend en entrée 2 listes L1 et L2 et on souhaite résoudre le labyrinthe'''

    m=len(L1)
    n=len(L1[0])
    T=[n*[0] for k in range(m)]
    T[m-1][0]=1
    k=1
    while T[0][n-1]==0:
        for i in range(m):
            for j in range(n):
                if T[i][j]==0:
                    Bn = i>0 and T[i-1][j]==k and not L1[i-1][j]
                    Bs = i<m-1 and T[i+1][j]==k and not L1[i][j]
                    Be = j>0 and T[i][j-1]==k and not L2[i][j-1]
                    Bw = j<n-1 and T[i][j+1]==k and not L2[i][j]
                    if Bn or Bs or Be or Bw:
                        T[i][j]=k+1
        k=k+1
    Solution=[[0,n-1]]
    i = 0
    j= n-1
    while k>1:
        if i>0 and T[i-1][j]==k-1 and not L1[i-1][j]:
            i = i-1
            j = j
        elif i<m-1 and T[i+1][j]==k-1 and not L1[i][j]:
            i = i+1
            j = j
        elif j>0 and T[i][j-1]==k-1 and not L2[i][j-1]:
            i = i
            j = j-1
        elif j<n-1 and T[i][j+1]==k-1 and not L2[i][j]:
            i = i
            j = j+1
        # on rajoute la solution à la liste des solutions
        Solution=[[i,j]]+Solution
        # On enlève cette solution au nombre total de solution
        k-=1
        #print(Solution)
    return Solution






def AffichageLabyrinthe(L1,L2):
    ''' prend en entrée 2 listes L1 et L2 et on souhaite afficher le labyrinthe'''

    m=len(L1)
    n=len(L1[0])
# On affiche tous les murs du tableau, en noir avec le "b", et d'épaisseur 4
    plt.plot([0,0,n],[0,m,m], color="b", linewidth=4)
# On parcourt les tableaux et on affiche les murs à droite et en haut
    for i in range(m):
        for j in range(n):
            if L1[i][j]:
                plt.plot([j,j+1], [m-1-i,m-1-i], color="b", linewidth=4)
            if L2[i][j]:
                plt.plot([j+1,j+1], [m-i,m-1-i], color="b", linewidth=4)








def AffichageSolution(Solution):
    ''' prend en entrée la liste de solutions et on souhaite afficher la solution du labyrinthe;
        on se place à 0,5 pour être au milieu de la case'''

    X=[0.5]
    Y=[0]
    for S in Solution:
        X.append(0.5+S[1])
        Y.append(m-0.5-S[0])
    X.append(n)
    Y.append(m-0.5)
    plt.plot(X,Y, color="r", linewidth=4)








Longueur,Largeur=Labyrinthe(m,n)


# Affichage du labyrinthe créé avec l'algorithme
plt.figure(figsize=(8,8))
AffichageLabyrinthe(Longueur,Largeur)
plt.axis("equal")
plt.axis("off")
plt.title("Labyrinthe créé à l'aide de l'algorithme")
plt.show()


# Affichage de la solution ou non par l'utilisateur
print("\n")
sol = input('Voulez - vous afficher la solution du labyrinthe ? : ')

if sol=='oui' or sol=='Oui':
    print("Veuillez attendre la génération de la solution...")
    Solution=ResolutionLabyrinthe(Longueur,Largeur)
    plt.figure(figsize=(8,8))
    AffichageLabyrinthe(Longueur,Largeur)
    AffichageSolution(Solution)
    plt.axis("equal")
    plt.axis("off")
    plt.title('Solution du labyrinthe')
    plt.show()

# Fin du jeu
print("\n", end='Fin, veuillez relancer le programme')




