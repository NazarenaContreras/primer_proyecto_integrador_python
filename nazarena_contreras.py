import random #para elecciones aleatorias

#para validar la letra ingresada
def validar_letra(func):
    def wrapper(juego, *args, **kwargs):
        letra = kwargs.get('letra')
        if not letra.isalpha() or len(letra) != 1: #isalpha() para asegurar que se ingresa una letra y no un numero. Y len(letra) != 1: para que la longitud de entrada sea estrictamente 1.
            print("Por favor, ingresa una sola letra.")
        elif letra in juego.letras_adivinadas:   #usa la lista letras_adivinadas para verificar si la letra ingresada esta en esa lista.
            print(f"Ya has adivinado la letra '{letra}'. Intenta otra.")
        else:
            return func(juego, *args, **kwargs)
    return wrapper

#para verificar si el juego finalizo
def verificar_final(func):
    def wrapper(juego, *args, **kwargs):
        if juego.verificar_victoria():  #verifica si el jugador adivino todas las letras.
            print("¡Felicidades! ¡Adivinaste la palabra!")
            return
        elif juego.intentos <= 0:
            print(f"Lo siento \U0001F641 perdiste. La palabra secreta era '{juego.palabra_secreta}'. \nFin del juego.")
            return
        return func(juego, *args, **kwargs) 
    return wrapper

#generador para proporcionar palabras secretas
def generador_palabras(palabras):
    for palabra in palabras:
        yield palabra

#clase JuegoAdivinaLaPalabra es una plantilla para crear objetos, agrupa datos (atributos) y funciones (métodos)
class JuegoAdivinaLaPalabra:
    
    #metodo constructor __init__  metodo especial que se llama automáticamente cuando se crea un objeto.
    def __init__(self, *args, **kwargs):   #*args y **kwargs permiten al constructor aceptar un número variable de argumentos posicionales y de palabras clave
        self.palabra_secreta = kwargs.get('palabra_secreta') #atributo que almacena la palabra secreta
        self.intentos = kwargs.get('intentos', 6) #atributo que almacena el número de intentos que tiene el jugador, o sea 6
        self.letras_adivinadas = []    #atrubuto como lista vacía donde se guardan las letras adivinadas
        self.estado_actual = ["_" for _ in self.palabra_secreta] #atrubuto como lista de guines, donde cada guion representa una letra de la palabra secreta
        self.letras_incorrectas = [] #atributo como lista vacia donde se guardan las letras ingresadas incorrectas

    
    #el decorador se aplica a la función adivinar_letra para verificar si el juego termino antes de proceder con el resto de la lógica.
    @validar_letra  
    @verificar_final
    def adivinar_letra(self, *args, **kwargs):
        letra = kwargs.get('letra')   #añade la letra ingresada a la lista letras_adivinadas
        self.letras_adivinadas.append(letra) 
        if letra in self.palabra_secreta:    #para verificar si la letra ingresada se encuentra en la palabra secreta.
            for i, char in enumerate(self.palabra_secreta):   #para iterar sobre los caracteres de la palabra secreta y sus índices.
                if char == letra:  #comprueba si el carácter actual (chr) coincide con la letra ingresada.
                    self.estado_actual[i] = letra  #reemplaza el guion bajo con la letra adivinada en la posición correcta (i).
            print("¡Buena elección!")
        else:
            self.intentos -= 1   #para restar intentos cuando ingresa una letra incorrecta.
            self.letras_incorrectas.append(letra)  #para agregar la letra incorrecta a la lista. 
            print("Letra incorrecta. Pierdes un intento.")
        self.mostrar_estado()

    
    #para mostrar el estado de letras adivinadas, intentos y letras incorrectas.
    def mostrar_estado(self):
        print("Palabra: " + " ".join(self.estado_actual))
        print(f"Intentos restantes: {self.intentos}")
        print(f"Letras incorrectas: {', '.join(self.letras_incorrectas)}")

    
    #para verificar si el jugador adivino todas las letras. Verifica si no hay guiones bajos en self.estado_actual.
    def verificar_victoria(self):
        return "_" not in self.estado_actual


    #metodo jugar que controla el flujo del juego
    def jugar(self, *args, **kwargs):
        print("¡Bienvenida al juego Adivina la Palabra! \U0001F604 Para iniciar ingresa una letra y si deseas salir escribe 'salir' en cualquier momento.")
        self.mostrar_estado()
        while self.intentos > 0 and not self.verificar_victoria():  #bucle while para continuar ejecutando mientras queden intentos.
            letra = input("Adivina una letra: ").lower()
            if letra == "salir":
                print("Decidiste no jugar más \U0001F615 \nFin del juego.")
                return
            self.adivinar_letra(letra=letra)
        if self.verificar_victoria():
            print("¡Felicidades! \U0001F973 ¡Adivinaste la palabra! \nFin del juego.")
        else:
            print(f"Lo siento \U0001F641 perdiste. La palabra secreta era '{self.palabra_secreta}'. \nFin del juego.")

#lista de palabras secretas
palabras_secretas = ["camara", "auriculares", "celular", "monitor", "teclado"]


# Seleccionar la palabra secreta aleatoriamente usando random.choice
palabra_secreta = random.choice(palabras_secretas)


#iniciar el juego
juego = JuegoAdivinaLaPalabra(palabra_secreta=palabra_secreta)
juego.jugar()