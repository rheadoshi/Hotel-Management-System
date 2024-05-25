import csv
import datetime
def main():

    print('\n\tWelcome to Sapphires Sports and Healthcare Centre\n')

    global rn, grname, date
    
    rn=int(input('Enter room number: '))
    grname=input('Enter Guest name: ')
    isvalid=False
    while isvalid==False:
        date=input('Enter Date: ')
        isvalid=dateValid(date)
    print('\nEnter 0 to return back')
    print('1. Sports')
    print('2. Spa')
    print('3. Gym')
    choice=int(input('Enter your choice: '))
    if choice==1:
        sports()
    elif choice==2:
        spa()
    elif choice==3:
        gym()
    else:
        return

def dateValid(date):
    d=date.split('/')
    valid=True
    try:
        datetime.datetime(int(d[2]),int(d[1]),int(d[0]))
    except ValueError:
        valid=False
    return valid

def print_bill(lst):
    tot=0
    grand_tot=lst.pop(-1)
    print('\n\n\tBILL')
    print('---------------------------------------')
    print('Name of guest: ',grname)
    print('Room number: ',rn)
    print('Date: ',date)
    print('---------------------------------------')
    print('SERVICE\t\tQTY\t\tCOST')
    print('---------------------------------------')
    for i in range (1,len(lst)):
        if lst[i][0]=='Sauna':
            lst[i][0]='Sauna\t' 
        print(lst[i][0],'\t',lst[i][1],'\t\t',lst[i][2],'INR')
        tot+=lst[i][2]
    print('---------------------------------------')
    print('Total: ',tot,'INR')
    print('Discount offered: ',(tot-grand_tot),'INR')
    print('Grand total: ',grand_tot,'INR')
    print('---------------------------------------\n\n')
    
def sports():
    s_list=[[1],]
    totalcost=0
    
    print('\n\tWelcome to Sapphires Sports Centre')
    print('Avail 15% discount if costs exceed 800 INR')

    sports={'Basketball':200, 'Swimming':100, 'Table Tennis':150,
            'Lawn Tennis':250, 'Football':300, 'Archery':350}
    print('\nBasketball\t\t',sports['Basketball'],'INR')
    print('\nFootball\t\t',sports['Football'],'INR')
    print('\nSwimming\t\t',sports['Swimming'],'INR')
    print('\nTable Tennis\t',sports['Table Tennis'],'INR')
    print('\nLawn Tennis\t',sports['Lawn Tennis'],'INR')
    print('\nArchery\t\t',sports['Archery'],'INR')

    print('\n\nEnter END when you want to exit the sports menu')
    while True:
        service=input('\nEnter Service: ')
        if service=='END' :
            break
        elif service not in sports:
            print('\t\t Error! Unspecified service!')
            print('Please try again')
        else:
            n=int(input('Enter number of days of membership: '))
            cost= sports[service]*n
            i= [service , n , cost]
            s_list.append(i)
            totalcost += cost

    if totalcost>=800:
        discount=0.15*totalcost
        totalcost-=discount
    
    s_list.append(totalcost)
    print_bill(s_list)
    print('Payment to be made when guests check out\n\n')

    with open ('Sapphire.csv','a') as f:
        mywriter=csv.writer(f)
        mywriter.writerow([rn,date,'Sports',totalcost])
   
def spa():
    spalist=[[1],]
    totalcost=0
    
    print('\n\tWelcome to Sapphires Spa Centre')
    print('Avail 25% discount if costs exceed 700 INR')

    spa={'Massage':1000, 'Sauna':750, 'Steam Room':600}

    print('\nMassage\t\t',spa['Massage'],'INR')
    print('Sauna\t\t',spa['Sauna'],'INR')
    print('Steam Room\t',spa['Steam Room'],'INR')
    print('\n\nEnter END when you want to exit the spa menu')
    while True:
        service=input('\nEnter Service: ')
        if service=='END' :
            break
        elif service not in spa:
            print('\t\t Error! Unspecified service!')
            print('Please try again')
        else:
            cost= spa[service]
            i= [service , 1 , cost]
            spalist.append(i)
            totalcost += cost

    if totalcost>=700:
        totalcost=0.75*totalcost

    spalist.append(totalcost)
    print_bill(spalist)
    print('Payment to be made when guests check out\n\n')

    with open ('Sapphire.csv','a') as f:
        mywriter=csv.writer(f)
        mywriter.writerow([rn,date,'Spa',totalcost])

def gym():
    g_list=[[1],]
    
    print('\n\tWelcome to Sapphires Gym')
    print('Avail 20% discount if costs exceed 1500 INR')

    while True:
        try:
            n=int(input('Enter number of days of membership: '))
            cost= 1000*n
            i= ['Gym \t' , n , cost]
            g_list.append(i)

            if cost>=800:
                discount=0.15*cost
                cost-=discount
    
            g_list.append(cost)
            print_bill(g_list)
            print('Payment to be made when guests check out\n\n')
            break
        except ValueError:
            continue

    with open ('Sapphire.csv','a') as f:
        mywriter=csv.writer(f)
        mywriter.writerow([rn,date,'Gym',cost])


