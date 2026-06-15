import numpy as np

def jacobi_method(A, b, x0=None, tol=1e-10, max_iter=100):
    """
    Solve Ax = b using the Jacobi iterative method.

    Parameters:
        A : 2D list or numpy array (square matrix)
        b : 1D list or numpy array
        x0 : initial guess (optional)
        tol : tolerance for convergence
        max_iter : maximum number of iterations

    Returns:
        x : solution vector
        k : number of iterations used
    """

    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    x_new = np.zeros(n)

    for k in range(max_iter):

        for i in range(n):
            sum1 = 0.0

            for j in range(n):
                if i != j:
                    sum1 += A[i][j] * x[j]

            x_new[i] = (b[i] - sum1) / A[i][i]

        # check convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:
            return x_new, k + 1

        x[:] = x_new

    return x, max_iter


# Example usage
if __name__ == "__main__":
    A = [[10, 3, 1],
         [3, 10, 2],
         [1, 2, 10]]

    b = [19, 29, 35]

    sol, iters = jacobi_method(A, b)

    print("Solution:", sol)
    print("Iterations:", iters)
