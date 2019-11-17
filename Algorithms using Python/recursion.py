#First simple example of recursion

def countdown(i):
    print(i)
    if i <=0: # Base case
        return
    else:
        countdown(i-1) # Recursive case

print(countdown(10))

# The recursive functions use the call stack


def factorial(x):
    if x==1:
        return 1
    else : 
        return x * factorial(x-1)


print('The factorial of 3 is',factorial(3))