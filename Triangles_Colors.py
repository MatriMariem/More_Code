#!/usr/bin/python3


"""
Assuming that we have a list of triangles
each triangle has 3 points.
in each triangle, we need to assign The colors R, B and G to all points.
The function TriangleColors, takes a list of triangles and assigns colors to each point
The function must handle common points between different triangles
"""


def TriangleColors(t):

    colors = ['R', 'B', 'G']

    """ d is a dictionary that contains point=color pairs """
    d = {}


    for ti in range(len(t)):
        for pi in range(len(t[ti])):
            """ each point is stored as a string in the dictionary d"""
            sp = ', '.join(str(i) for i in t[ti][pi])
            if sp in d:
                pass
            else:
                """ color of the point must be different from other points colors in the same triangle """
                seleColors = colors[:]
                for p_prev_i in range(pi):
                    sprev = ', '.join(str(i) for i in t[ti][p_prev_i])
                    seleColors.remove(d.get(sprev))
                d[sp] = seleColors[0]

    colorPoints = {}
    for c in colors:
        if c not in colorPoints:
            colorPoints[c] = []

    """
    transferring the data from the d dicioanry to colorPoints dictionary,
    from point=color (in d), to color=[list of points] (in colorPoints)
    """
    for sp, c in d.items():
        p = sp.split(', ')
        colorPoints[c].append(p)

    return colorPoints






triangles = [
[ [0,0], [3,0], [0,5] ],
[ [3,0], [0,0], [0.5, -3] ],
[ [4,3], [3,0], [6,0] ],
[ [6,0], [8,3], [9,0] ]
]
print(TriangleColors(triangles))

print()

""" There is no solution for this case but the program doesn't throw an error """
triangles = [
[ [0,0], [2.5,3], [5,0] ],
[ [0,0], [2.5,-4], [5,0] ],
[ [0,0], [2.5,3], [2.5,-4] ],
[ [2.5,3], [2.5,-4], [5,0] ]
]
print(TriangleColors(triangles))
