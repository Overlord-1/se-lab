# matrix_operations.py
import numpy as np

def matrix_demo():
    # Create two sample matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    # Perform operations
    addition = matrix1 + matrix2
    multiplication = np.dot(matrix1, matrix2)
    
    print("Matrix 1:\n", matrix1)
    print("Matrix 2:\n", matrix2)
    print("Addition Result:\n", addition)
    print("Multiplication Result:\n", multiplication)

if __name__ == "__main__":
    matrix_demo()

