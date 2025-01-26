"""
Primer proyecto integrador python - nazarenacontreras.py
------------------- EL JUEGO SE LLAMA: ADIVINA LA PALABRA -------------------------              
"""
import random #para elecciones aleatorias

#se define una funcion para validar que la letra no haya sido adivinada antes y que sea solo una letra.
def validar_letra(func):
    def wrapper(juego, letra):
        if not letra.isalpha() or len(letra) != 1: #isalpha() para asegurar que se ingresa una letra y no un numero. Y len(letra) != 1: para que la longitud de entrada sea estrictamente 1.
            print("Por favor, ingresa una sola letra.")
        elif letra in juego.letras_adivinadas:  #usa la lista letras_adivinadas para verificar si la letra ingresada esta en esa lista.
            print(f"Ya adivinaste la letra '{letra}'. Intenta otra.") 
        else:
            return func(juego, letra)
    return wrapper

#clase JuegoAdivinaLaPalabra es una plantilla para crear objetos, agrupa datos (atributos) y funciones (métodos)
class JuegoAdivinaLaPalabra:
    #metodo constructor __init__ 
    def __init__(self, palabra_secreta, intentos=6):          
        self.palabra_secreta = palabra_secreta                
        self.intentos = intentos                              
        self.letras_adivinadas = []                           
        self.estado_actual = ["_" for _ in palabra_secreta]   
        self.letras_incorrectas = []                          

    @validar_letra        #el decorador se aplica a la función adivinar_letra para validar la letra antes de proceder con el resto de la lógica. 
    def adivinar_letra(self, letra):
        self.letras_adivinadas.append(letra)  #añade la letra ingresada a la lista letras_adivinadas
        if letra in self.palabra_secreta:     #para verificar si la letra ingresada se encuentra en la palabra secreta.
            for i, chr in enumerate(self.palabra_secreta):  #para iterar sobre los caracteres de la palabra secreta y sus índices.
                if chr == letra:   #comprueba si el carácter actual (chr) coincide con la letra ingresada.
                    self.estado_actual[i] = letra   #reemplaza el guion bajo con la letra adivinada en la posición correcta (i).
            print("¡Bien hecho!")
        else:
            self.intentos -= 1 #para restar intentos cuando ingresa una letra incorrecta.
            self.letras_incorrectas.append(letra) #para agregar la letra incorrecta a la lista. 
            print("Letra incorrecta. Pierdes un intento.")
        self.mostrar_estado() 
        
#para iniciar el juego
juego = JuegoAdivinaLaPalabra(palabra_secreta)
juego.jugar()

#lista de palabras secretas
palabras_secretas = ["camara", "auriculares", "celular", "monitor", "teclado"]
palabra_secreta = random.choice(palabras_secretas)

    #para mostrar el estado de letras adivinadas, intentos y letras incorrectas.
    def mostrar_estado(self):
        print("Palabra: " + " ".join(self.estado_actual)), print(f"Intentos restantes: {self.intentos}"), print(f"Letras incorrectas: {', '.join(self.letras_incorrectas)}")
        
    #para verificar si el jugador adivino todas las letras. Verifica si no hay guiones bajos en self.estado_actual.
    def verificar_victoria(self):
        return "_" not in self.estado_actual
    
    #metodo jugar que controla el flujo del juego
    def jugar(self):
        print("¡Bienvenida al juego Adivina la Palabra!  Para iniciar ingresa una letra y si deseas salir escribe 'salir' en cualquier momento.")
        self.mostrar_estado()
        while self.intentos > 0 and not self.verificar_victoria(): #bucle while para continuar ejecutando mientras queden intentos.
            letra = input("Adivina una letra: ").lower()
            if letra == "salir":
                print("Decidiste no jugar mas. Fin del juego.")
                return
            self.adivinar_letra(letra)
        if self.verificar_victoria():
            print("¡Felicidades! ¡Adivinaste la palabra!")
        else:
            print(f"Perdiste. La palabra secreta era '{self.palabra_secreta}'. Fin del juego.")
        print("gracias por jugar")