"""
/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */
"""

preguntas_respuestas = [
    {
        "pregunta": "¿Qué cualidad valoras más en ti mismo?",
        "respuestas": {
            "a": "Valentía",
            "b": "Astucia",
            "c": "Lealtad",
            "d": "Inteligencia"
        }
    },
    {
        "pregunta": "¿Qué animal te representa mejor?",
        "respuestas": {
            "a": "León",
            "b": "Serpiente",
            "c": "Tejón",
            "d": "Águila"
        }
    },
    {
        "pregunta": "¿Qué tipo de tarea prefieres realizar?",
        "respuestas": {
            "a": "Una aventura emocionante",
            "b": "Algo que te permita alcanzar tus objetivos, sin importar los medios",
            "c": "Ayudar a los demás en lo que necesiten",
            "d": "Resolver acertijos y enigmas difíciles"
        }
    },
    {
        "pregunta": "¿Qué lugar te atrae más?",
        "respuestas": {
            "a": "Un campo abierto y soleado",
            "b": "Un bosque oscuro y misterioso",
            "c": "Un hogar cálido y acogedor",
            "d": "Una biblioteca silenciosa y llena de conocimiento"
        }
    },
    {
        "pregunta": "¿Qué crees que es más importante para alcanzar el éxito?",
        "respuestas": {
            "a": "Coraje",
            "b": "Ambición",
            "c": "Lealtad",
            "d": "Inteligencia"
        }
    }
]


class User:
    def __init__(self):
        self.gryffindor = 0
        self.slytherin = 0
        self.hufflepuff = 0
        self.ravenclaw = 0

    def addGryffindor(self):
        self.gryffindor += 1

    def addSlytherin(self):
        self.slytherin += 1

    def addHufflepuff(self):
        self.hufflepuff += 1

    def addRavenclaw(self):
        self.ravenclaw += 1

    def getHouse(self):
        houses = {
            "Gryffindor": self.gryffindor,
            "Slytherin": self.slytherin,
            "Hufflepuff": self.hufflepuff,
            "Ravenclaw": self.ravenclaw
        }
        max_house = max(houses, key=houses.get)
        return max_house


def LucasJimenezN():
    maggle = User()
    for pregunta in preguntas_respuestas:
        print(pregunta["pregunta"])
        respuesta = "s"
        for key in pregunta["respuestas"]:
            print(f"{key} - {pregunta['respuestas'][key]}")
        while respuesta == "s":
            respuesta = input("Introduce la respuesta: ")
            if respuesta == "a":
                maggle.addGryffindor()
            else:
                if respuesta == "b":
                    maggle.addSlytherin()
                else:
                    if respuesta == "c":
                        maggle.addHufflepuff()
                    else:
                        if respuesta == "d":
                            maggle.addRavenclaw()
                        else:
                            print(f"Respuesta invalida")
                            respuesta = "s"
    house = maggle.getHouse()
    print(f"La casa que se le ha elegido es {house}")


LucasJimenezN()
