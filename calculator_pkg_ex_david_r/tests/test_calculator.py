# from calculator_pkg_ex_david_r import Calculator
import pytest

from ..calculator import Calculator


class TestCalculator:
    def test_add(self) -> None:
        assert Calculator().add(1, 2) == 3, "Add failed"

    def test_substract(self) -> None:
        assert Calculator().substract(1, 2) == -1, "Substract failed"

    def test_multiply(self) -> None:
        assert Calculator().multiply(3, 2) == 6, "Multiply failed"

    def test_divide(self) -> None:
        assert Calculator().divide(8, 2) == 4, "Divide failed"

    def test_divide_zero(self) -> None:
        with pytest.raises(ZeroDivisionError):
            Calculator().divide(8, 0)
