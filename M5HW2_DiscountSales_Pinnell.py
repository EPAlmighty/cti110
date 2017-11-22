#CTI 110
#M5HW1- Discount Sales
#Evan Pinnell
#11/201/17

def main():

   
    quantity = int(input( 'How many packages would you like:' ))
    price = quantity * 99
    
    if quantity >= 10 and quantity <=19:
        discount = float(quantity * .10)
        print ('Price:',discount * price)
    elif quantity >=20 and quantity <=49:
        discountTwo = float(quantity * .20)
        print ('Price:',discountTwo * price)
    elif quantity >=50 and quantity <=99:
        discountThree = float(quantity * .30)
        print ('Price:',discountThree * price)
    elif quantity >=100:
        discountFour = float(quantity *.40)
        print ('Price:', discountFour * price)
    else:
        print ('No Discount')

main()
