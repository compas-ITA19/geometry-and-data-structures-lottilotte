# Assignment 2, Data Structures - Task 1:
# i. Define a function for traversing the mesh from boundary to boundary in a topologically "straight" line. (Using faces.obj)
# ii. Visualise the result

__author__ = "Lotte Aldinger"
__email__ = "aldinger@arch.ethz.ch"
__date__ = "30.10.2019"

import os
import compas

from random import randint

from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

# ==============================================================================
# Input file
# ==============================================================================

HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')

mesh = Mesh.from_obj(FILE)

# ==============================================================================
# Function
# ==============================================================================

def random_vertex_on_boundaries_exl_corners(mesh):
    """Find random vertex on boundary that is not in a corner.

    Parameters
    ----------
    mesh: mesh
        Mesh to operate on.

    Returns
    -------
    key of vertex
    """
    vertices_on_boundary_no_edges = []
    for key in mesh.vertices():
        if mesh.vertex_degree(key) == 3:
            vertices_on_boundary_no_edges.append(key)
    return vertices_on_boundary_no_edges[randint(0, len(vertices_on_boundary_no_edges)-1)]


def straight_traversing_mesh(vertex_present, mesh):
    """For traversing the mesh from boundary to boundary in a topologically "straight" line

    Parameters
    ----------
    vertex_present: key of vertex.
        Input vertex on boundary of mesh but not in corner.
    mesh: mesh
        Mesh to operate on.

    Returns
    -------
    Tuple: list of vertices, list of edges
        The vertices and edges on topologically straight line.
    """
    # create lists
    edges_line = []
    vertices_line = []
    # add first to list
    vertices_line.append(vertex_present)

    # for first vertex find neighbor vertex that is not on boundary, for ordered neighbors always the second.
    neighbors = mesh.vertex_neighbors(vertex_present, ordered=True)
    vertex_next = neighbors[1]
    # add to lists
    vertices_line.append(vertex_next)
    edges_line.append((vertex_present, vertex_next))
    # update the vertices
    vertex_previous = vertex_present
    vertex_present = vertex_next

    while len(mesh.vertex_neighbors(vertex_present, ordered=True)) == 4:
        # find opposite vertex to previous vertex
        neighbors = mesh.vertex_neighbors(vertex_present, ordered=True)
        for i, n in enumerate(neighbors):
            if n == vertex_previous:
                vertex_next = neighbors[i-2]      
        # add to lists     
        vertices_line.append(vertex_next) 
        edges_line.append((vertex_present, vertex_next))
        # update the vertices
        vertex_previous = vertex_present
        vertex_present = vertex_next
        
    print("vertices on topologically 'straight' line: ", vertices_line)
    return (vertices_line, edges_line)

# ==============================================================================
# Run
# ==============================================================================

vertex_input = random_vertex_on_boundaries_exl_corners(mesh)
vertices, edges = straight_traversing_mesh(vertex_input, mesh)

# ==============================================================================
# Visualisation
# ==============================================================================

plotter = MeshPlotter(mesh, figsize=(16, 10))

plotter.draw_vertices(
    text={key: key for key in mesh.vertices()},
    radius=0.2,
    facecolor={key: (255, 0, 0) for key in vertices}
)

plotter.draw_edges(
    keys= edges,
    color=(255, 0, 0))

plotter.draw_faces()
plotter.show()



