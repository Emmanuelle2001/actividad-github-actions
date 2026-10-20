def calcular_descuento(precio: float, porcentaje_descuento: float) -> float:
    if precio < 0 or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("Valores fuera de rango válido.")
    descuento = precio * (porcentaje_descuento / 100)
    return round(precio - descuento, 2)


def calcular_iva(precio: float, tasa_iva: float = 0.16) -> float:
    if precio < 0 or tasa_iva < 0:
        raise ValueError("El precio y la tasa de IVA deben ser positivos.")
    return round(precio * tasa_iva, 2)