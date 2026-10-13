def factorial(n):
    
    if n == 0:
        return 1
    
    return n * factorial(n-1)


# Test the function 
x = 5
print(x, "! =", factorial(x))



def factorial(n):
    
    answer = 1
    for i in range(n, 1, -1): 
        answer = answer * i
    
    return answer

# Test the function 
x = 5
print(x, "! =", factorial(5)))
