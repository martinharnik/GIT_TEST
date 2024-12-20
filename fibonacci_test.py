import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} {kwargs}")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} returned {result}")
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@log_decorator
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
n = 10  # Change this value to generate more or fewer Fibonacci numbers
print(fibonacci(n))

# TEST CASES

# write a test case for the fibonacci function
def test_fibonacci():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

test_fibonacci()