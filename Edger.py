import sqlite3
import datetime

conn = sqlite3.connect("Employee.db")
c = conn.cursor()
conn.commit()

def employee_table():
    c.execute("CREATE TABLE IF NOT EXISTS Employee(ID INTEGER PRIMARY KEY,"
              "EmployeeID TEXT,StartDate TEXT,Seniority TEXT)")


employee_table()


accural = {'A':5,'B':10,'C':15,'D':20,'E':25}
tenure = {'one_two':1,'two_four':1.25,'four_plus':1.5}

def insert_employee(empid,startdate,seniority):
    c.execute("INSERT INTO Employee (EmployeeID,StartDate,Seniority) VALUES(?,?,?)",(empid,startdate,seniority))
    conn.commit()

'''
You will need to remove the print statments and check how i have calculated the points but
otherwise the code is done.
Check for any redundant code and remove so as to make the code neat
'''

def queary_points(empid):
    start = []
    sen = []
    datelist = []
    year = []
    
    c.execute("SELECT * FROM Employee WHERE EmployeeID = ?",(empid,))

    for row in c.fetchall():
        
        startdate = row[2]
        seniority = row[3]

        start.append(startdate)
        sen.append(seniority)

    print(start)
    print(sen)
    count = 0
    count1 = 0
    while count<len(start):
        date = datetime.datetime.strptime(start[count],"%Y/%m/%d")
        period = datetime.datetime.today().year-date.year
        datelist.append(period)
        year.append(date.year)
        count+=1
    print(year)
    print(datelist)

    while count1<len(year):
        x = datelist[count1]
        y = sen[count1]
        
        if x >= 1 & x <= 2:
            w = tenure.get('one_two')

            if y == 'A':
                q = accural.get('A')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'B':
                q = accural.get('B')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'C':
                q = accural.get('C')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                
            elif y == 'D':
                q = accural.get('D')
                points = w*q
                print('For '+str([count1])+' you have '+str(points)+ ' points')

            elif y == 'E':
                q = accural.get('E')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            else:
                print('Error')

        elif x >= 2 & x <= 4:
            w = tenure.get('two_four')

            if y == 'A':
                q = accural.get('A')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'B':
                q = accural.get('B')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'C':
                q = accural.get('C')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                
            elif y == 'D':
                q = accural.get('D')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'E':
                q = accural.get('E')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            else:
                print('Error')

        elif x > 4:
            w = tenure.get('four_plus')

            if y == 'A':
                q = accural.get('A')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'B':
                q = accural.get('B')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'C':
                q = accural.get('C')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')
                
            elif y == 'D':
                q = accural.get('D')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            elif y == 'E':
                q = accural.get('E')
                points = w*q
                print('For '+str(start[count1])+' you have '+str(points)+ ' points')

            else:
                print('Error')

        else:
            print('Out of range')

        count1+=1

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
            

        
        


    
