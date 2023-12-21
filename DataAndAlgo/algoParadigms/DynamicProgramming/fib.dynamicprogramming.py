
def dynamic_fib(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dynamic_fib(n-1) + dynamic_fib(n-2)
    return lookup[n]
    

lookup = [None]*(1000)
for i in range(6):
    print(dynamic_fib(i))