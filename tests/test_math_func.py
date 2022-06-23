"""
pytest tests/test_math_func.py
# ejecuta solo los test de determinado archivo
pytest tests/. -v --disable-warnings
# ejecuta todos los test
pytest tests/test_math_func.py::test_product -v --disable-warnings
# ejecuta los test de uan fucnion especifica
pytest tests/test_math_func.py -v -k "add or string"
# ejecuta solo las funciones de los test cuyos nombres
# contengan los keywrords pasados
pytest tests/test_math_func.py -v -m number --disable-warnings
# ejecuta solo los test que tengan las marcas de number
pytest tests/test_math_func.py -v --disable-warnings -s
# imprime los print
pytest tests/test_math_func.py -q --disable-warnings
"""

from src import math_func
import pytest


@pytest.mark.number
def test_add():
    print("mi primer test")
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9


@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


@pytest.mark.strings
def test_add_strings():
    result = math_func.add("Hello", " World")
    assert result == "Hello World"
    assert type(result) is str
    assert "Hello" in result
