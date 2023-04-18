# Projecte_MongoDB_Grup08
## Pràctica 1 Bases de Dades No Relacionals MatCAD
1. Judit Yebra Valencia, NIU: 1603614, Github user: JuditYebra, Contact: 1603614@uab.cat 
2. Pau Fuentes Hernández, NIU: 1600158, Github user: PauFuentes, Contact: 1600158@uab.cat 
3. Andrea Gonzalez Aguilera, NIU: 1603921, Github user: andreaagonzaalez, Contact: 1603921@uab.cat
4. Xavier Seminario Monllaó, NIU: 1603853, Github user: XavierSeminario, Contact: 1603853@uab.cat

## Introducció 
Aquest repositori conté el projecte de MongoDB que es duu a terme a la assignatura de Bases de Dades no Relacionals al grau de Matemàtica Computacional i Analítica de Dades.
## Pràctica 1 Bases de Dades No Relacionals MatCAD
1. Judit Yebra Valencia, NIU: 1603614, Github user: JuditYebra, Contact: 1603614@uab.cat 
2. Pau Fuentes Hernández, NIU: 1600158, Github user: PauFuentes, Contact: 1600158@uab.cat 
3. Andrea Gonzalez Aguilera, NIU: 1603921, Github user: andreaagonzaalez, Contact: 1603921@uab.cat
4. Xavier Seminario Monllaó, NIU: 1603853, Github user: XavierSeminario, Contact: 1603853@uab.cat

<p align="center">
<img src="https://github.com/PauFuentes/Projecte_MongoDB_Grup08/blob/master/logo.jpg", widht="300", height="300">
</p>

### Introducció
Aquest repositori conté el projecte de MongoDB que es duu a terme a l'assignatura de Bases de Dades no Relacionals al grau de Matemàtica Computacional i Analítica de Dades.

### Plantejament del problema
En aquest projecte es treballarà el disseny, la implementació i la consulta a una base de dades en MongoDB.A partir d'uns requisits i material relacionat amb la base de dades, s'haurà d'implementar un script en Python que processi i insereixi les dades en una base de dades de MongoDB. Posteriorment, s'haurà d'implementar en el disseny ja creat deu consultes de les quals es tenen els resultats, fent així un joc de proves.

### Part 1: Disseny ER
Per començar es disposa d'un diagrama Entitat-Relació, el qual proporciona la següent informació:
Es vol fer una base de dades que ens permeti emmagatzemar les publicacions de col·leccions de llibres de diferents editorials que disposa una tenda de còmics.
Una editorial crea col·leccions de publicacions. De fet, una mateixa col·lecció es pot crear en més d'una editorial.
Cada col·lecció està formada per diferents publicacions. A cada llibre hi apareixen diversos personatges. A més, aquests personatges poden aparèixer en més d'una publicació.
Finalment, es guardaran els artistes que han participat en la creació de les publicacions.
Amb aquesta informació que proporciona el diagrama s'han aplicat patrons de disseny per convertir el model a un conjunt de col·leccions i posteriorment s'ha editat l'Excel perquè es pugui treballar amb ell.

### Part 2: Implementació de l'script
Posteriorment s'ha implementat un script en Python main.py, el qual pren com a argument el fitxer Excel qui conté totes les dades.

### Part 3: Joc de Proves
Finalment s'han implementat les consultes dels jocs de proves en un script, i comprovat que els resultats siguin correctes.

