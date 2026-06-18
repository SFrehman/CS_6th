def f(x):
    return (1/(1+x**5))

def Simpson_3_8(start,end,n,h):
    total_sum = f(start) + f(end)
    x=start
    for i in range(1,n):
        x=x+h
        if(i%3 == 0):
            total_sum += 2 * f(x)
        else:
            total_sum += 3 * f(x)
    result = ((3*h)/8) * (total_sum)
    print(f"Result : {result}")

        
# ------------main------------
if __name__=="__main__":
    a = 0
    b = 3
    points = 7
    no_itrations = points - 1
    h = (b - a)/ no_itrations
    Simpson_3_8(a,b,no_itrations,h)