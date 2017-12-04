#Converting feet to inches
#12/3/17
#CTI-110 M7T2_FeetToInches
#Evan Pinnell

INCHES_PER_FOOT = 12 #global constant

def main():
    feet = int(input('Enter a number of feet:'))
    print(feet,'equals', feet_to_inches(feet), 'inches')
    
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
