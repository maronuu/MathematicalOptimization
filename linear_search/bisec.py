import numpy as np


def linear_search_bisect(
    g,
    h,
    alpha_0: float,
    xi: float,
) -> float:
    alpha = alpha_0
    k = 0
    print(f"{k}: alpha={alpha}")
    while True:
        if _check_almijo(alpha, xi, g, h):
            print(f"Almijo constraint is satisfied at k = {k}")
            break
        alpha *= 0.5
        print(f"{k}: alpha={alpha}")
        k += 1
    
    return alpha


def _check_almijo(alpha: float, xi: float, g, h):
    lhs = g(alpha)
    rhs = h(alpha, xi)
    return lhs <= rhs


def main():
    g = lambda a: a**4 - 4*a**3 + a**2 - 6*a
    h = lambda a, xi: -6*xi*a
    
    alpha_0 = 1000
    xi = 0.25
    
    alpha_hat = linear_search_bisect(g, h, alpha_0, xi)
    
    print(f"Final alpha = {alpha_hat}")


if __name__ == "__main__":
    main()