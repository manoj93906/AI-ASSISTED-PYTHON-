from typing import Callable, Dict


def _rectangle_area(length: float, width: float) -> float:
    return length * width


def _square_area(side: float, _: float = 0) -> float:
    return side * side


def _circle_area(radius: float, _: float = 0) -> float:
    return 3.14 * radius * radius


_AREA_DISPATCH: Dict[str, Callable[[float, float], float]] = {
    "rectangle": _rectangle_area,
    "square": _square_area,
    "circle": _circle_area,
}


def calculate_area(shape: str, x: float, y: float = 0) -> float:
    """Calculate the area of a supported shape.

    Args:
        shape: One of 'rectangle', 'square', or 'circle'.
        x: Primary dimension (length, side, or radius).
        y: Secondary dimension (width) for rectangles; ignored otherwise.
    """
    try:
        calculator = _AREA_DISPATCH[shape.lower()]
    except KeyError as exc:
        raise ValueError(f"Unsupported shape: {shape}") from exc
    return calculator(x, y)
  
