import numpy as np


def linear_search_secant(
    g,
    dg,
    h,
    alpha_0: float,
    alpha_1: float,
    xi: float,
) -> float:
    alpha_k1 = alpha_0
    alpha_k = alpha_1
    
    k = 1
    print(f"{k}: alpha={alpha_k}")
    while True:
        if _check_almijo(alpha_k, xi, g, h):
            print(f"Almijo constraint is satisfied at k = {k}")
            break
        alpha_k, alpha_k1 = _calc_new_alpha(alpha_k, alpha_k1, dg)
        print(f"{k}: alpha={alpha_k}")
        k += 1
    
    return alpha_k

def _calc_new_alpha(alpha_k: float, alpha_k1:float, dg) -> float:
    new_alpha = alpha_k - dg(alpha_k) * (alpha_k - alpha_k1) / (dg(alpha_k) - dg(alpha_k1))
    return new_alpha, alpha_k

def _check_almijo(alpha: float, xi: float, g, h):
    lhs = g(alpha)
    rhs = h(alpha, xi)
    return lhs <= rhs


def main():
    g = lambda a: a**4 - 4*a**3 + a**2 - 6*a
    dg = lambda a: 4*a**3 - 12*a**2 + 2*a - 6
    h = lambda a, xi: -6*xi*a
    
    alpha_0 = 20
    alpha_1 = 10
    xi = 0.8
    
    alpha_hat = linear_search_secant(g, dg, h, alpha_0, alpha_1, xi)
    
    print(f"Final alpha = {alpha_hat}")


if __name__ == "__main__":
    main()