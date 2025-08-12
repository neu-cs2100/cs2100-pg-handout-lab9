import sys
sys.path.append("/path/to/this/directory") # Fill in this path
from q1 import Coordinates
from q2 import is_in_order


def add_in_order(element: Coordinates, coordinates: list[Coordinates]) -> None:
    # Add the element to the list of coordinates. Add the element at the index 
    # that keeps the list in order (for example, if we want to add 4 to the 
    # list [2, 9], then it should be added at index 1 so that the list becomes 
    # [2, 4, 9].). If the list is not currently in order, raise a ValueError.
    pass
