#CTI 110
#M5T1-AreaOfRectangle
#Evan Pinnell
#11/20/17

def main():

    length1 = int(input('enter the length of rectangle one:'))
    width1 = int(input('enter the width of rectangle one:'))

    length2 = int(input('enter the length of rectangle two:'))
    width2 = int(input('enter the width of rectangle two:'))

    area1 = length1 * width1
    area2 = length2 * width2

    if area1 > area2:
        print(' Recangle one is larger')
    elif area2 > area1:
        print ('Rectangle two is larger')
    else:
        print ('They are the same size')
        
main()
