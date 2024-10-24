``` bash
class Animal {
  public name: string;
  public type: string;
 
  constructor(type: string, name: string) {
      this.name = name;
      this.type = type
  }
  voice() {
      console.log(`Cat ${this.name} says myau`);
  }
 
  transformToDog() {
      this.type = "Doggy";
  }
 
  ohNahnahWhatsMyName() {
    return this.name;
  }
 
}
 
const cat = new Animal("Cat", "Barsik");
// Transition animale
cat.transformToDog();
cat.voice();
 
const animalName = cat.ohNahnahWhatsMyName();
console.log("nom de l'animal après transformation : " + animalName);
```

``` mermaid
sequenceDiagram
participant PGM
participant Animal

PGM->>Animal: creer chat (cat, Barsik)
Animal->>PGM: Le chat Barsik
PGM ->> Animal : transformer chien
Animal ->> Animal : change To Dog
Animal ->> PGM : OK transformer chien
PGM ->> Animal : get voice (donner son nom)
Animal ->> Animal : nom + type après transformation
Animal ->> PGM : afficher nom +type
PGM ->> Animal : get your name
Animal ->> PGM : animal name
PGM ->> PGM :  nom de l'animal après transformation
```