import pymongo
import re
from pymongo import errors
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
mydb = client["employee"]
mycol = mydb["Users"]
print("Enter employee details")

def insert():
    try:
        employeeId = input('Enter Employee id :')
        val1 = int(employeeId)
        employeeName = input('Enter Name :')
        if not re.match("^[A-z]*$", employeeName):
            print("Only characters are allowed")
            exit()
        employeeAge = input('Enter age :')
        val2 = int(employeeAge)
        employeeCountry = input('Enter Country :')
        if not re.match("^[A-z]*$", employeeCountry):
            print("Only characters are allowed")
            exit()

        mydb.mycol.insert_one(
            {
                "id": val1,
                "name":employeeName,
                "age":val2,
                "country":employeeCountry
        })
        print("\nData inserted successfully\n")
    except pymongo.errors.PyMongoError as e:
        print(str(e))

def read():
    try:
        empCol = mydb.mycol.find()
        print("\n All data from EmployeeData Database \n")
        for emp in empCol:
            print(emp)

    except Exception as e:
        print(str(e))

def update():
    try:
        criteria = input('\nEnter id to update\n')
        val3 = int(criteria)
        name = input('\nEnter name to update\n')
        if not re.match("^[A-z]*$", name):
            print("Only characters are allowed")
            exit()
        age = input('\nEnter age to update\n')
        val4 = int(age)
        country = input('\nEnter country to update\n')
        if not re.match("^[A-z]*$", country):
            print("Only characters are allowed")
            exit()

        mydb.mycol.update_one(
            {"id": val3},
            {
                "$set": {
                    "name":name,
                    "age":val4,
                    "country":country
                }
            }
        )
        print("\nData updated successfully\n")    
    
    except Exception as e:
        print(str(e))

def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        val5 = int(criteria)
        mydb.mycol.delete_one({"id":val5})
        print("\nData deleted\n")
    except Exception as e:
        print(str(e))

def main_fun():
    while(1):
        choice = input("Select 1 to insert, 2 to display, 3 to update, 4 to delete\n")
        print(choice)   
        if choice == '1':
            insert()
        elif choice == '2':
            read()
        elif choice == '3':
            update()
        elif choice == '4':
            delete()
        else:
            print("\n INVALID CHOICE \n")
            quit()

main_fun()