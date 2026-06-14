def f(x):
    return (x**2) - 9

def df(x):
    return 2*x

def raphson(a, n):
    x = a
    for i in range(n):
        if df(x) == 0:
            print(f"Iteration {i}: Derivative is zero! Cannot divide by zero.")
            return

        # to stop loop when solution found
        if f(x) == 0 or (-0.001 < f(x) < 0.001):
            print(f"iteration no {i} :\t Solutions : {x}")
            print(f"Found at {i} :\t Sol : {x:.0f}")
            return
        
        # Main Formula of Raphson
        x = x - (f(x) / df(x))
        print(f"iteration no {i} :\t Solutions : {x}")
        
# ------------main------------
if __name__ == "__main__":
    start = 5
    no_itrations = 6

    raphson(start, no_itrations)
