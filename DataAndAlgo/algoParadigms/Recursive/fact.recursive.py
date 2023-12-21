# using recursive to solve the factorial problem

def factorial(n):
    # test the base case
    if n ==0:
        return 1
    # make a calculation and a recursive call
    else:
        return n*factorial(n-1)

print(factorial(4))
    
   
