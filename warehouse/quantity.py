"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Parse a pick-list quantity string into a non-negative integer.

    Raises:
        ValueError: If the value cannot be parsed or is negative.
    """
    result = int(value.strip())
    if result < 0:
        raise ValueError(f"Quantity must be non-negative, got {result}")
    return result
