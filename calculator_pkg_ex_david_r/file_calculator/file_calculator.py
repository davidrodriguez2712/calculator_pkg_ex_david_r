from ..calculator import Calculator # relative import
# from calculator_pkg_ex_david_r.calculator import Calculator # abolute import 
from pathlib import Path

class FileCalculator(Calculator):
    def __init__(
        self,
        path= Path(__file__).parent / "nums.csv"
    ):
        self.path = path

    def add_file(self):
        total = None
        with open(self.path) as f:
            for line in f:
                if total is None:
                    total = line
                    continue
                else:
                    total += line
        return total

