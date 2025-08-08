"""
utilities.py

A growing collection of simple, reusable Python functions. These helpers cover
string manipulation and basic mathematics. Each function is written to be
self‑contained and independent of external libraries, making them easy to
reuse in varied contexts.
"""

import string
import math
from typing import Iterator


def to_snake_case(text: str) -> str:
    """Convert a string to snake_case.

    This function replaces spaces and hyphens with underscores, inserts an
    underscore before each capital letter that follows a lowercase letter,
    then lowercases the entire result.

    Parameters
    ----------
    text : str
        The input string, e.g. ``"HelloWorld"`` or ``"hello world"``.

    Returns
    -------
    str
        A snake_case version of the input, e.g. ``"hello_world"``.
    """
    result = []
    prev_is_lower = False
    for char in text:
        if char in (' ', '-'):
            if result and result[-1] != '_':
                result.append('_')
            prev_is_lower = False
        elif char.isupper():
            if prev_is_lower:
                result.append('_')
            result.append(char.lower())
            prev_is_lower = False
        else:
            result.append(char)
            prev_is_lower = True
    snake = ''.join(result).strip('_')
    return snake


def to_camel_case(text: str) -> str:
    """Convert a string to camelCase.

    The first word is lowercased; subsequent words are capitalised. All
    non‑alphanumeric characters are treated as separators.

    Parameters
    ----------
    text : str
        Input string such as ``"hello world"`` or ``"Hello_world"``.

    Returns
    -------
    str
        The camelCase version of the input, e.g. ``"helloWorld"``.
    """
    parts = []
    current = []
    for ch in text:
        if ch.isalnum():
            current.append(ch)
        else:
            if current:
                parts.append(''.join(current))
                current = []
    if current:
        parts.append(''.join(current))
    if not parts:
        return ''
    first, *rest = parts
    camel = first.lower() + ''.join(word.capitalize() for word in rest)
    return camel


def remove_punctuation(text: str) -> str:
    """Return a copy of the string with all punctuation removed.

    Parameters
    ----------
    text : str
        The input string.

    Returns
    -------
    str
        The input string without punctuation characters.
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome.

    The check ignores case and punctuation. White space is also ignored.

    Parameters
    ----------
    text : str
        The candidate string.

    Returns
    -------
    bool
        True if the input is a palindrome, False otherwise.
    """
    cleaned = remove_punctuation(text).replace(' ', '').lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number.

    Uses an iterative approach. The sequence is defined for n >= 0 with
    ``fibonacci(0) == 0`` and ``fibonacci(1) == 1``.

    Parameters
    ----------
    n : int
        Index into the Fibonacci sequence. Must be non‑negative.

    Returns
    -------
    int
        The nth Fibonacci number.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non‑negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def factorial(n: int) -> int:
    """Compute the factorial of n.

    Uses an iterative loop for efficiency. ``factorial(0)`` returns 1.

    Parameters
    ----------
    n : int
        Non‑negative integer.

    Returns
    -------
    int
        The factorial of n.

    Raises
    ------
    ValueError
        If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non‑negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n: int) -> bool:
    """Determine whether n is a prime number.

    A prime number is greater than one and has no positive divisors other than 1
    and itself.

    Parameters
    ----------
    n : int
        Candidate number.

    Returns
    -------
    bool
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True