# Fibonacci Sequence in Python

This repository contains a Python implementation of the Fibonacci sequence.

## Description

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This implementation provides a simple way to generate Fibonacci numbers up to a specified limit.

## Usage

To use the Fibonacci sequence generator, simply run the `fibonacci.py` script with the desired limit.

### Example

```python
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

# Generate Fibonacci sequence up to 1000
fibonacci(1000)
```

## Requirements

- Python 3.x

## Installation

Clone the repository:

```bash
git clone https://github.com/martinharnik/GIT_TEST.git
cd GIT_TEST
```

## Running the Script

Run the script with Python:

```bash
python fibonacci.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Author

Martin Harnik