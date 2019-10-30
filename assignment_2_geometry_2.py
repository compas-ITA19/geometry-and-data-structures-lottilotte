# Assignment 2, Geometry -  Task 2:
# Use the cross product to compute the area of a convex, 2D polygon.

__author__ = "Lotte Aldinger"
__email__ = "aldinger@arch.ethz.ch"
__date__ = "30.10.2019"

import compas_rhino
from compas.geometry import Polygon
from compas.geometry import Vector
from compas.utilities import pairwise

# ==============================================================================
# Functions
# ==============================================================================

def convex_polygon_area(polygon):
    """Compute the area of a convex polygon.

    Parameters
    ----------
    polygon: compas.geometry.Polygon
        An ordered list of points of a convex polygon.

    Returns
    -------
    Float
        Area of the polygon.
    """
    # find vectors from centroid to all corner points.
    centroid = polygon.centroid
    vectors = []
    for vertex in polygon: 
        vectors.append(Vector.from_start_end(centroid, vertex))
    areas = []
    # the magnitude of the cross product equals the area of a parallelogram, thus half of it equals the triangle.
    for u, v in pairwise(vectors + vectors[:1]):
        uxv = u.cross(v)
        a = uxv.length / 2
        areas.append(a)
    return sum(areas)

def draw_polygon(polygon, layer):
    """Visualize the polygon in Rhino in black.

    Parameters
    ----------
    polygon: compas.geometry.Polygon
        An ordered list of points of a convex polygon
    layer: string
        Name of Layer inside Rhino.
    """
    lines = []
    for a, b in pairwise(list(polygon) + list(polygon[:1])):
        lines.append({'start': tuple(a), 'end': tuple(b), 'color': (0, 0, 0)})
    compas_rhino.draw_lines(lines, layer=layer, clear=False)

# ==============================================================================
# Input and Output
# ==============================================================================

polygon = Polygon([[0,0,0], [1,-0.5,0], [1,1,0], [0.5,1.5,0], [0,1,0]]) 

myArea = convex_polygon_area(polygon)

print(myArea)

# double check within compas function
print(polygon.area == myArea)

# ==============================================================================
# Visualisation
# ==============================================================================

draw_polygon(polygon, "Polygon")