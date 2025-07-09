# fibonacci_generator.py

def generate_fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    try:
        num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
        if num_terms < 0:
            print("Please enter a non-negative integer.")
        else:
            sequence = generate_fibonacci(num_terms)
            print(f"First {num_terms} Fibonacci terms: {sequence}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()