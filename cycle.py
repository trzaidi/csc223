def cycle():
    # Read integers a, b, c, and M
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    M = int(input("Enter M: "))
    
    # Phase I: Find a point on the cycle using Floyd's Tortoise and Hare algorithm
    slow = c
    fast = (a * c + b) % M
    
    while slow != fast:
        slow = (a * slow + b) % M
        fast = (a * (a * fast + b) + b) % M  # Fast moves twice as fast as slow
    
    # Phase II: Compute the cycle length
    cycle_start = slow
    cycle_length = 1
    fast = (a * slow + b) % M
    
    while fast != cycle_start:
        fast = (a * fast + b) % M
        cycle_length += 1
    
    print(f"Cycle length is {cycle_length}.")

# Example to test the function
cycle()
