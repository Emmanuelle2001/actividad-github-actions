import pytest
from calculos import calcular_descuento, calcular_iva

def test_calcular_descuento_correcto():
    # Descuento del 10% sobre 100 debe dar 90
    assert calcular_descuento(100.0, 10.0) == 90.0
    # Descuento del 50% sobre 200 debe dar 100
    assert calcular_descuento(200.0, 50.0) == 100.0

def test_calcular_iva_correcto():
    # IVA del 16% sobre 100 es 16.0
    assert calcular_iva(100.0, 0.16) == 16.0
    # IVA del 16% sobre 500 es 80.0
    assert calcular_iva(500.0, 0.16) == 80.0

def test_excepciones_valores_negativos():
    # Debe lanzar error con valores no permitidos
    with pytest.raises(ValueError):
        calcular_descuento(-50, 10)
    with pytest.raises(ValueError):
        calcular_iva(-100)