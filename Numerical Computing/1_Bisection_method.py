def f(x): 
    return (x**2) - 9 

def bisection(a, b, n):
    if f(a) * f(b) > 0:
        print("Solution in these roots does not exist")
        return
    
    for i in range(n):  # Starting from 1 makes the iteration printout cleaner
        mid = (a + b) / 2
        
        if f(mid) == 0 or -0.0001<f(mid)<0.0001:
            print(f"Iteration no {i:02d} :\t Exact Solution Found: {mid:.4f}")
            return
        print(f"Iteration no {i+1:02d} :\t Current Guess: {mid:.4f} | Interval: [{a:.4f}, {b:.4f}]")
        # Update the boundaries
        if f(a) * f(mid) > 0:
            a = mid
        else:
            b = mid
        
# ------------main------------
if __name__ == "__main__": 
    start = 0
    end = 5
    no_iterations = 20
    bisection(start, end, no_iterations)
