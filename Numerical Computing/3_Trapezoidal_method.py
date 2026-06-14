def f(x):
    return 1/(x**2)

def Trapezoidal(start,end,n,h):
    total_sum = f(start) + f(end)
    x=start
    for i in range(1,n):
        x=x+h
        total_sum += 2* f(x)
    result = (h/2) * (total_sum)
    print(f"Result : {result}")

        
# ------------main------------
if __name__=="__main__":
    a = 1
    b = 3
    points = 3
    no_itrations = points - 1
    h = (b - a)/no_itrations
    Trapezoidal(a,b,no_itrations,h)
