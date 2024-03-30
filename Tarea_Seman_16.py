# Tarea semana 16 Trabajo con Archivos de Texto en Python

# Crear y escribir en un archivo de texto llamado my_notes.txt
def escribir_notas():
    try:
        # Abrimos el archivo creado en modo escritura
        with open('my_notes.txt', 'w') as archivo:
            # Escribimos un título y tres líneas con notas personales
            archivo.write("Notas personales:\n")
            archivo.write("1. Estudio en la Universidad Estatal Amazónica.\n")
            archivo.write("2. Quiero ser un ingeniero de la republica del Ecuador.\n")
            archivo.write("3. Sigo Ingeniería en Tecnologías de la Información.\n")
            # El archivo se cierra automáticamente al salir del bloque 'with'

    # Buscamos errores en la escritura del texto
    except IOError:
        print('Error al escribir en el archivo.')


# Leemos las notas desde el archivo de texto
def leer_notas():
    try:
        # Abrimos el archivo en modo lectura
        with open('my_notes.txt', 'r') as archivo:
            # Leemos el contenido del archivo línea por línea
            linea = archivo.readline()
            while linea:
                # Imprimimos cada línea leída
                print(linea.strip())
                linea = archivo.readline()

    # Escribimos un codigo de error en caso de falla del programa
    except FileNotFoundError:
        print("El archivo my_notes.txt no existe.")


# Llamamos a las funciones para leer y escribir las líneas del archivo
escribir_notas()
leer_notas()

# Fin del programa
