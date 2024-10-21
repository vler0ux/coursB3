#Tu as deux informations à ta disposition :

 #   sizes : un tableau qui présente les tailles des vaisseaux qui souhaitent s’amarrer à Alpha-Codix
#    maxCapacity : la capacité maximale que peut accueillir Alpha-Codix en terme de tailles de vaisseaux cumulées

#Les tailles doivent être traitées dans l’ordre initial de sizes.

#On cherche à savoir combien de vaisseaux ont pu s’amarré et la capacité restante après le passage du dernier vaisseau.

#Tu dois retourner ces 2 informations sous la forme : nbVaisseauxAmarrés_capacitéRestante

# NE PAS TOUCHER
sizes = [2, 6, 4, 1, 10, 7, 10, 7, 3, 9, 6, 10, 8, 2, 8, 10, 5, 7]
max_capacity = 99
# NE PAS TOUCHER

nbre_vaisseau = 0
place_restante=max_capacity

for vaisseau in sizes :
    if vaisseau <= place_restante:
        place_restante -= vaisseau
        nbre_vaisseau += 1

print (str(nbre_vaisseau)+"_"+str(place_restante))

