# Generators in Python

This folder contains examples and demonstrations of Python generators.

## What are Generators?

Generators are special functions that use `yield` instead of `return` to produce values lazily, one at a time. They are memory-efficient and powerful tools for working with sequences of data.

## Why Use Generators?

### 1. Memory Efficiency

- They generate values on-demand rather than storing everything in memory
- Example: `range(1000000)` as a generator vs a list - generator uses minimal memory regardless of size

### 2. Lazy Evaluation

- Values are computed only when needed
- We can start processing data before the entire sequence is ready
- Perfect for large datasets or streaming data

### 3. Infinite Sequences

- Can represent endless streams (like `infinite_sequence()` in the example)
- Not possible with regular lists - they must be finite

### 4. State Preservation

- The function "remembers" where it left off between `yield` calls
- Local variables and execution state are maintained
- Like having a pause/resume button for a function

### 5. Pipeline Processing

- Can chain generators together efficiently
- Example: `(process(x) for x in filter(condition, data) for data in source())`
- Each stage processes one item at a time, not entire collections

### 6. Performance

- Faster startup time - no need to generate all values upfront
- Lower memory footprint = less garbage collection overhead

**Real-world example:** Reading a 10GB log file line-by-line with a generator uses ~constant memory. Loading it all as a list would require 10GB+ of RAM and could crash the program.

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

## Example Output

```
==================================================
Example 1: Countdown Generator
==================================================
Starting countdown...
Count: 5
Count: 4
Count: 3
Count: 2
Count: 1
Countdown finished!

==================================================
Example 2: Fibonacci Generator
==================================================
Fibonacci numbers < 100: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

==================================================
Example 3: Using next() with generator
==================================================
Starting countdown...
First call: 3
Second call: 2
Third call: 1

==================================================
Example 4: Infinite Generator (first 10)
==================================================
0 1 2 3 4 5 6 7 8 9 

==================================================
Example 5: Generator Expression
==================================================
List comprehension: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Generator expression: <generator object demonstrate_generator_expression.<locals>.<genexpr> at 0x102faaa80>
Values from generator: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

==================================================
Key Benefits of Generators:
==================================================
Memory efficient - values generated on demand
Can represent infinite sequences
Can pause and resume execution
Great for pipeline processing
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
