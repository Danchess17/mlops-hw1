import numpy as np
import pytest
from cholesky_module import cholesky_decomposition

A1x1 = [[4]]

A2x2 = [[4, 2], 
        [2, 5]]

A3x3 = [[4, 12, -16],
        [12, 37, -43], 
        [-16, -43, 98]]

A4x4 = [[25, 15, -5, 0],
        [15, 18, 0, 0],
        [-5, 0, 11, 0],
        [0, 0, 0, 9]]

A5x5 = [[25, 15, -5, 0, 0],
        [15, 18, 0, 0, 0],
        [-5, 0, 11, 0, 0],
        [0, 0, 0, 9, 0],
        [0, 0, 0, 0, 16]]

A_identity_3x3 = [[1, 0, 0],
                  [0, 1, 0],
                  [0, 0, 1]]

A_diagonal_3x3 = [[9, 0, 0],
                  [0, 16, 0],
                  [0, 0, 25]]

A_dense_3x3 = [[6, 3, 1],
               [3, 5, 2],
               [1, 2, 4]]

A_dense_4x4 = [[10, 4, 2, 1],
               [4, 8, 3, 2],
               [2, 3, 7, 1],
               [1, 2, 1, 6]]

A_dense_5x5 = [[16, 8, 4, 2, 1],
               [8, 15, 6, 3, 2],
               [4, 6, 14, 5, 3],
               [2, 3, 5, 13, 4],
               [1, 2, 3, 4, 12]]

test_cases = [
    (A1x1, "Matrix 1x1"),
    (A2x2, "Matrix 2x2"),
    (A3x3, "Matrix 3x3"),
    (A4x4, "Matrix 4x4"),
    (A5x5, "Matrix 5x5"),
    (A_identity_3x3, "Identity matrix 3x3"),
    (A_diagonal_3x3, "Diagonal matrix 3x3"),
    (A_dense_3x3, "Dense matrix 3x3"),
    (A_dense_4x4, "Dense matrix 4x4"),
    (A_dense_5x5, "Dense matrix 5x5"),
]

@pytest.mark.parametrize("A,test_name", [
    pytest.param(A, name, id=name.replace(" ", "_")) for A, name in test_cases
])
def test_cholesky(A, test_name):
    L_custom = cholesky_decomposition(A)
    L_numpy = np.linalg.cholesky(A)
    error = np.max(np.abs(np.array(L_custom) - L_numpy))
    assert error < 1e-10, f"Test '{test_name}' failed: max difference = {error}"
