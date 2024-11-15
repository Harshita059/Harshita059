def multiply_matrices(A, B):
    # Result matrix
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

# Example matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Multiply matrices
result = multiply_matrices(A, B)

# Display result
print(result)
