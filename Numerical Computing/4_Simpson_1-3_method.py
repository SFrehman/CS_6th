def f(x):
    return 1/(1+x)

def Simpson_1_3(start,end,n,h):
    total_sum = f(start) + f(end)
    x=start
    for i in range(1,n):
        x=x+h
        if x%2 != 0:
            total_sum += 4 * f(x)
        else:
            total_sum += 2 * f(x)
    result = (h/3) * (total_sum)
    print(f"Result : {result}")

        
# ------------main------------
if __name__=="__main__":
    a = 0
    b = 1
    points = 3
    no_itrations = points - 1
    h = (b - a)/ no_itrations
    Simpson_1_3(a,b,no_itrations,h)