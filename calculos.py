def calcular_descuento(precio: float, porcentaje_descuento: float) -> float:
    if precio < 0 or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Valores fuera de rango válido.")
    descuento = precio * (porcentaje_descuento / 100)
    return round(precio - descuento, 2)  # CORREGIDO