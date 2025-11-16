from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

#### PARTE DEL GRUPO 4 #####
def construir_prompt(datos: dict):
    nombre = datos.get("nombre", "el negocio")
    info = "\n".join([f"{k.capitalize()}: {v}" for k, v in datos.items() if k != "nombre"])
    info = info.replace("{", "{{").replace("}", "}}")

    sys_template = (
        f"Eres un asistente que responde preguntas sobre un negocio llamado {nombre}. y solo quiero que respondas informacion del negocio, no informacion adicional\n"
        f"Información del negocio es: \n{info}\n"
        "Recuerda que CPU es Procesador, GPU es Tarjeta de Video o Grafica, MotherBoard es Placa Madre. Se cuidadoso a la hora de otorgar los componentes, tienes que ser preciso al responder de acorde al componente"
        "Por ultimo trata de mencionar las marcas del componente"
        "Si no te preguntan nada relacionado al negocio, trata de ser amable para atraer al cliente."
        )
    
    user_template = (
        "Pregunta: {pregunta}\n"
        "Respuesta: "
    )
    
    prompt = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(sys_template),
        HumanMessagePromptTemplate.from_template(user_template)
    ])
    return prompt

#### PARTE DEL GRUPO 3 #####
def enviar_a_ollama(prompt, pregunta: str): #Nombre del modelo Ej. 'llama3.1'
    modelo = OllamaLLM(model = "phi4-mini")
    chain = prompt | modelo
    respuesta = chain.invoke({
        "pregunta":pregunta
        })
    return respuesta