import numpy as np
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'build'))

from cholesky_module import cholesky_decomposition
print("Module imported successfully!")

A = [[4, 12, -16],
     [12, 37, -43], 
     [-16, -43, 98]]

print("Testing with matrix:")
print(np.array(A))

L_custom = cholesky_decomposition(A)
print("\nOur implementation result:")
print(np.array(L_custom))

L_numpy = np.linalg.cholesky(A)
print("\nNumPy result:")
print(L_numpy)

error = np.max(np.abs(np.array(L_custom) - L_numpy))
print(f"\nMax difference: {error}")

if error < 1e-10:
    print("TEST PASSED!")
else:
    print("TEST FAILED!")
        