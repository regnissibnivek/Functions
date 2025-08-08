# Functions

This repository will host a collection of reusable Python functions and utilities. The goal is to build a library of clean, well‑documented code that you can drop into your other projects without modification.

## Contents

* `utilities.py` – includes functions for string manipulation and basic mathematics. Each function has a concise docstring that explains its purpose and usage.

## Usage

Clone this repository, then import the functions you need from `utilities.py`. Feel free to expand the collection by adding your own functions and submitting pull requests.

```python
from utilities import to_snake_case, fibonacci

print(to_snake_case("Hello World"))  # hello_world
print(fibonacci(10))  # 55
```

## Contributing

Keep the code style consistent: clear names, type hints, and docstrings. Include a simple usage example in your pull request description to show how your function works.