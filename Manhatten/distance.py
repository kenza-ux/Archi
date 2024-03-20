class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

def distance_manhattan(point1, point2):
    """
    Calcule la distance de Manhattan entre deux points.

    Args:
        point1 (Point): Le premier point.
        point2 (Point): Le deuxième point.

    Returns:
        int: La distance de Manhattan entre les deux points.
    """
    return abs(point1._x - point2._x) + abs(point1._y - point2._y)

# Exemple d'utilisation
point1 = Point(3, 5)
point2 = Point(7, 9)
distance = distance_manhattan(point1, point2)
print("Distance de Manhattan entre", point1, "et", point2, ":", distance)
