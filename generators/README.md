# Generators in Python

This folder contains examples and demonstrations of Python generators.

## What are Generators?

Generators are special functions that use `yield` instead of `return` to produce values lazily, one at a time. They are memory-efficient and powerful tools for working with sequences of data.

## Why Use Generators?

- **Memory Efficient**: Generate values on-demand instead of storing everything in memory
- **Lazy Evaluation**: Values computed only when needed
- **Infinite Sequences**: Can represent endless streams of data
- **State Preservation**: Function remembers where it left off between calls
- **Pipeline Processing**: Chain generators together for efficient data processing

## Files in this Directory

- `generator_example.py` - Comprehensive examples demonstrating:
  - Simple countdown generator
  - Fibonacci sequence generator
  - File reading with generators
  - Infinite sequence generation
  - Generator expressions vs list comprehensions

## Running the Examples

```bash
python generator_example.py
```

## Quick Example

```python
def fibonacci(limit):
    """Generate Fibonacci numbers up to a limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci(100):
    print(num, end=" ")
# Output: 0 1 1 2 3 5 8 13 21 34 55 89
```

## Key Concept

The `yield` keyword pauses the function and returns a value, but saves its state so it can resume where it left off on the next call.
