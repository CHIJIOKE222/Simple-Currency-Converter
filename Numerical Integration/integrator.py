def f(x):
    """The function we want to integrate. You can change this to any math expression."""
    return x**2

def trapezoidal_rule(a, b, n):
    """
    Calculates the integral of f(x) from a to b using n subdivisions.
    Formula: (h/2) * [f(a) + 2*sum(f(x_i)) + f(b)]
    """
    h = (b - a) / n
    total_sum = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x_i = a + i * h
        total_sum += f(x_i)
        
    return total_sum * h

def main():
    print("--- Numerical Integration Tool (Trapezoidal Rule) ---")
    print("Integrating f(x) = x^2")
    
    try:
        lower_limit = float(input("Enter the lower limit (a): "))
        upper_limit = float(input("Enter the upper limit (b): "))
        subdivisions = int(input("Enter the number of sub-intervals (n): "))

        if subdivisions <= 0:
            print("Number of intervals must be a positive integer.")
            return

        result = trapezoidal_rule(lower_limit, upper_limit, subdivisions)
        print(f"\nEstimated Integral: {result:.6f}")
        
    except ValueError:
        print("\nError: Please enter valid numbers.")

if __name__ == "__main__":
    main()