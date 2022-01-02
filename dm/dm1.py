## DM 4 d'informatique : Dichotomie

  ##Retour sur la recherche linéaire
  
    ##Exercice
    
    def appartient(e,L):
    return e in L

#1. 1
#2. 4
#3. 3

#3. Il fera au minimum une comparaison et au maximum n comparaisons, il faut privilégier le minimum de
#comparaisons afin d'obtenir un programme rapide.

#4. 10^11/10^9=100 secondes


  ##Dichotomie
    ##Exercice
    
    def croissant(L):
    for i in range (len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True
  
      ##Exercice

# Il y a eu 4 comparaisons dans cet exemple. C'est moins que si l'on avait utilisé appartien(e,L)qui en aurait utilisé 11. La dichotomie est donc plus efficace.

    ##Exercice
  
  def dichotomie(e, L):
    i, j = 0, len(L) - 1  
    while i<=j: 
        m =(i+j)//2 # milieu de i et j
        if e < L[m]:
            j=m-1 # regarder dans la partie gauche
        elif e > L[m]:
            i=m+1 # regarder dans la partie droite
        else:
            return True
    return False


L1, L2, L3 = [0, 2], [0, 2, 5], [-2, 1, 2, 4, 6, 7, 8, 9, 11, 12, 14, 15, 18, 22, 54]
assert (dichotomie(0, L1) and not dichotomie(1, L1))
assert (dichotomie(5, L2) and not dichotomie(7, L2))
assert (dichotomie(14, L3) and not dichotomie(-4, L3))

    ##Exercice
  
  #1.1e-08
  
  
##Exponentiation rapide

      ##Exercice
  
#1.  def puissance(a,n):
    p=1
    for i in range (n):
        p=p*a
    return p
puissance(2,9)

#2. La fonction précédente réalise n-1 multiplications

      ##Exercice
  #1. 
  #puissance_rapide(2,12) 

#Valeurs rentrées :(r=1;a=2;n=12)/// A chaque passage dans le while on remplace n par son quotient dans la division euclidienne par 2

#n=12 est différent de 0 et pair alors on multiplie 2 par 2(a*a) (r=1;a=4;n=6)
#n=6 est différent de 0 et pair alors on multiplie 4 par 4 (a*a)(r=1;a=16;n=3)
#n=3 est différent de 0 mais est impair alors on multiplie 1 par 16(r*a) puis 16 par 16 (a*a)(r=16;a=256;n=1)
#n=1 est différent de 0 mais est impair alors on multiplie 16 par 256(r*a) puis 256 par 256 (a*a)(r=4096;a=65536;n=0)
#Le programme renvoie enfin r=4096

#2. 
#On réalise dans cet exemple 6 multiplications
#On en aurait réalisé 11 avec la première fonction

#3.
'''Regardons une étape de la boucle while en fonction de la parité de n.
Si n est pair : 
    r*a^n devient r*(a*a)^(n/2)= r*(a^2)^(n/2)=r*a^n
Si n est impair :
    r*a^n devient (r*a)*(a*a)^(n/2 - 1/2)=(r*a)*(a^2)^((n-1)/2)=(r*a)*a^(n-1)=r*a^n
    
Dans tous les cas, r*a^n reste inchangé lorsque le programme parcourt la boucle while

puissance_rapide(a, n) renvoie la valeur de r après la boucle while. Or après la boucle while, n=0.
On a donc a^n=a^0=1 . Donc on a r=ra^n.
Or ra^n reste constant malgré la boucle while donc ra^n à la fin de la boucle while est égal à ra^n au début de la boucle.
Or au premier passage de la boucle, r=1 donc ra^n=a^n
Au total la fonction renvoie a^n'''

#4. 
def puissance_rapide(a, n):
    r = 1
    while n != 1:
        if n % 2 == 1:
            r = r * a
        a = a * a
        n = n // 2
    return a*r
puissance_rapide(2,12)














## DM 5 d'informatique : Récursivité
  ##Principe général
    #Exercice
    '''La fonction renverra 1,2,3,4,5'''
    
def f(n):  # exemple de fonction récursive
    if n == 0:
        return
    f(n-1)
    print(n)
f(5)
1
2
3
4
5


    #Exercice
  def dessin(n):
    if n==0:
        return
    print(n*"*", end="")
    print()
    dessin(n-1)
    
    #Exercice
    def dessin2(n,k):
    if n==k:
        return
    print(k*"*", end="")
    print()
    dessin2(n,k+1)
    print(k*"*", end="")
    print()
    
    
    
  ##Applications simples
  
    #Exercice
    def somme(n):
    t=0
    for i in range (n+1):
        t=t+i**2
    return(t)

  
  #Exercice
  #1. 
  #n!=(n-1)!*n

#2.
def fact(n):
    if n==0:
        return 1
    return fact(n-1)*n
    
    
    
  ##Dichotomie en récursif
    #Exercice
    
    def dichotomie(e,L,i,j):
    i,j=0,len(L)
    while i<=j:
        
        m=(i+j)//2
        if e<L[m]:
            return dichotomie(e,L,i,m-1)
        elif e>L[m]:
            return dichotomie(e,L,m+1,j)
        else:
            return True
    return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    ## DM 6 d'informatique : Dessin de fractale
    
      ##matplotlib
      
        #Exercice
        
import matplotlib.pyplot as plt

def segment(p,q):
    plt.plot([p[0],q[0]],[p[1],q[1]]);

segment((3, 7), (4, 5))
plt.show()
    

      #Exercice
    
import numpy as np
X, Y = [], []
for i in range (10000):
    X.append(i*0.001)
    Y.append(X[i]+np.cos(X[i]))
plt.plot(X,Y)
plt.show()



  ##Rotation
  
    #Exercice
    
import numpy as np

def rotation(r,d,a):
    return(r[0]+d*np.cos(a),r[1]+d*np.sin(a))
  
  
  
  #Exercice
  
  import matplotlib.pyplot as plt
def segment(p,q):
    plt.plot([p[0],q[0]],[p[1],q[1]]);
    plt.axis("equal")





segment((0,0),rotation((0,0),1,np.pi/2))

plt.show()




  ##Fractale
    #Exercice
    
import numpy as np
import matplotlib.pyplot as plt

def rotation(r,d,a):
    return(r[0]+d*np.cos(a),r[1]+d*np.sin(a))

def segment(p,q):
    plt.plot([p[0],q[0]],[p[1],q[1]]);
    plt.axis("equal")




def arbre(r, d, a, n):
    if n == 0: # cas de base : on arrête les appels récursifs
        return
    segment(r,rotation(r,d,a)) # dessiner le tronc
    arbre(rotation(r,d,a),d/1.2,a+np.pi/2,n-1) # dessiner le sous-arbre gauche
    arbre(rotation(r,d,a),d/1.2,a-np.pi/6,n-1) # dessiner le sous-arbre droit

