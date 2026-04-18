import pytest

def spiral_traversal(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

def test_spiral_traversal():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_traversal(matrix) == expected

def test_spiral_traversal_empty():
    matrix = []
    expected = []
    assert spiral_traversal(matrix) == expected

def test_spiral_traversal_single_element():
    matrix = [[1]]
    expected = [1]
    assert spiral_traversal(matrix) == expected

def test_spiral_traversal_single_row():
    matrix = [[1, 2, 3]]
    expected = [1, 2, 3]
    assert spiral_traversal(matrix) == expected

def test_spiral_traversal_single_column():
    matrix = [
        [1],
        [2],
        [3]
    ]
    expected = [1, 2, 3]
    assert spiral_traversal(matrix) == expected
