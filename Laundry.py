import csv
import datetime

def main():

    global rn,name,date
    l_list=[[1],]
    totalcost=0
    print('\n\tWelcome to Sapphires Laundry\n')
    print('You can avail 10% discount if total cost exceeds 5000')
    rn=int(input('Enter room number: '))
    name=input('Enter guest name: ')

    isvalid=False
    while isvalid==False:
        date=input('Enter Date: ')
        isvalid=dateValid(date)
    
    dlaundry={'T-shirt':200,'Shorts':300,'Saree':500,'Dhoti':350,'Jacket':450,
              'Sweater':500, 'Suit':800}
    print('\n\nEnter END when you want to exit the Laundry menu')

    while True:
        item=input('\nEnter item: ')
        if item=='END' :
            break
        elif item not in dlaundry:
            print('\t\t Error! Unspecified service!')
            print('Please try again')
        else:
            n=int(input('Enter quantity: '))
            cost= dlaundry[item]*n
            i= [item , n , cost]
            l_list.append(i)
            totalcost += cost

    if totalcost>=5000:
        discount=0.1*totalcost
        totalcost-=discount
    
    l_list.append(totalcost)
    print_bill(l_list)
    print('Payment to be made when guests check out\n\n')

    with open ('Sapphire.csv','a') as f:
        mywriter=csv.writer(f)
        mywriter.writerow([rn,date,'Laundry',totalcost])

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
    print('Name of guest: ',name)
    print('Room number: ',rn)
    print('Date: ',date)
    print('---------------------------------------')
    print('ITEM\t\tQTY\t\tCOST')
    print('---------------------------------------')
    for i in range (1,len(lst)):
        print(lst[i][0],'\t\t',lst[i][1],'\t\t',lst[i][2],'INR')
        tot+=lst[i][2]
    print('---------------------------------------')
    print('Total: ',tot,'INR')
    print('Discount offered: ',(tot-grand_tot),'INR')
    print('Grand total: ',grand_tot,'INR')
    print('---------------------------------------\n\n')
    

                
                
            
