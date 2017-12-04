#CTI 110
##M6HW3- Factorial
#Evan Pinnell
#12/1/17

def main():

    total = 0
    n = int(input('Enter a nonnegative integer:'))
       
    while n<0:
        n = int(input('Enter a nonnegative integer:'))
    if n<=1:
        print(1)
    else:
        def factorial(n):
            num = 1
            while n >= 1:
                num = num * n
                n = n - 1
            return num
        factorial(n)
        print(factorial(n))
        
                
    
main()        
