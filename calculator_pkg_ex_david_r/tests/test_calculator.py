from ..calculator import Calculator
# from calculator_pkg_ex_david_r import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        assert Calculator().add(1, 2) == 3, "Add failed"

    def test_substract(self):
        assert Calculator().substract(1, 2) == -1, "Substract failed"

    def test_multiply(self):
        assert Calculator().multiply(3, 2) == 6, "Multiply failed"

    def test_divide(self):
        assert Calculator().divide(8, 2)== 4, "Divide failed"

    def test_divide_zero(self):
        with pytest.raises(ZeroDivisionError):
            Calculator().divide(8, 0)