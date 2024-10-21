# Algorithmie – Bonnes pratiques Python
En algorithmie, et en programmation d’une manière générale, adopter de bonnes pratiques est essentiel pour concevoir des algorithmes clairs, efficaces et faciles à comprendre. Cela facilite non seulement la lecture et la maintenance du code mais également la collaboration avec d’autres membres de son équipe.

Si tu as déjà beaucoup codé, cette liste te paraitra peut être « évidente » ou « triviale », mais il y a sans doute quelques éléments à découvrir et n’hésite pas à la voir comme une check list à garder en tête pendant que tu codes 😉

On alternera à chaque fois un bout de code et les explications qui vont avec.

Voici donc 9 bonnes pratiques en Python :

    1. Utiliser des noms de variables clairs et significatifs
    2.Utilisation de constantes
    3.Utiliser la bonne boucle
    4.Eviter les else inutiles
    5.Ecrire des fonctions pour réutiliser son code
    6.Commenter son code
    7.Diviser les problèmes en sous problèmes
    8.Tester l’algorithme avec différents cas
    9.Ce n’est pas un concours du code le + court
    Bonus : autres langages

## Noms de variables clairs et significatifs en Python

### Mauvais exemple
```
a = 90  
b = 45 
c = a - b
```

### Bon exemple
```
total_match_time = 90  
half_time_duration = 15  
effective_play_time = total_match_time - half_time_duration`
```
Explications :

En utilisant des noms de variables explicites, écrites en **_snake_case_**, ton code devient plus lisible et facile à comprendre. Dans le bon exemple, les noms **_total_match_time_**, **_half_time_duration_** et **_effective_play_time_** décrivent clairement leur rôle, ce qui facilite la compréhension du code pour toi et pour les autres.

Il n’y a ni limite ni besoin d’abréviation lorsqu’on nomme une variable, une fonction, une classe, une méthode, etc.
## Les constantes en Python

### Mauvais exemple
```circle_area = 3.14159 * radius ** 2```

### Bon exemple
```
PI = 3.14159
circle_area = PI * radius ** 2
```
Explications :

En Python, il n’existe pas de mot-clé const ou autre pour définir des constantes. Par convention, les constantes sont définies en majuscules avec des underscores pour séparer les mots. Les constantes sont généralement définies au niveau du module (en dehors des fonctions et des classes).

Les constantes te permettent de définir des valeurs fixes et réutilisables. En définissant PI, tu évites les erreurs liées à la réécriture de la valeur et facilites les modifications ultérieures.
## La bonne boucle en Python

### Mauvais exemple (utilisation de while pour un nombre connu d'itérations)
```
i = 0
while i < 11:
    print(f"Joueur numéro {i} est sur le terrain.")
    i += 1
```
### Bon exemple (utilisation de for pour un nombre connu d'itérations)
```
for i in range(11):
    print(f"Joueur numéro {i} est sur le terrain.")
```
Explications :

Choisir la boucle appropriée rend ton code plus clair et plus efficace. Utilise une boucle for lorsque tu connais à l’avance le nombre d’itérations. D’autant qu’une boucle while peut entrainer une boucle infinie !
## Eviter les else inutiles en Python

### Mauvais exemple
```
def check_qualification(score):
    if score >= 10:
        print("Tu es qualifié pour la finale.")
    else:
        print("Tu n'es pas qualifié.")
```
### Bon exemple
```
def check_qualification(score):
    if score < 10:
        print("Tu n'es pas qualifié.")
        return
    print("Tu es qualifié pour la finale.")
```
Explications :

En éliminant les else inutiles, tu simplifies ton code et le rends plus lisible. En retournant ou en sortant de la fonction dès que possible, tu évites les conditions imbriquées et facilites la compréhension du flux logique.
## Ecrire des fonctions pour réutiliser son code

### Mauvais exemple
```
athlete1_speed_kmh = (100 / 9.58) * 3.6
athlete2_speed_kmh = (100 / 9.80) * 3.6
```
### Bon exemple
```
def calculate_speed_kmh(distance_meters, time_seconds):
    return (distance_meters / time_seconds) * 3.6

athlete1_speed_kmh = calculate_speed_kmh(100, 9.58)
athlete2_speed_kmh = calculate_speed_kmh(100, 9.80)
```
Explications :

En créant des fonctions pour les opérations répétitives, tu rends ton code plus modulable et facile à maintenir. Dans cet exemple, la fonction calculate_speed_kmh te permet de calculer la vitesse en km/h de n’importe quel athlète en fonction de la distance et du temps, sans répéter le calcul à chaque fois !
## Commenter son code

Pas d’exemple de code ici.

Le but n’est pas de commenter pour commenter mais de prendre le temps d’écrire les commentaires avant de coder, pour expliciter la portion de code qui arrive, à quoi elle sert, comment elle fonctionne, etc. Cela permet d’écrire le plan du code à produire, avant de le produire !

J’en parle dans la vidéo : méthodologie pour résoudre un challenge de code (à partir de 4min27, c’est du PHP mais ça ne change rien au principe)
## Diviser les problèmes en sous problèmes

### Mauvais exemple (fonction monolithique)
```
def get_team_statistics(team):
    total_points = 0
    total_assists = 0
    for player in team:
        total_points += player['points']
        total_assists += player['assists']
    average_points = total_points / len(team)
    average_assists = total_assists / len(team)
    print(f"Points moyens par joueur : {average_points}")
    print(f"Passes décisives moyennes par joueur : {average_assists}")
```
### Bon exemple (division en sous-fonctions)
```
def calculate_total(team, stat):
    return sum(player[stat] for player in team)

def calculate_average(total, count):
    return total / count if count else 0

def display_team_statistics(average_points, average_assists):
    print(f"Points moyens par joueur : {average_points}")
    print(f"Passes décisives moyennes par joueur : {average_assists}")

def get_team_statistics(team):
    total_points = calculate_total(team, 'points')
    total_assists = calculate_total(team, 'assists')
    average_points = calculate_average(total_points, len(team))
    average_assists = calculate_average(total_assists, len(team))
    display_team_statistics(average_points, average_assists)
```
En divisant un problème complexe en sous-problèmes, tu rends ton code plus facile à gérer et à comprendre. Chaque fonction a une responsabilité spécifique, ce qui facilite les tests, car tu pourras tester les fonctions une par une et non tout le programme à la fois. C’est pareil pour la maintenance, tu vas pouvoir faire évoluer ou optimiser ton code portion par portion.

Tu peux retrouver des méthodes pour réfléchir au découpage d’un algorithme.
## Tester son algorithme avec différents cas

Pas d’exemple de code ici.

Le but est de rappeler que bien souvent, le diable se cache dans les détails ! Ou plutôt que les bugs se cachent dans les cas particuliers ! Alors prends le temps d’analyser ton code et de définir les cas principaux et, surtout, les cas particuliers qui te permettront de déterminer si ton code est correct ou non.

Par « cas », j’entends un ensemble de données cohérentes entre elles qui sont susceptibles d’être des paramètres d’entrée de ton code.

Et quand on parle de tests, on ne peut pas ne pas parler de tests unitaires. Donc n’hésite pas à découvrir ce que sont les tests unitaires et comment en réaliser en python (des contenus dédiés arrivent sur Tainix, en attendant, Google et ChatGPT sont tes amis 😉 )
## Le code le + court, une fausse bonne idée

### Mauvais exemple (code condensé et peu lisible)
```
total_score = sum([p['points'] for p in players if p['trophies'] > 2])
```
### Bon exemple (code clair et bien formaté)
```
total_score = 0
for player in players:
    if player['trophies'] > 2:
        total_score += player['points']
```
Explications :

L’exemple ici est un peu extrême ! Mais fais attention aux ternaires qui s’enchainent, aux conventions non respectées, aux variables mal nommées, etc. Sur l’instant, le code parait clair et intelligent… mais quand on revient dessus quelques jours plus tard, bien souvent on y comprend plus rien !
