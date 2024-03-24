# Tarea semana 15
# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Andrés", "apellido": "Ponce", "edad": 38, "ciudad": "Guayaquil", "profesion": "Especialista Electrónico"
}

# Accedemos y modificamos el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Quito"

# Actualizamos el valor de la clave "profesion"
informacion_personal["profesion"] = "Ingeniero en Tics"

# Verificamos si la clave "telefono" existe, caso contrario la agregamos
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "099-647-9614"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)

# Fin del programa