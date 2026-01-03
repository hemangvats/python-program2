#Hemang Vats XII A Vocabulary builder
import csv
import os
def menu():
    print("""WELCOME TO VOCABULARY BUILDER
Please select your action
1. ADD
2. MODIFY
3. DELETE
4. DISPLAY
5. EXIT""")
def add():
    f=open('ap.csv','a',newline='')
    try:
        l=[]
        word=input('Enter word:')
        l.append(word)
        mean=input('Enter meaning of the word:')
        l.append(mean)
        sy=input('Enter synonym of the word:')
        l.append(sy)
        ay=input('Enter antonym of the word:')
        l.append(ay)
        sm1=input('Enter similar word:')
        l.append(sm1)
        sm2=input('Enter similar word:')
        l.append(sm2)
        c=csv.writer(f)
        c.writerow(l)
    except:
        print('Enter valid values')
    finally:
        f.close()
def display():
    f=open('ap.csv','r',newline='')
    r=csv.reader(f)
    for x in r:
        for y in x:
            if y==x[0]:
                print('Word:',y)
            elif y==x[1]:
                print('Meaning:',y)
            elif y==x[2]:
                print('Synonym:',y)
            elif y==x[3]:
                print('Antonym:',y)
            elif y==x[4]:
                print('One of the similar word is:',y)
            elif y==x[5]:
                print('The other similar word is:',y)
            else:
                continue
        print()
    f.close()
def selective(word):
    f=open('ap.csv','r',newline='')
    r=csv.reader(f)
    for x in r:
        if x[0]==word:
            for y in x :
                if y==x[0]:
                    print('Word:',y)
                elif y==x[1]:
                    print('Meaning:',y)
                elif y==x[2]:
                    print('Synonym:',y)
                elif y==x[3]:
                    print('Antonym:',y)
                elif y==x[4]:
                    print('One of the similar word is:',y)
                elif y==x[5]:
                    print('The other similar word is:',y)
                else:
                    continue
        else:
            continue
    f.close()
def delete(word):
    f=open('ap.csv','r',newline='')
    f1=open('temp.csv','w',newline='')
    r=csv.reader(f)
    c=csv.writer(f1)
    for x in r:
        if x[0]==word:
            continue
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('ap.csv')
    os.rename('temp.csv','ap.csv')
def modify(word,old):
    f=open('ap.csv','r',newline='')
    f1=open('temp.csv','w',newline='')
    r=csv.reader(f)
    c=csv.writer(f1)
    for x in r:
        if x[0]== word:
            if old==1:
                print('Sorry the word cannot be changed')
            elif old==2:
                mean=input('Enter the new meaning:')
                x[1]=mean
            elif old==3:
                sy=input('Enter new synonym of the word:')
                x[2]=sy
            elif old==4:
                ay=input('Enter new antonym of the word:')
                x[3]=ay
            elif old==5:
                sm1=input('Enter new similar word:')
                x[4]=sm1
            elif old==6:
                sm2=input('Enter another new similar word:')
                x[5]==sm2
            c.writerow(x)
        else:
            c.writerow(x)
    f.close()
    f1.close()
    os.remove('ap.csv')
    os.rename('temp.csv','ap.csv')
x='yes'
while x=='yes':
    menu()
    no=int(input('Enter your choice by entering the number:'))
    if no==1:
        add()
        print('The data is added')
        print()
        continue
    elif no==2:
        try:
            word=input('Enter the word you want to edit:')
            print("""1. Word
2. Meaning
3. Synonym
4. Antonym
5.First Similar Word
6. Second Similar Word""")
            old=int(input('Enter the number of the data you want to edit:'))
        except:
            print('Enter valid values')
        if (old>6)and (old<1):
            print('Enter valid choice')
            print()
            continue
        else:
            modify(word,old)
            print('The data is modified')
            print()
            continue
    elif no==3:
        try:
            word=input("Enter the word which you need to delete:")
        except:
            x='Enter valid values'
        delete(word)
        print('The data is deleted')
        print()
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
            word=input("Enter the word whose data you need to display:")
            selective(word)
            print()
            continue
        else:
            print('Enter valid choice')
            print()
            continue
    elif no==5:
        print('Thank you')
        break
    else:
        print('Enter valid choice')
        print()
        continue
        
    
    
    
