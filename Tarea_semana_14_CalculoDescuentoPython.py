# Tarea semana 14: Cálculo de Descuento en Compras
# Función para calcular el descuento aplicando un porcentaje al monto total de la compra.

def calcular_descuento(valor_total, porcentaje_descuento=13):

    # Calculo de descuento
    descuento = valor_total * (porcentaje_descuento / 100)
    return descuento

# Valor total de la compra
valor_compra = 7692
# Primer llamado a la función calcular_descuento
valor_final = valor_compra - calcular_descuento(valor_compra)
# Imprime el valor total de la compra sin descuento
print(f"Valor total de la compra: ${valor_compra}")
# Segundo llamado a la función calcular_descuento
# Imprime el valor del descuento
print("Descuento:", calcular_descuento(valor_compra))
# Imprime el valor a pagar incluido el descuento
print("Valor total a pagar:", valor_final)

# Fin del programa