#CTI 110
#M6T2- Bug Collector
#Evan Pinnell
#11/29/17

def main():

    total = 0

    for day in range(1, 8):
        print('Enter the bugs collected on day', day)
        bugs = int(input())
        total += bugs

    print('You collected a total of', total, 'bugs')

main()    
        
    
