def f(x): 
    return (x**2) - 9 

def bisection(a, b, n):

    # Check if a root exists in the given interval first
    if f(a) * f(b) > 0:
        print("Solution in these roots does not exist")
        return
    
    # Loop for upto no of itrations
    for i in range(n):
        mid = (a + b) / 2
        
        if f(mid) == 0 or (-0.001 < f(mid) < 0.001):
            print(f"iteration no {i} :\t Solutions : {mid}")
            print(f"Found solution at itration {i} : sol : {mid:.0f}")
            break
        elif f(a) * f(mid) > 0:
            a = mid
        else:
            b = mid
        print(f"iteration no {i} :\t Solutions : {mid}")
        
# ------------main------------
if __name__ == "__main__": 
    start = 0
    end = 5
    no_iterations = 20
    bisection(start, end, no_iterations)

