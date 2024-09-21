def trace():
    # Read integers a, b, c, and M
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    M = int(input("Enter M: "))
    
    x = c  # Starting value (seed)
    
    for i in range(M):
        print(f"{x:4}", end=' ')  # Print the value with 4-character spacing
        if (i + 1) % 16 == 0:  # Newline after every 16 values
            print()
        x = (a * x + b) % M  # Update the next value using the formula

    print()  # Final newline

# Example to test the function
trace()

