# The function we want to solve (we want to find where x**2 - 9 equals 0)
def f(x):
    return (x**2) - 9

# The derivative (slope) of our function
def df(x):
    return 2*x

def raphson(a, n):
    x = a  # Save our starting guess into x
    
    # Run the loop for the number of times requested
    for i in range(1, n + 1):
        # Safety check: if slope is 0, the math breaks (cannot divide by zero)
        if df(x) == 0:
            print(f"Iteration {i}: Slope is zero! Cannot continue.")
            return
        
        # The main formula: calculate the next, better guess for x
        x = x - (f(x) / df(x))
        
        # Print the current step and the new answer
        print(f"Iteration no {i:02d} :\t Current Estimate: {x:.10f}")
        
# ------------main------------
if __name__ == "__main__":
    start = 5           # Our starting guess
    no_iterations = 6   # How many times to run the loop
    
    raphson(start, no_iterations)
