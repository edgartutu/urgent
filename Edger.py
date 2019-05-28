import sqlite3
import datetime

conn = sqlite3.connect("Employee.db")
c = conn.cursor()
conn.commit()

def employee_table():
    c.execute("CREATE TABLE IF NOT EXISTS Employee(ID INTEGER PRIMARY KEY,"
              "EmployeeID TEXT,StartDate TEXT,Seniority TEXT)")


employee_table()

def accural_monthly():
    a = 5
    b = 10
    c = 15
    d = 20
    e = 25

def tenure_years():
    one_two = 1
    two_four = 1.25
    four_plus = 1.5

def insert_employee(empid,startdate,seniority):
    c.execute("INSERT INTO Employee (EmployeeID,StartDate,Seniority) VALUES(?,?,?)",(empid,startdate,seniority))
    conn.commit()

def queary_points(empid):
    
    c.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(empid,))

    for row in c.fetchall():
        startdate = row[1]
        seniority = row[2]

        print(startdate,seniority)

def Calculate_points():
    list_=[]

    for i in employee_table.query.filter_by(EmployeeID=1):  #try to filter as its done in sqlite by the persons id
        dict_={"id":i.EmployeeID,'date':i.StartDate,'senior':i.Seniority}
        dict_.append(list_) #apend the disctionaries to a list

    date1_=datetime.datetime.strptime(list_[0]['date'], "%m/%d/%Y") # pick out the dates from the dictionary and strip them to normal
    date2_=datetime.datetime.strptime(list_[1]['date'], "%m/%d/%Y")
    date3_=datetime.datetime.strptime(list_[3]['date'], "%m/%d/%Y")
    date12_=date1_-date2_  # calc the difference of dates 
    date23_=date2_-date3_

    s1=list_[0]['senior']  # check the seniority before u do the computation please u can use your methods in all this parts 
    while True:
        s0=abs(date12_.days)
        s1=abs(date23_.days)

        P1= tenure_years.one_two *accural_monthly.a * (s0)/365 
        P2= tenure_years.two_four *accural_monthly.c * (s1)/365
        if s0<=730 :

            
        elif 730<s1<=1460:
            



            

        P2=accural_monthly.c * (s1)/365

        if P1<=

    



'''
 f
'''
def program():
    x = int(input("Enter \n 1 to insert Employee \n 2 to queary employee points: "))

    if x == 1:
        while True:
            y = input("Employee ID: ")
            z = input("Start Date: ")
            a = input("Seniority: ")

            insert_employee(y,z,a)

            if y or z or a == 'Exit':
                break
                program()

    elif x == 2:
        y = input("Employee ID: ")
        queary_points(y)

    else:
        print('Enter either 1 or 2')
        program()

program()
            

        
        


    
