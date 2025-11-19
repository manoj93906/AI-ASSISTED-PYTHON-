import sympy as sp

def prompt_float(prompt: str, default: float) -> float:
    """Prompt the user for a floating-point value, using default if blank."""
    while True:
        raw = input(f"{prompt} [default {default}]: ").strip()
        if not raw:
            return default
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")

def find_minimum(a: float, b: float, c: float):
    if a == 0:
        if b == 0:
            return {
                "type": "constant",
                "message": f"The function is constant; f(x) = {c} for all x.",
            }
        slope_sign = "positive" if b > 0 else "negative"
        direction = "increasing" if b > 0 else "decreasing"
        return {
            "type": "linear",
            "message": (
                f"The function is linear with {slope_sign} slope and is strictly "
                f"{direction}; it has no finite minimum."
            ),
        }

    x = sp.symbols("x", real=True)
    f = a * x**3 + b * x + c
    derivative = sp.diff(f, x)
    second_derivative = sp.diff(derivative, x)

    minima = []
    for critical_point in sp.solve(sp.Eq(derivative, 0), x):
        numeric_point = complex(critical_point.evalf())
        if abs(numeric_point.imag) > 1e-9:
            continue  # Skip non-real stationary points
        curvature = float(second_derivative.subs(x, critical_point).evalf())
        if curvature > 0:
            value = float(f.subs(x, critical_point).evalf())
            minima.append((float(numeric_point.real), value))

    if minima:
        minima.sort(key=lambda item: item[1])
        best_x, best_value = minima[0]
        return {
            "type": "minimum",
            "x_min": best_x,
            "f_min": best_value,
            "message": f"Minimum occurs at x = {best_x:.4f}, where f(x) = {best_value:.4f}",
        }

    return {
        "type": "none",
        "message": (
            "The derivative has no real roots, so the function is strictly monotonic "
            "and does not attain a finite minimum."
        ),
    }

if __name__ == "__main__":
    print("Analyze f(x) = ax^3 + bx + c")
    print("Enter coefficients manually, or press Enter to keep defaults (2x^3 + 4x + 5).")

    a_coeff = prompt_float("Coefficient a", 2.0)
    b_coeff = prompt_float("Coefficient b", 4.0)
    c_coeff = prompt_float("Constant term c", 5.0)

    result = find_minimum(a_coeff, b_coeff, c_coeff)
    print(result["message"])
import sympy as sp

def find_minimum():
    x = sp.symbols("x", real=True)
    f = 2 * x**3 + 4 * x + 5

    derivative = sp.diff(f, x)
    critical_points = sp.solve(sp.Eq(derivative, 0), x)

    real_points = [pt for pt in critical_points if sp.im(pt) == 0]

    if real_points:
        minima = [(pt, f.subs(x, pt).evalf()) for pt in real_points]
        minima.sort(key=lambda item: item[1])
        return {
            "has_real_minimum": True,
            "minimum_point": float(minima[0][0]),
            "minimum_value": float(minima[0][1]),
        }

    return {
        "has_real_minimum": False,
        "message": (
            "f(x) = 2x^3 + 4x + 5 has derivative 6x^2 + 4 > 0 for all real x, "
            "so the function is strictly increasing and unbounded below "
            "(no finite x gives a real minimum)."
        ),
    }

if __name__ == "__main__":
    result = find_minimum()
    if result["has_real_minimum"]:
        print(f"Minimum occurs at x = {result['minimum_point']}")
        print(f"Minimum value f(x) = {result['minimum_value']}")
    else:
        print(result["message"])
