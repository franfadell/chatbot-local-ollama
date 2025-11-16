from Data.DataCollection import informacion  # Carga los datos del negocio
from core import * # Construye el prompt con la pregunta del usuario
datos=informacion

prompt = construir_prompt(datos)

def main():
    print("=== Chatbot del Negocio ===")
    print("Escribe tu pregunta sobre el negocio. Escribe 'salir' para terminar.\n")

    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() == "salir":
            print("Chatbot: ¡Hasta luego!")
            break

        respuesta = enviar_a_ollama(prompt, pregunta)
        print("Bot:", respuesta)

if __name__ == "__main__":
    main()
