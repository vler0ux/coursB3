#Tu as à ta disposition 4 informations :

#    shipsFirstPeriod : les vaisseaux qui souhaitent s’amarrer en première partie de (ta) journée
#    shipsSecondPeriod : les vaisseaux qui souhaitent s’amarrer en deuxième partie de (ta) journée
#    shipsThirdPeriod : les vaisseaux qui souhaitent s’amarrer en troisième partie de (ta) journée
#    shipsMax : la capacité maximale de Alpha-Codix

#On cherche à savoir s’il y a assez de place pour tout le monde.

#Tu dois retourner :

 #   S’il y a assez de places : « OK :  » et le nombre de places restantes
#    S’il n’y a pas assez de places : « KO :  » et le nombre de places manquantes


# NE PAS TOUCHER
ships_first_period = 7
ships_second_period = 10
ships_third_period = 6
ships_max = 17
# NE PAS TOUCHER

somme = ships_first_period+ships_second_period+ships_third_period
calcul_place = ships_max -somme
if calcul_place > 0 :
    print ("OK : " ,calcul_place)
else :
    print ("KO :",calcul_place )