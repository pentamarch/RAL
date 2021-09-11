import csv 

username = input("Enter username : ")

flag=0
with open('credentials.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
  
    for row in csv_reader:
      
        if(username == row[0] ):
            print(f'username found {row[0]}')
            flag=1
            break
       
    if(flag == 0):
        print("Incorrect username")
    else:
        password = input("Enter password : ")
        if(password == row[1]):
            print("password matched")
        else:
            print("wrong password")
            
       



