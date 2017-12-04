#CTI 110
#M6HW2- Running Total
#Evan Pinnell
#12/1/17

def main():

    total = 0

    number = int(input('Enter a number:'))

    while number >=0:
        total += number
        number = int(input('Enter a number:'))

    print('Total:', total)    
        

main()        
        
    
                            
