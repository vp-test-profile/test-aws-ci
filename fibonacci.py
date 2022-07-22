# Fibonacci Series
def fibonacci_seq(number):
    if number <= 1:
        return number
    else:
        fib_num = (fibonacci_seq(number-1) + fibonacci_seq(number-2))
    print('Fibonacci Generated')
    return fib_num
