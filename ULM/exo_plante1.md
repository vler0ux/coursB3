```mermaid
sequenceDiagram

participant PGM
participant BDD_event 
participant BDD_planning_event_acclimate
actor user

PGM ->> BDD_event : get Nb event (userId)
BDD_event ->> PGM : nb user event 

alt NB event > 6
        PGM->> PGM: good user code promo 80%
    else Nb event<6
        PGM->>PGM: simple user code promo 20%
    end

PGM ->> BDD_planning_event_acclimate : consulter date_event_acclimate
BDD_planning_event_acclimate ->>PGM : return date

PGM ->> user : send next date event acclimate + code promo
```