#!/usr/bin/python3
"""Rotate 2D matrix module"""


def rotate_2d_matrix(matrix):
    """rotates 2D matrix 90 degrees clockwise"""
    rotated = [
        [matrix[j][i] for j in range(len(matrix[i]))]
        for i in range(len(matrix))
    ]
    for i in range(len(matrix)):
        pos = -1
        for j in range(len(matrix[i])):
            matrix[i][j] = rotated[i][pos]
            pos -= 1
