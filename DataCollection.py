# Importamos la librería "json" que permite trabajar con archivos y datos en formato JSON 
# (leer, escribir, convertir a diccionarios, etc).
import json

# Cargamos el archivo llamado "nomb_archivo" con "datos.json"
nomb_archivo = 'datos.json'

with open(nomb_archivo, 'r', encoding='utf-8') as archivo:
    datos = json.load(archivo)

# Organizmos la informacion del archivo

informacion = {
    'nombre_empresa': datos.get('nombre'),
    'contacto': {
        'telefono': datos.get('telefono'),
        'correo': datos.get('correo')
    },
    'horarios': datos.get('horarios_atencion'),
    'productos': [
        {
            'nombre': producto.get('nombre'),
            'precio': producto.get('precio'),
            'link': producto.get('link')
        }
        for producto in datos.get('productos', [])
    ],
    'empleados': datos.get('empleados', [])
}

# Creamos un modulo para mostrar la informacion principal del local
def mostrar_informacion_local():
    print("---------------------------------------")
    print("Informacion del local")
    print("Nombre:", informacion['nombre_empresa'])
    print("Telefono:", informacion['contacto']['telefono'])
    print("Correo:", informacion['contacto']['correo'])
    print("---------------------------------------")

# Creamos un modulo para mostrar los horarios del local
def mostrar_horarios():
    print("\nHorarios del local")
    for dia in informacion['horarios']:
        horario=informacion['horarios'][dia]
        print(f"{dia}: {horario}")

# Creamos un modulo para mostrar los productos del local
def mostrar_productos():
    print("\nLista de productos")
    contador= 1
    print(f"cantidad de productos encontrados: {len(informacion['productos'])}")
    for producto in informacion['productos']:
        print(f"\nProducto {contador}:")
        print("  Nombre:", producto['nombre'])
        print("  Precio:", producto['precio'])
        print("  Link:", producto['link'])
        contador +=1
   

# Creamos un modulo para mostrar la informacion de los empleados del local
def mostrar_empleados():
    empleados = informacion['empleados']
    if not empleados:
        print("\nNo se encuentra informacion de los empleados")
        return
    print("\nEmpleados")
    for i, empleado in enumerate(empleados, start=1):
        print(f"\nEmpleado {i}:")
        print(" Nombre:", empleado.get('nombre'))
        print(" telefono:", empleado.get('telefono'))
        print(" Horario de atencion:", empleado.get('horario'))
        print(" Dia de trabajo:",empleado.get('dias_trabajo'))

# Creacion del menu
# Caso que quiera probar el programa, saque los "#"
# while True:
#    print("\nMenu del local")
#    print("1) Ver la informacion del local")
#    print("2) Ver los productos del local")
#    print("3) Ver los datos de los empleados del local")
#    print("4) Ver los horarios de atencion del local")
#    print("5) Salir del menu")
#
#    opcion = input("Seleccione una opcion: \n")
#
#    if opcion == "1":
#        mostrar_informacion_local()
#    elif opcion == "2":
#        mostrar_productos()
#    elif opcion == "3":
#        mostrar_empleados()
#    elif opcion == "4":
#        mostrar_horarios()
#    elif opcion == "5":
#        print("Programa finalizado")
#        break
#    else:
#        print("Opcion no valida, ingrese de nuevo")