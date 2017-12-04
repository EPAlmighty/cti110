#CTI 110
#M7T1- Kilometer Converter
#Evan Pinnell
#12/3/17

CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float(input('Enter distance in kilometers:'))
    show_miles(kilometers)

def show_miles(km):
    miles = km * CONVERSION_FACTOR
    print(km, 'kilometers equals', miles, 'miles.')

main()    
