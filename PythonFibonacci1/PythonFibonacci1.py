
# The following code is based off of code found at educative.io
def fib(n):
    # The base cases
    if n <= 1:  # First number in the sequence
        return 0
    elif n == 2:  # Second number in the sequence
        return 1
    else:
        # Recursive call
        return fib(n - 1) + fib(n - 2)


print(fib(6))


#The Fibonacci sequence is a sequence of numbers where every number is the sum of the two numbers before it. The first two numbers are 0 and 1. In the above code, the print(fib()) can have any number in it, and it will correlate to the number in the fibonacci sequence at that index. Note that all inputs less than 1 are treated as incorrect. If the number inputted is larger than 2, then it will be the sum of the two values before it. So for example in print(fib(6)), the output would be 5, as that is the number it correlates to in the fibonacci sequence.
#The above code has the concept of recursion, that is, the function defined calls itself during the execution. And every cal goes deeper into the function, like going inside the layers of a box. There must be a base case defined for the recursions to stop and the original function to end, otherwise there will be an infinite loop.
#The recursive calls in the above code will stop at 0 and 1, since those are always the first two values in the fiboncacci sequence, thus being base cases.