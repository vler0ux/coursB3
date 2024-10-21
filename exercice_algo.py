#Une mêlée est composée de 8 joueurs, répartis sur 3 lignes :

#    3 joueurs sur la première ligne
#    4 joueurs sur la deuxième ligne
#    1 dernier joueur sur la troisième et dernière ligne

#Tu vas devoir calculer la puissance de la mêlée à l’impact !
#Règles

#Les joueurs sont répartis dans 3 tableaux line1, line2 et line3.

#Chaque joueur est défini par son poids et sa force, ce sont deux entiers, séparés par « : ».

#L’impact de chaque joueur est égal à son poids multiplié par sa force.

#Mais…

 #   La première ligne a un coefficient supplémentaire de 1,5
#    La troisième ligne a un coefficient supplémentaire de 0,75

# Pour les calculs, l’impact de chaque joueur doit être arrondi à l’entier inférieur, après application du coefficient.

# Tu dois retourner l’impact total de la mêlée, c’est à dire la somme des impacts de chaque joueur.

# NE PAS TOUCHER
line1 = ['100:60', '102:99', '104:27']
line2 = ['88:99', '94:10', '105:17', '96:37']
line3 = ['90:34']
# NE PAS TOUCHER

def get_force(line, facteur=1):
    force_total = 0
    for joueur in line :
        poidStr, forceStr  = joueur.split (":")
        force = int(poidStr)*int(forceStr)
        force_total += force
    return force_total*facteur

print(get_force(line1))

print(line1[0].split(':'))

forceline1= get_force(line1)
forceline2= get_force(line2)
forceline3= get_force(line3)

res= forceline1+forceline2+forceline3
print(res)
            