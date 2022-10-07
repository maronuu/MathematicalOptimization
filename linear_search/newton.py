import numpy as np


def linear_search_newton(
    g,
    dg,
    d2g,
    h,
    alpha_0: float,
    xi: float,
) -> float:
    alpha_k = alpha_0
    k = 0
    print(f"{k}: alpha={alpha_k}")
    while True:
        if _check_almijo(alpha_k, xi, g, h):
            print(f"Almijo constraint is satisfied at k = {k}")
            break
        alpha_k = alpha_k - dg(alpha_k) / (d2g(alpha_k) + 1e-5)
        print(f"{k}: alpha={alpha_k}")
        k += 1
    
    return alpha_k

def _check_almijo(alpha: float, xi: float, g, h):
    lhs = g(alpha)
    rhs = h(alpha, xi)
    return lhs <= rhs


def main():
    g = lambda a: a**4 - 4*a**3 + a**2 - 6*a
    dg = lambda a: 4*a**3 - 12*a**2 + 2*a - 6
    d2g = lambda a: 12*a**2 - 24*a + 2
    h = lambda a, xi: -6*xi*a
    
    alpha_0 = 20
    xi = 0.5
    
    alpha_hat = linear_search_newton(g, dg, d2g, h, alpha_0, xi)
    
    print(f"Final alpha = {alpha_hat}")


if __name__ == "__main__":
    main()