def add(a, b):
    """Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b

def subtract(a, b):
    """Subtract b from a.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Result of a - b

    Examples:
        >>> subtract(5, 2)
        3
        >>> subtract(10, 3.5)
        6.5
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers.

    Args:
        a: First factor (int or float)
        b: Second factor (int or float)

    Returns:
        Product of a and b

    Examples:
        >>> multiply(3, 4)
        12
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b

def divide(a, b):
    """Divide a by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float, must be non-zero)

    Returns:
        Quotient of a divided by b

    Raises:
        ValueError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(5, 2)
        2.5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent.

    Args:
        base: The base number (int or float)
        exponent: The exponent (int or float)

    Returns:
        Result of base^exponent

    Examples:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent

def factorial(n):
    """Calculate the factorial of a non-negative integer.

    Args:
        n: Non-negative integer

    Returns:
        Factorial of n

    Raises:
        ValueError: If n is negative

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)

def is_prime(n):
    """Check if a number is prime.

    Args:
        n: Positive integer greater than 1

    Returns:
        True if n is prime, False otherwise

    Raises:
        ValueError: If n <= 1

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(8)
        False
    """
    if n <= 1:
        raise ValueError("Input must be greater than 1")
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
