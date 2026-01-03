# Hemang Vats, XII-A , An software to maintain records of the customers of a particular jewellery shop
import pickle
import os
def menu():
    print("""Welcome to Ratna Jewellers <.>
Today Rates:
Gold22carat price is 4,500(in Indian Rupees)(per gram)
Gold24carat price is 4,900(in Indian Rupees)(per gram)
Silver price is 58.91(in Indian Rupees)(per gram)
Dimond costs 1,00,000(in Indian Rupees)(per piece)

Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    f=open('jewel.dat','ab')
    l=[]
    try:
        name=input('Enter Customer Name:')
        l.append(name)
        phone=input("Enter Customer's Phone Number:")
        l.append(phone)
        pan=input("Enter Customer's Pan Number:")
        l.append(pan)
        date=input('Enter Date in the Formate (DD/MM/YYYY):')
        l.append(date)
        count=int(input('Enter Number of objects:'))
        l.append(count)
        for x in range(0,count):
                print()
                metal=input('Enter Type of Metal with specific details:')
                if metal not in ('Diamond','diamond','gold22carat','Gold22carat','silver','Silver','gold24carat','Gold24carat'):
                    print('Enter vaild metal')
                    for p in range(1,5):
                        metal=input('Enter Type of Metal with specific details:')
                        if metal not in ('Diamond','diamond','gold22carat','Gold22carat','silver','Silver','gold24carat','Gold24carat'):
                            print('Enter vaild metal')
                            continue
                        else:
                            break
                    if p>=4:
                        print('Please fill the form from the begining')
                        print('-------------------------------------------------------------------------------------------')
                        continue
                if metal in ('Diamond','diamond'):
                    t=input('Enter the metal in which it is embedded:')
                    if t not in ('gold22carat','Gold22carat','silver','Silver','gold24carat','Gold24carat'):
                        print('Enter vaild metal')
                        for u in range(1,5):
                            t=input('Enter the metal in which it is embedded:')
                            if t not in ('gold22carat','Gold22carat','silver','Silver','gold24carat','Gold24carat'):
                                print('Enter vaild metal')
                                continue
                            else:
                                break
                        if u>=4:
                            print('Please fill the form from the begining')
                            print('-------------------------------------------------------------------------------------------')
                            continue
                    num1=int(input('Enter number of diamonds:'))
                    l.append(metal+t)
                else:
                    l.append(metal) 
                orna=input('Enter Type of Ornaments:')
                l.append(orna)
                quantity=int(input('Enter Qauntity of Ornaments:'))
                l.append(quantity)
                weight=float(input('Enter Weight of the Metal:'))
                l.append(weight)
                if metal in('gold22carat','Gold22carat'):
                    cost=weight*4500
                elif metal in ('silver','Silver'):
                    cost=weight*58.91
                elif metal in ('gold24carat','Gold24carat'):
                    cost=weight*4900
                elif metal in ('diamond','Diamond'):
                    if t in('gold22carat','Gold22carat'):
                       cost=(weight*4500)+(num1*100000)
                    elif t in ('silver','Silver'):
                        cost=(weight*58.91)+(num1*100000)
                    elif t in ('gold24carat','Gold24carat'):
                        cost=(weight*4900)+(num1*100000)
                l.append(cost)
        pickle.dump(l,f)
    except:
        print('Please enter valid values')
    finally:
        f.close()
def display():
    f=open('jewel.dat','rb')
    try:
        while(f):
            l=pickle.load(f)
            for x in l:
                if x==l[0]:
                    print('Name:',x)
                    print()
                elif x==l[1]:
                    print("Phone Number:",'+91',x)
                    print()
                elif x==l[2]:
                    print('Pan Number:',x)
                    print()
                elif x==l[3]:
                    print('Date of Billing:',x)
                    print()
                elif x==l[4]:
                    print('Count of Objects:',x)
                    print()
                elif x==l[5]:
                    print('Metal Type:',x)
                    print()
                elif x==l[6]:
                    print('Type of ornament:',x)
                    print()
                elif x==l[7]:
                    print('Quantity of ornaments:',x)
                    print()
                elif x==l[8]:
                    print('Weight of the ornament:',x,'gm')
                    print()
                elif x==l[9]:
                    print('Cost','Rs',x,)
                    print()
            print()
    except:
        z='File completed'
    finally:
        f.close()
def selective(name):
    f=open('jewel.dat','rb')
    try:
        while(f):
            l=pickle.load(f)
            if name in l:
                for x in l:
                    if x==l[0]:
                        print('Name:',x)
                        print()
                    elif x==l[1]:
                        print("Phone Number:",'+91',x)
                        print()
                    elif x==l[2]:
                        print('Pan Number:',x)
                        print()
                    elif x==l[3]:
                        print('Date of Billing:',x)
                        print()
                    elif x==l[4]:
                        print('Count of Objects:',x)
                        print()
                    elif x==l[5]:
                        print('Metal Type:',x)
                        print()
                    elif x==l[6]:
                        print('Type of ornament:',x)
                        print()
                    elif x==l[7]:
                        print('Quantity of ornaments:',x)
                        print()
                    elif x==l[8]:
                        print('Weight of the ornament:',x,'gm')
                        print()
                    elif x==l[9]:
                        print('Cost','Rs',x,)
                        print()
                break
            else:
                continue
    except:
        z='File compeleted'
    finally:
        f.close()
def delete(name):
    f=open('jewel.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while(f):
            l=pickle.load(f)
            if name in l:
                continue
            else:
                pickle.dump(l,f1)
    except:
        z='File is complete'
    finally:
        f.close()
        f1.close()
        os.remove('jewel.dat')
        os.rename('temp.dat','jewel.dat')
def modify(word,old):
    f=open('jewel.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while(f):
            l=pickle.load(f)
            if word==l[0]:
                    if old==1:
                        print('Sorry you cannot change the name')
                    elif old==2:
                        phone=input("Enter Customer's New Phone Number:")
                        l[1]=phone
                    elif old==3:
                        pan=input("Enter Customer's New Pan Number:")
                        l[2]=pan
                    elif old==4:
                        date=input('Enter New Date in the Formate (DD/MM/YYYY):')
                        l[3]=date
                    elif old==5:
                        count=int(input('Enter Number of objects:'))
                        l[4]=count
                    pickle.dump(l,f1)
            else:
                pickle.dump(l,f1)
                continue
    except:
        z='File is complete'
    finally:
        f.close()
        f1.close()
        os.remove('jewel.dat')
        os.rename('temp.dat','jewel.dat')
x='yes'
while x=='yes':
    menu()
    no=int(input('Enter your choice by entering the number:'))
    if no==1:
        add()
        print('The data is added')
        continue
    elif no==2:
        name=input('Enter the name for which you need to edit the data:')
        print("""1. Name
2. Phone
3. Pan
4. Date 
5. Count""")
        old=int(input('Enter the number of the data you want to edit:'))
        if (old>6) and(old<1):
            print('Enter valid choice:')
            continue
        else:
            modify(name,old)
            print('The data is modified')
            continue
    elif no==3:
        try:
            name=input('Enter the name for which you need to delete the data:')
        except:
            x='Enter valid values'
        delete(name)
        print('The data is deleted')
        continue
    elif no==4:
        print("""1. COMPLETE
2. SELECTIVE""")
        try:
            num=int(input('Enter the number corresponding to your choice:'))
        except:
            x='Enter valid values'
        if num==1:
            display()
        elif num==2:
            name=input('Enter the name of the data which you need to display:')
            selective(name)
            continue
    elif no==5:
        print('Thank you for joining in')
        break
    else:
        print('Please enter valid number')
        continue