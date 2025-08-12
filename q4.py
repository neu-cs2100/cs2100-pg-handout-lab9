import sys
sys.path.append("/path/to/this/directory") # Fill in this path
from q1 import Coordinates
from collections.abc import Iterable, Iterator
from typing import TypeVar, Generic

T = TypeVar('T')

class CoordinatesInOrder(Iterable[T]):
    # Works like a list of Coordinates, but
    # when iterated over, goes in order from 
    # "smallest" to "largest"
    def __init__(self, coordinates: list[Coordinates]):
        pass
