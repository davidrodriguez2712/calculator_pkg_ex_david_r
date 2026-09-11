# from calculator_pkg_ex_david_r.calculator import Calculator # abolute import
import time
from pathlib import Path

from tqdm import tqdm

from ..calculator import Calculator  # relative import


class FileCalculator(Calculator):
    def __init__(self, path: Path = Path(__file__).parent / "nums.csv") -> None:
        self.path = path
        self.expected_lines: int = 3

    def add_file(self) -> float | None:
        # mylist: list[int] = [1, 2, 3]
        total: float = 0
        with open(self.path) as f:
            for line in tqdm(
                f,
                total= self.expected_lines,
                desc= 'Summing lines in file'

            ):
                time.sleep(2)
                total += float(line)
        return total
