#!/usr/bin/python3
"""Pascal Triangle module"""


def pascal_triangle(n):
    """computes pascal triangle

    Args:
      n: int
    """
    if n <= 0:
        return []
    triangle = [[1]]
    idx = 0

    for i in range(1, n):
        prev = triangle[idx]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        idx += 1
        triangle.append(row)
    return triangle
