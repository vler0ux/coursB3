## Cours infrastructure
les composants ppx :
- serveur
- reseaux
- stockage : NAS (netwotrk Attached Storage) partage de donnée SAN (Storage Area Network) accès à la volumetrie du systeme DAS (PC avec plein de stockage)
- sys expoitage
- securité

1U est une hauteur de serveur (standard)

pour les data Center, on a un onduleur specifique qui produit du courant stabilisé. le courant EDF va juste alimenter les bateries des onduleurs.

On essaie d'eviter les clims par un *free cooling*.  
Filtrage de l'air : poussière, encrassage.  
Dans les bonnes pratiques :  3 sauvegardes de la DATA/ 2 sauvegardes autres/ 1 copie sur site différent/ 1 sauvegarde froide, non accéssible/ 0 données exploitables après vos test.
la règle "3,2,1,1,0"

# Réseaux
### modèle OSI  
*couche materiel :* on a 7 couches, mais tout se passe dans les 4 premieres couches.    
- couche 1 : branchement
- couche 2 : adresse MAC
- couche 3: adresse IP
- couche 4 : ping

# Evaluer une structure infra :

_1. Serveurs_  
Coût moyen : 1 500 à 5 000 € par serveur
Total pour 2 serveurs : 3 000 à 10 000 €  

_2. Stockage_  : Disques durs (HDD ou SSD) : 100 à 500 € par disque
NAS ou SAN : 1 000 à 5 000 €  
Total : 1 500 à 7 000 €    

_3. Réseau_  
Routeur et pare-feu : 200 à 1 500 €
Switches : 100 à 1 000 €
Câblage réseau : 200 à 500 €
Total : 500 à 3 000 €

_4. Postes de travail :_
Ordinateurs de bureau : 600 à 1 200 € par unité
Total pour 10 postes : 6 000 à 12 000 €
  
_5. Sécurité_
Systèmes de sécurité physique : 500 à 2 000 €
Logiciels de sécurité : 300 à 1 000 €
Total : 800 à 3 000 €
  
_6. Alimentation_
Onduleurs (UPS) : 200 à 1 000 € par unité
Rack de distribution électrique : 100 à 500 €
Total : 300 à 1 500 €
  
_7. Climatisation_
Systèmes de climatisation : 1 000 à 5 000 €
Total : 1 000 à 5 000 €
  
_8. Logiciels_
Système d'exploitation serveur : 500 à 1 500 €
Logiciels de gestion et de sécurité : 500 à 2 000 €
Outils de sauvegarde : 300 à 1 000 €
  
**_Total : 1 300 à 4 500 €_**  

_9. Accessoires_  
Écrans, claviers et souris : 100 à 300 € par poste
Total pour 10 postes : 1 000 à 3 000 €  

_10. Formation et documentation_
Formation : 500 à 2 000 €
Documentation : 200 à 1 000 €
Total : 700 à 3 000 €  

_11. Services de support_
Contrats de maintenance : 500 à 2 000 € par an
Total : 500 à 2 000 €
  
**_Coût total estimé :_**
Minimum : Environ 15 300 €
Maximum : Environ 50 000 €
 
 ## Mon exemple :

_Détail des coûts estimés (pour une PME avec 20 To de stockage) :_

_1. Serveurs_  
Coût moyen : 1 500 à 5 000 € par serveur
Total pour 2 serveurs : 3 000 à 10 000 €  

_2. stockage_
NAS (5 baies) : environ 500 €.
5 disques de 4 To (HDD) : environ 5 x 100 € = 500 €.
Avantages : Centralisation des données, sécurité des données (RAID), accès à distance. Inconvénients : Coût initial plus élevé, nécessite une gestion/configuration.
Total : environ 1000 € pour 20 To.  

_3. Réseau_  
Routeur et pare-feu : 200 à 1 500 €
Switches : 100 à 1 000 €
Câblage réseau : 200 à 500 €
Total : 500 à 3 000 €

_5. Sécurité_
Systèmes de sécurité physique : 500 à 2 000 €
Logiciels de sécurité : 300 à 1 000 €
Total : 800 à 3 000 €
  
_6. Alimentation_
Onduleurs (UPS) : 200 à 1 000 € par unité
Rack de distribution électrique : 100 à 500 €
Total : 300 à 1 500 €
  
_7. Climatisation_
Systèmes de climatisation : 1 000 à 5 000 €
Total : 1 000 à 5 000 €
  
_8. Logiciels_
Système d'exploitation serveur : 500 à 1 500 €
Logiciels de gestion et de sécurité : 500 à 2 000 €
Outils de sauvegarde : 300 à 1 000 €


Récapitulatif des coûts pour la première année :
Matériel réseau : 4300 €
Licences et logiciels : 3200 €
Formations : 5500 €
Support et maintenance (annuel) : 12 430 €


*Exemple de coûts de matériel pour une PME :*

Routeur : 200 à 500 €.
Switch (24 ports, géré) : 300 à 800 €.

Points d'accès Wi-Fi : 100 à 300 € chacun (selon le nombre nécessaire).

Pare-feu : 500 à 1000 € (pour un pare-feu dédié).
Câblage Ethernet 

(installation) : Environ 3 à 5 € par mètre, plus le coût de l’installation.

Baie de brassage / armoires : 100 à 500 €.
Serveurs NAS : 500 à 1500 € (selon la capacité et les besoins).
Licences et logiciels : 3200 €
Formations : 5500 €
Support et maintenance (annuel) : 12 430 €


### Pour en savoir +

1. Stockage : Disques durs, SSD, NAS (Network Attached Storage)
 * Disques durs (HDD - Hard Disk Drive): pour des volumes de données importants, mais ils sont plus lents que les SSD.

Prix moyen : 20 à 40 €/To (Téraoctet).
Capacité : 1 To, 2 To, 4 To, 8 To et plus.
Exemples de coûts :
1 To : 40 à 60 €.
4 To : 100 à 150 €.
8 To : 200 à 300 €.  
Avantages : Grande capacité à faible coût. Inconvénients : Moins rapides, moins résistants aux chocs.

-  SSD (Solid State Drive)
Les SSD plus rapides que les disques durs, mais + coûteux pour des volumes importants.

Prix moyen : 90 à 150 €/To pour les SSD classiques (SATA), et environ 100 à 200 €/To pour les SSD NVMe (plus rapides).
Capacité : 500 Go, 1 To, 2 To et plus.
Exemples de coûts :

500 Go : 50 à 70 €.
1 To (SATA) : 90 à 130 €.
1 To (NVMe) : 110 à 150 €.
2 To (SATA) : 180 à 250 €.
Avantages : Très rapides, silencieux, résistants aux chocs. Inconvénients : Coût élevé par rapport aux disques durs.

-  NAS (Network Attached Storage)
Un NAS est un dispositif de stockage en réseau, souvent utilisé pour stocker, partager et sécuriser les données dans une entreprise. Il peut être configuré avec plusieurs disques durs (HDD ou SSD) et offre des fonctionnalités comme la sauvegarde automatique, l'accès à distance, et la redondance des données (RAID).

Prix moyen du NAS (sans disques) :
NAS 2 baies : 150 à 300 €.
NAS 4 baies : 300 à 600 €.
NAS 8 baies : 600 à 1000 €.
Coût total avec disques : Dépend des disques que tu y installes. Par exemple, un NAS 4 baies avec 4 disques de 4 To coûtera :

NAS (4 baies) : environ 400 €.
4 disques de 4 To (HDD) : environ 4 x 100 € = 400 €.
Total : environ 800 € pour 16 To.
Avantages : Centralisation des données, sécurité des données (RAID), accès à distance. Inconvénients : Coût initial plus élevé, nécessite une gestion/configuration.

## Généralisation de la virtualisation
### le Cloud Vs On-premise
 cout ? le cout est basé sur la consommation des ressources, pas de maintenance.  
Cout pour PME 1500 à 20k€ /an

- le type de cloud :  public/ privé/ hybride/ communautaire.
avantages: scabliT, reducion, cout, dispo, flex/  inconvenient : securité, fiabilité.

IAAS : Infrastrucuture as a service : prestataire fournit un accès à son infrastructure (deploiement d'applica web avec controle total)

PAAS : plateforme as a service (developpement sur un framework)

SAAS : software as a service.

CaaS : *containers as a service* est un mod de service cloud où le fourn gère l'infra necessaire pour executer, orchestrer et gerer les conteneurs (deployer, orchestrer, surperviser, mettre à l'échelle es applcations)

## La virtualisation 
- la machine virtuelle contient des fichiers : VDI, VBOX
- plusieurs type de hyperviseurs. **_Le Hyperviseur de Type 1_**: ex Kvm, VMware, Xen qui sont des noyaux linux, c'est un OS. **_Le hyperviseur de type 2_** : un syst exploitation qui se lance dans un OS ex : VirtualBox

accès au CPu de l'hote (modification/technolog)

# Distribution Linux 
- software distribution = création de logiciel
- GNU Linux

*Les licences*
elles st copyleft, donne la permission d'executer une copie du programme.
 - GPL copyleft fort
 - LGPL copyleft faible : je peux developper a fin commercial
 - AGPL (reseau)
 - EUPL


*LICENCE bsd* : c'est non copyleft

Dérivé : RedHat, Debian, Slackware, Gentoo, Atchlinux

proxy : va faire des requete sur `https`  
1 octet = 8 bits  
**_hachage : format pour conserver les mots de passe, qui ne se fera que dans un sens, ne pourra pas revenir en clair._**

`dpkg -l | grep ssh` pour voir les SSH
