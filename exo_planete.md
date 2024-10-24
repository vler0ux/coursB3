## Envoie d'un mail avec les nouvelles planètes non effectuées

``` mermaid
sequenceDiagram
participant PGM
participant BDD client
participant BDD event Planete
actor user

PGM ->> BDD client : demande exp client
BDD client ->> PGM : récupère Exp client
PGM ->> BDD event Planete : demande OtherEvent
BDD event Planete ->> PGM : retour OtherEvent
PGM ->> user : envoie mail OtherEvent
```