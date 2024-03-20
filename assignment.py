def fibonacci_sequence(n):
    fibonacci = [0, 1]  # Initialize the Fibonacci sequence with the first two terms

    # Generate the Fibonacci sequence up to the specified term n
    while len(fibonacci) < n:
        next_term = fibonacci[-1] + fibonacci[-2]  # Calculate the next term
        fibonacci.append(next_term)  # Add the next term to the sequence

    return fibonacci[:n]  # Return the first n terms of the Fibonacci sequence

def main():
    # Ask the user to input the value of n
    n = int(input("Enter the value of n: "))

    # Generate the Fibonacci sequence
    fibonacci_sequence_list = fibonacci_sequence(n)

    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, "is:", fibonacci_sequence_list)

if __name__ == "__main__":
    main()
