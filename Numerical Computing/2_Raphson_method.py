def f(x):
    return (x**2) - 9

def df(x):
    return 2*x

def raphson(a, n):
    x = a  # Save our starting guess into x
    
    # Run the loop for the number of times requested
    for i in range(n):
        if df(x) == 0:
            print(f"Iteration {i}: Slope is zero! Cannot continue.")
            return
        x = x - (f(x) / df(x))
        print(f"Iteration no {i+1:02d} :\t Current Estimate: {x:.10f}")
        
# ------------main------------
if __name__ == "__main__":
    start = 5           # Our starting guess
    no_iterations = 6   # How many times to run the loop
    
    raphson(start, no_iterations)
