"""
Generator Examples in Python
Generators are functions that use 'yield' instead of 'return' to produce values lazily.
They are memory-efficient and great for working with large datasets.
"""

# Example 1: Simple Number Generator
def countdown(n):
    """Generate numbers from n down to 1"""
    print("Starting countdown...")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")


# Example 2: Fibonacci Generator
def fibonacci(limit):
    """Generate Fibonacci numbers up to a limit"""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


# Example 3: File Reader Generator (memory efficient)
def read_large_file(filename):
    """Read a file line by line without loading entire file into memory"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {filename} not found")


# Example 4: Infinite Generator
def infinite_sequence():
    """Generate infinite sequence of numbers"""
    num = 0
    while True:
        yield num
        num += 1


# Example 5: Generator Expression (like list comprehension but lazy)
def demonstrate_generator_expression():
    """Show generator expressions vs list comprehensions"""
    # List comprehension - creates entire list in memory
    list_comp = [x**2 for x in range(10)]
    print(f"List comprehension: {list_comp}")
    
    # Generator expression - lazy evaluation
    gen_exp = (x**2 for x in range(10))
    print(f"Generator expression: {gen_exp}")
    print(f"Values from generator: {list(gen_exp)}")


# Main demonstrations
if __name__ == "__main__":
    print("=" * 50)
    print("Example 1: Countdown Generator")
    print("=" * 50)
    for num in countdown(5):
        print(f"Count: {num}")
    
    print("\n" + "=" * 50)
    print("Example 2: Fibonacci Generator")
    print("=" * 50)
    fib_gen = fibonacci(100)
    print(f"Fibonacci numbers < 100: {list(fib_gen)}")
    
    print("\n" + "=" * 50)
    print("Example 3: Using next() with generator")
    print("=" * 50)
    counter = countdown(3)
    print(f"First call: {next(counter)}")
    print(f"Second call: {next(counter)}")
    print(f"Third call: {next(counter)}")
    # print(next(counter))  # Would raise StopIteration
    
    print("\n" + "=" * 50)
    print("Example 4: Infinite Generator (first 10)")
    print("=" * 50)
    inf_gen = infinite_sequence()
    for _ in range(10):
        print(next(inf_gen), end=" ")
    print()
    
    print("\n" + "=" * 50)
    print("Example 5: Generator Expression")
    print("=" * 50)
    demonstrate_generator_expression()
    
    print("\n" + "=" * 50)
    print("Key Benefits of Generators:")
    print("=" * 50)
    print("✓ Memory efficient - values generated on demand")
    print("✓ Can represent infinite sequences")
    print("✓ Can pause and resume execution")
    print("✓ Great for pipeline processing")
