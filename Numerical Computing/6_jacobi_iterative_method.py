"""
    Solve Ax = b using the Jacobi iterative method.

        A : 2D list or numpy array (square matrix)
        b : 1D list or numpy array
        x0 : initial guess (optional)
        tol : tolerance for convergence
        max_iter : maximum number of iterations

            AX = B
         [10, 3, 1] [x1] = [19]
         [3, 10, 2] [x2] = [29]
         [1, 2, 10] [x3] = [35]

    """

import numpy as np

def jacobi_method(A, b, x0=None, tol=1e-10, max_iter=100):
    
    # Ax = b
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    n = len(b)

    # For first itration let x=[0,0,0]
    if x0 is None:
        x = np.zeros(n)
    else:
        x = np.array(x0, dtype=float)

    # create zeroes filled result matrix/array 
    x_new = np.zeros(n)

    for k in range(max_iter):                               # loop for number of itrations

        for i in range(n):                                  # loop to itrate first row of first matrix A
            sum1 = 0.0

            for j in range(n):                              # for each index of first matrix's row, Loop will itrate 2nd matrix's column
                if i != j:                                  # if its not diagonal like 1x1 , 2x2 , 3x3
                    sum1 += A[i][j] * x[j]                  # multiply index of first row to 2nd matrix indexe  
                                                            # Due to loop first matrix each index in row is multiples all indexes of 2nd matrix  
            x_new[i] = (b[i] - sum1) / A[i][i]              # function to find our answer rows index like x0 , x1 , x2

        # check convergence
        if np.linalg.norm(x_new - x, ord=np.inf) < tol:     # function to check if answers stoped changing or not if yes ends loop else next itrations
            return x_new, k + 1

        x[:] = x_new                                        # for next itration , current output array is the initial guess

    return x, max_iter                                      # when found the result return result matrix/array with maximum itrations performed


# Example usage
if __name__ == "__main__":
    A = [[10, 3, 1],
         [3, 10, 2],
         [1, 2, 10]]

    b = [19, 29, 35]


    sol, iters = jacobi_method(A, b)

    print("Solution:", sol)
    print("Iterations:", iters)