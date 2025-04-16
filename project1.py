import mysql.connector
print("******************************************************")
print("*                                                    *")
print("*     Welcome to Pharmacy Management System          *")               
print("*                                                    *")
print("******************************************************")
#______Creating Database_________
mydb=mysql.connector.connect(host="localhost",user="root",passwd='13082005')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists pysales_new")
mycursor.execute("use pysales_new")
#______Creating Required Tables________
mycursor.execute("create table if not exists login(username varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists purchase(odate date not null,name varchar(25) not null,pcode int not null,amount int not null)")
mycursor.execute("create table if not exists stock(pcode int not null,pname varchar(25) not null,quantity int not null,price int not null)")
mydb.commit()
z=0
mycursor.execute("select * from login")#==>Empty
for i in mycursor:
    z+=1
if z==0:
    mycursor.execute("insert into login values('username','ng')")
    mydb.commit()
while True:
    print("""
1.Admin
2.Customer
3.Exit
""")
    ch=int(input('Enter your choice:'))
#_____________________________ADMIN SECTION___________________________
    if ch==1:
        passs=input('Enter password:')
        mycursor.execute('select * from login')
        for i in mycursor:
            username,password=i
        if passs==password:
            print('WELCOME !')
            loop2='y'
        while loop2=='y' or loop2=='Y':
#_________More options in Admin Section____________
            print("""
     1.Add New Item
     2.Updating Price
     3.deleting Item
     4.Display All Items
     5.To Change the Password
     6.Log Out
""")
            ch=int(input('Enter your choice:'))
            if ch==1:#___To add new item
                loop='y'
                while loop =='y' or loop=='Y':
                    pcode=int(input('Enter product code:'))
                    pname=input('Enter product name:')
                    quantity=int(input('Enter product quantity:'))
                    price=int(input('Enter product price:'))
                    mycursor.execute("insert into stock values('"+str(pcode)+"','"+pname+"','"+str(quantity)+"','"+str(price)+"')")
                    mydb.commit()
                    print('Record Succesfully Inserted...')
                    loop=input('Do you want to enter more items..(y/n):')
                loop2=input('Do you want to continue editing stock..(y/n):')
            elif ch==2:#___To Update the price
                loop='y'
                while loop=='y' or loop=='Y':
                    pcode=int(input('Enter product code:'))
                    new_price=int(input('Enter new price:'))
                    mycursor.execute("update stock set price='"+str(new_price)+"'where pcode='"+str(pcode)+"'")
                    mydb.commit()
                    loop=input('Do you want to change the price of any other item..(y/n):')
                loop2=input('Do you want to continue editing stock..(y/n):')
            elif ch==3:#____To delete the items
                loop='y'
                while loop=='y' or loop=='Y':
                    pcode=int(input('Enter product code:'))
                    mycursor.execute("delete from stock where pcode='"+str(pcode)+"'")
                    mydb.commit()
                    loop=input('Do you want to delete any other data..(y/n):')
                loop2=input('Do you want to continue editing stock..(y/n):')
            elif ch==4:#_____To display all the items
                mycursor.execute('select * from stock')
                print('pcode || pname || quantity || price')
                for i in mycursor:
                    t_code,t_name,t_quan,t_price=i
                    print(f"{t_code}   ||   {t_name}   || {t_quan}   ||    {t_price}")
                n=input('Do you want to edit stock..(y/n):')
                if n=='y' or n=='Y':
                    continue
                else:
                    break
            elif ch==5:#_____To change the password
                    old_pass=input('Enter old password:')
                    mycursor.execute('select * from login')
                    for i in mycursor:
                        username,password=i
                    if old_pass==password:
                        new_pass=input('Enter new Password:')
                        mycursor.execute("update login set password='"+new_pass+"'")
                        mydb.commit()
            elif ch==6:#____If user wants to logout
                break
        else:
            print('Wrong password')
#_______________________CUSTOMER SECTION___________________________            
    elif ch==2:
#___________More options in Customer Section____________
        print("""
1.Item Bucket
2.Payment
3.View Available Items
4.Go Back
""")
        ch2=int(input('Enter your choice:'))
        if ch2==1:#______Item Bucket
            name=input('Enter your name:')
            pcode=int(input('Enter product code:'))
            quantity=int(input('Enter product quantity:'))
            mycursor.execute("select * from stock where pcode='"+str(pcode)+"'")
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
            amount=t_price*quantity
            net_quan=t_quan-quantity
            mycursor.execute("update stock set quantity ='"+str(net_quan)+"'where pcode='"+str(pcode)+"'")
            mycursor.execute("insert into purchase values(now(),'"+name+"','"+str(pcode)+"','"+str(amount)+"')")
            mydb.commit()
                
        elif ch2==2:#______Payment
            print('Amount to be paid:',amount)
        elif ch2==3:#______To view available items
            print('CODE || NAME || PRICE')
            mycursor.execute('select * from stock')
            for i in mycursor:
                t_code,t_name,t_quan,t_price=i
                print(f"{t_code} || {t_name} || {t_price}")
        elif ch2==4:#_______To go back
            break
#___________Exit___________________
    elif ch==3:
        break