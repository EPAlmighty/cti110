#CTI 110
#M6HW1- Distance Traveled
#Evan Pinnell
#11/29/17

def main():

    speed = int(input('What is the speed of the vehicle in mph?'))
    time = int(input('How many hours have you traveled?'))

    print('Hour\t\t\t Distance traveled')
    print('------------------------------------------')
    

    for t in range(1, time+1):
        distance= speed * t
        print(t,"\t\t\t",distance)

main()        

    
