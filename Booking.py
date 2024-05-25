import datetime
import csv

occupancy=[[0,0,0,0,0,0,0,0,0,0], #assuming hotel has 5 floor with 10 rooms each
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0]]

def dateValid(date):
    d=date.split('/')
    valid=True
    try:
        datetime.datetime(int(d[2]),int(d[1]),int(d[0]))#year/month/day
    except ValueError:
        valid=False
    return valid

def checkin():
    name=input('Enter name of guest: ')
    phone=input('Enter phone number: ')
    add=input('Enter home address: ')
    while True:
        print('\nPlease enter dates in dd/mm/yyyy format')
        ci_date=input('Enter check-in date: ')
        co_date=input('Enter check-out date: ')
        if dateValid(ci_date) and dateValid(co_date):
            ci= ci_date.split('/')
            date1=datetime.date(int(ci[2]),int(ci[1]),int(ci[0]))
            co= co_date.split('/')
            date2=datetime.date(int(co[2]),int(co[1]),int(co[0]))
            n_days= (date2-date1).days #to calculate days of stay
            if n_days<=0:
                print('\n\tKindly note checkout date must be after checkin date')
            else:
                break
        else:
            print('Invalid date(s) entered')
            
    num_g=int(input('Enter number of guests: '))
    if num_g>4:
        print('Congratulations! You are eligible for a 10% discount')
    num_r=int(input('\nEnter number of rooms required: '))
    room_cost_tot=0
    room={'Queen':5000, 'Deluxe':5500, 'Suite':6000}
    print('\tRoom types ')
    print('Kindly note that all prices mentioned are per night\n')
    for i in room:
        print(i,'\t\t',room[i],'INR')

    for i in range(num_r):
        while True:
            rch=input('\nEnter your choice: ')
            if rch not in room:
                print('Error!','Invalid Choice! Please try again!')
            else:
                rno=roomno(rch) 
                room_cost_tot+=room[rch]
                print('Your room number alloted are ',rno)
                break

    room_cost_tot*=n_days
    if num_g>4:
        room_cost_tot= 0.9*room_cost_tot
    print('\nYour total room rent is ',room_cost_tot,'INR')
    print('Payments to be made when guests check out')
    print('Romm rent is charged to Room number ',rno)

    with  open('Sapphire.csv','a') as f:
        mywriter=csv.writer(f)
        mywriter.writerow([rno,ci_date,'Room Rent',room_cost_tot])

def roomno(rtype):
    rno=0
    global occupancy
    for i in range(1,6):
        if rtype=='Suite':
            if occupancy[i-1][9]==0:
                occupancy[i-1][9]=1
                rno=i*100+9
                break
        elif rtype=='Deluxe':
            if occupancy[i-1][8]==0:
                occupancy[i-1][8]=1
                rno=i*100+8
                break
            elif occupancy[i][7]==0:
                occupancy[i][7]=1
                rno=i*100+7
                break
        else:
            for j in range(1,7):
                if occupancy[i-1][j-1]==0:
                    occupancy[i-1][j-1]=1
                    rno=i*100+(j)
                    break
    return rno

def checkout():
    data1=[]
    tot=0
    rno=input('Enter Room number: ')
    print('\n\n\tBILL')
    print('---------------------------------------')
    print('DATE\t\tITEM\t\tCOST')
    print('---------------------------------------')
    with open('Sapphire.csv','r') as f:
        data=csv.reader(f)
        for row in data:
            data1.append(row)
        data1=list(filter(None,data1))
        for row in data1:
            if row[0]==rno:
                print(row[1],'\t',row[2],'\t',row[3],'INR')
                tot+=float(row[3])
                data1.remove(row)
    f.close()
    print('---------------------------------------')
    print('Payment due :',tot)
    print('---------------------------------------')
    with open('Sapphire.csv','w') as f: 
        mywriter=csv.writer(f)
        for row in data1:
            mywriter.writerow(row)

