# Planete Event

Pouvoir faire des simulations de visites de planètes.

Tunnel d'achat : fidélisation

## Cas : le client a été malade lors d'un "event" et répond au questionnaire de satisfaction

### Diagramme de séquence

```mermaid
sequenceDiagram

participant PGM 
participant collection event
participant collection planning event acclimate
actor user

PGM ->> user : envoie enquete sat + userId
user ->> PGM : reponse malade
PGM ->> collection event : get Nb event (userId)
collection event->> PGM : nb user event 

alt NB event > 6
        PGM->> PGM: good user code promo 80%
    else Nb event<6
        PGM->>PGM: simple user code promo 20%
    end

PGM ->> collection planning event acclimate : consulter date next event acclimate
collection planning event acclimate ->>PGM : return date

PGM ->> user : send next date event acclimate + code promo
```

### Diagramme de Classe

```mermaid
classDiagram
collection_event: +userId
collection_event: +prix
collection_event: + get Nb event()
collection_planning_event_acclimate: +date next  event
collection_planning_event_acclimate : consulter next date()
```

### codage Typescript

``` typescript
class collection_event {
  public userId: string;
  public prix: int;
 
  constructor (userId: string, prix :int) {
      }

  get_nb_event() {

}}

class planning_event_acclimate{
  public userId: string;
  public prix: int;
 
  constructor (userId: string, prix :) {
      }

  get_nb_event() {

}}
 
```

## cas de la création d'un envoie de mail pour tester les nouvelles planètes pour un client 

### Diagramme de séquence
 
#### Envoie d'un mail avec les nouvelles planètes non effectuées
 
``` mermaid
sequenceDiagram
participant PGM
participant collection_event
participant collection_event_planete
actor user
 
PGM ->> collection_event : récupérer expérience client (idUser)
collection_event ->> PGM : expérience client
PGM ->> collection_event_planete : récupérer évènements non faits
collection_event_planete ->> PGM : évènements non faits
PGM ->> user : envoyer mail évènements non faits
```
 
### Diagramme de classes
 
``` mermaid
classDiagram
    collection_event : -int idUser
    collection_event : +checkExpClient()
    collection_event_planete : -string event
    collection_event_planete : +checkEventNotDone()
```