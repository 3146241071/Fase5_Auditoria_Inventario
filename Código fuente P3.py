# ==========================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Curso: Fundamentos de Programación
# Código del curso: 213022
# Fase 5 - Evaluación Final POA
#
# Autor: Keiner Paternina Acosta
# Grupo: 213022_4
# Programa: Ingeniería Electrónica
#
# Problema 3: Auditoría de Inventario
# ==========================================================


# ----------------------------------------------------------
# Función para calcular la cantidad que debe solicitarse
# ----------------------------------------------------------
def calcular_pedido(stock_actual, stock_minimo):
    """
    Calcula la cantidad de unidades que deben solicitarse.
    Si el stock actual es menor al stock mínimo,
    retorna la diferencia.
    De lo contrario retorna 0.
    """

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# ----------------------------------------------------------
# Matriz del inventario
# Formato:
# [Código, Nombre, Stock Actual, Stock Mínimo]
# ----------------------------------------------------------

inventario = [
    ["A001", "Tornillos", 15, 20],
    ["A002", "Tuercas", 40, 25],
    ["A003", "Arandelas", 10, 15],
    ["A004", "Cables", 50, 30],
    ["A005", "Interruptores", 5, 10]
]


# ----------------------------------------------------------
# Encabezado del reporte
# ----------------------------------------------------------

print("=" * 55)
print("          REPORTE DE AUDITORÍA DE INVENTARIO")
print("=" * 55)


# ----------------------------------------------------------
# Recorrer la matriz
# ----------------------------------------------------------

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print(f"\nCódigo: {codigo}")
    print(f"Artículo: {nombre}")
    print(f"Stock actual: {stock_actual}")
    print(f"Stock mínimo: {stock_minimo}")
    print(f"Cantidad a solicitar: {cantidad_pedir}")


print("\n" + "=" * 55)
print("      FIN DEL REPORTE DE INVENTARIO")
print("=" * 55)