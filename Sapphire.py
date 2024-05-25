import Booking as b
import SportsAndHealthcare as snh
import Laundry as l

def menu():

    while(True):
        print('\n================HOTEL SAPPHIRES================\n')
        print('\tWelcome to Sapphires hotel')
        print('There is a 10% family discount going on at present\n')
        print ('\n1. Check-In a Guest')
        print ('2. Check-Out a Guest')
        print ('3. Show information of hotel')
        print ('4. Sports and Healthcare Facilities')
        print ('5. Laundry Facilities')
        choice=int(input('\nEnter your choice: '))

        if choice==1:
            b.checkin()
        elif choice==2:
            b.checkout()
        elif choice==3:
            info()
        elif choice==4:
            snh.main()
        elif choice==5:
            l.main()
        else:
            break

def info():
    print("\n\tHOTEL INFORMATION")
    print('Sapphire is 3-star hotel in Agra associated with the Gems group.')
    print('It has 50 rooms that include 5 Suite rooms, 5 Deluxe rooms and 40 Queen rooms.')
    print('It offers many facilities including Laundry facilities and a Sports and Healthcare centre')
    print('\n\t"It is the most kid-friendly hotel in Agra" -The Times Magazine')

menu()        
    
