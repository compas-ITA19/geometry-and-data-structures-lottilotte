# Assignment 2, Geometry - Task 1: 
# Given two vectors, use the cross product to create a set of three orthonormal vectors.

__author__ = "Lotte Aldinger"
__email__ = "aldinger@arch.ethz.ch"
__date__ = "30.10.2019"

from random import random

import compas_rhino
from compas.geometry import Vector

# ==============================================================================
# Functions
# ==============================================================================

def orthonormal_vectors(u, v):
    """Create a set of three orthonormal vectors from two given vectors.

    Parameters
    ----------
    u : vector
        Vector defining the x direction.
    v : vector
        Second vector for defining the xy plane.

    Returns
    -------
    Tuple
        Three orthonormal vectors.

    Examples
    --------
    >>> iorthonormal_vectors(Vector(0.0, 0.0, 5.0), Vector(0.5, 2.0, 0.0))
    (Vector(0.000, 0.000, 1.000), Vector(0.243, 0.970, -0.000), Vector(-0.970, 0.243, 0.000))
    """
    x = u.unitized()
    z = u.cross(v).unitized()
    y = z.cross(x)
    return (x, y, z)

def draw_input_vectors(u, v, layer):
    """Visualize the two input vectors in Rhino in grey colors.

    Parameters
    ----------
    u : vector
        Vector defining the x direction.
    v : vector
        Second vector for defining the xy plane.
    layer: string
        Name of Layer inside Rhino.
    """
    origin = (0, 0, 0)
    lines = [
        {'start': origin, 'end': tuple(u), 'color': (100, 100, 100), 'arrow': 'end'},
        {'start': origin, 'end': tuple(v), 'color': (150, 150, 150), 'arrow': 'end'},
    ]
    compas_rhino.draw_lines(lines, layer=layer, clear=False)

def draw_orthonormal_vectors(vectors, layer):
    """Visualize the three orthonormal output vectors in Rhino in rgb colors.

    Parameters
    ----------
    vectors : Tuple
        Three orthonormal vectors.
    layer: string
        Name of Layer inside Rhino.
    """
    origin = (0, 0, 0)
    lines = [
        {'start': origin, 'end': tuple(vectors[0]), 'color': (255, 0, 0), 'arrow': 'end'},
        {'start': origin, 'end': tuple(vectors[1]), 'color': (0, 255, 0), 'arrow': 'end'},
        {'start': origin, 'end': tuple(vectors[2]), 'color': (0, 0, 255), 'arrow': 'end'}
    ]
    compas_rhino.draw_lines(lines, layer=layer, clear=False)

# ==============================================================================
# Input and Output
# ==============================================================================

# generate random vector
u_input = Vector(random(), random(), random())
v_input = Vector(random(), random(), random())

xyz = orthonormal_vectors(u_input, v_input)
print(xyz)

# ==============================================================================
# Visualisation
# ==============================================================================

draw_input_vectors(u_input, v_input, "Iput Vectors")
draw_orthonormal_vectors(xyz, "Orthonormal Vectors")