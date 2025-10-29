from collections.abc import Iterable, Iterator
import sys

sys.path.append(".")
from src.q1 import Coordinates


"""
Please implement the class CoordinatesInOrder below.
We can iterate over a CoordinatesInOrder object.
The order of iteration will be from "smallest" to "largest".
You will need to write the documentation.
"""


class CoordinatesInOrder(Iterable[Coordinates]):
    pass
