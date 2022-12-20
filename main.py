import numpy as np

GAMMAS = (10, 2, 4 / 5)
INPUT_SIZE = 20

MAX_ITERATIONS = 10_000
MAX_ERROR = 1e-6


class NotConverging(Exception):
    pass


def D(matrix):
    return np.diag(np.diag(matrix))


def L(matrix):
    return np.tril(matrix, -1)


def U(matrix):
    return np.triu(matrix, 1)


def solve(A, b, Q, x0, max_iterations=MAX_ITERATIONS, max_error=MAX_ERROR):
    Q_inv = np.linalg.inv(Q)

    x = x0
    for i in range(max_iterations):
        x = Q_inv @ ((Q - A) @ x + b)

        err = np.linalg.norm(A @ x - b) / np.linalg.norm(b)

        if err < max_error:
            return x, i

        if err == np.Infinity:
            raise NotConverging

    raise NotConverging


def create_input(gamma, dim=INPUT_SIZE):
    A = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            if i == j:
                A[i][j] = gamma
            elif abs(i - j) == 1:
                A[i][j] = -1

    b = np.zeros(dim)
    for i in range(dim):
        if i == 0 or i == dim - 1:
            b[i] = gamma - 1
        else:
            b[i] = gamma - 2

    x0 = np.zeros(dim)

    return A, b, x0


def spectral_radius(A, Q, dim=INPUT_SIZE):
    Q_inv = np.linalg.inv(Q)
    E = np.identity(dim)

    W = E - (Q_inv @ A)

    return np.max(np.abs(np.linalg.eigvals(W)))


def jacobi(input):
    A, b, x0 = create_input(input)
    Q = D(A)

    ro = spectral_radius(A, Q)
    should_converge = ro < 1

    print(f"ro={ro}")

    try:
        x, iterations = solve(A, b, Q, x0)
        assert should_converge == True
        print(f"Jacobi converged in {iterations} iterations for gamma={input}")
    except NotConverging:
        assert should_converge == False
        print(f"Jacobi did not converge for gamma={input}")


def gauss_seidel(input):
    A, b, x0 = create_input(input)
    Q = D(A) + L(A)

    ro = spectral_radius(A, Q)
    should_converge = ro < 1

    print(f"ro={ro}")

    try:
        x, iterations = solve(A, b, Q, x0)
        assert should_converge == True
        print(f"Gauss-Seidel converged in {iterations} iterations for gamma={input}")
    except NotConverging:
        assert should_converge == False
        print(f"Gauss-Seidel did not converge for gamma={input}")


def main():
    for input in GAMMAS:
        jacobi(input)
        gauss_seidel(input)


if __name__ == "__main__":
    main()
