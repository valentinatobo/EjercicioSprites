# APLICACIÓN DE PATRONES CREACIONALES :hammer: :octocat:


La idea principal del proyecto es gestionar un tablero de presentación de personajes de un juego, los cuales se podran ver desde diferentes perspectivas tanto laterales, como el frente, de espaldas y adicionalmente una acción a realizar, para el desarrollo de este programa se debe poner en practica dos patrones creacionales: Builder y Abstract Factory, empleandolos en la creación como tal del personaje.

## DIAGRAMA DE CLASES DEL PROYECTO 


## ¿Qué son los Patrones Creacionales? :triangular_ruler:

Los patrones de creación abstraen la forma en la que se crean los objetos, permitiendo tratar las clases a crear de forma genérica dejando para más tarde la decisión de qué clases crear o cómo crearlas.

Abstraen el proceso de instanciación, encapsulan conocimiento sobre qué clases concretas utiliza el sistema, independizan al sistema del modo en que se crean, componen y representan los objetos, flexibilizan el qué, quién, cómo y cuándo.

## Abstract Factory :factory:

### ¿Qué es Abstract Factory?
Es un patrón de creación que provee una interfaz para crear familias o conjuntos de objetos(productos) relacionados o que dependen entre sí, sin especificar sus clases concretas.

### ¿Como se implemento?

En el proyecto se puede evidenciar el uso de este patrón cuando creamos los productos que contienen la vista de cada personaje(frente, atras, derecha e izquierda) que en este caso seran las imagenes del sprite,  estos los tomara la fabrica del personaje y los unira para el proceso de creación del mismo genrando asi la fabrica de cada personaje con sus vistas respectivas.

## Builder  :clapper: :construction_worker:

### ¿Qué es Builder? 
Patrón creacional que permite la creación de un objeto complejo, a partir de una variedad de partes que contribuyen individualmente a la creación y ensamblación del objeto mencionado. Hace uso de la frase "divide y conquistarás". Por otro lado, centraliza el proceso de creación en un único punto, de tal forma que el mismo proceso de construcción pueda crear representaciones diferentes.

### ¿Como se implemento?
Para este caso tendremos clases constructores de cada personaje los cuales tendran relación directa con la fabrica respectiva, tendremos una clase director que sera la encargada de ensamblar las partes entregadas por el constructor y crear el objeto como tal que en este caso es nuestro personaje.

## Autores

* **Diana Valentina Uscategui Tobo - 20172020063
* **Edwin Andres Salinas Chaparro - 20172020087
