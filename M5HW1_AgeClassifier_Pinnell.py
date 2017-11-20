#CTI 110
#M5HW1- Age Classifier
#Evan Pinnell
#11/20/17

def main():

    age = int(input(' Enter Your Age:'))

    if age <= 1:
        print ('You are an infant')
    elif 1 < age < 13:
        print ('You are a child')
    elif 13 <= age < 20:
        print ('You are a teenager')
    else:
        print ('You are an adult')

main()
        
        

    
