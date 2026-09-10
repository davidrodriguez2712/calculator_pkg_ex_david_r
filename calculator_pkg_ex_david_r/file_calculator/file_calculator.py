from ..calculator import Calculator # relative import
# from calculator_pkg_ex_david_r.calculator import Calculator # abolute import 
from pathlib import Path
from typing import Any

class FileCalculator(Calculator):
    def __init__(
        self,
        path: Path = Path(__file__).parent / "nums.csv"
    ) -> None:
        self.path = path

    def add_file(self) -> float | None:
        #mylist: list[int] = [1, 2, 3]
        total: float | None = None 
        with open(self.path) as f:
            for line in f:
                if total is None:
                    total = float(line)
                    continue
                else:
                    total += float(line)
        return total

