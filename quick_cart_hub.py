import mysql.connector
from conn_db import Database
from validate import validation
from query_module import QueryModule
# from login_sys import LoginSystem

print("\n= ✕ = = ✕ = = ✕ = = ✕ = = ✕ = = ✕ = = ✕ =")
print("✕ \t\t\t\t\t✕ ")
print("||\tWEL COME TO QUICK CART HUB\t||")
print("✕ \t\t\t\t\t✕ ")
print("= ✕ = = ✕ = = ✕ = = ✕ = = ✕ = = ✕ = = ✕ = \n")

class Main:
    
    def __init__(self):
        pass        
    
    def admin_signup(self):
        user_status = False
        user_id = input("Enter your user id \t\t: ")
        admin_name = input("Enter your name \t\t: ")
        admin_dob = input("Enter your date of birth (dd/mm/yy): ")
        validation.validate_dob(admin_dob)
        admin_pass = input("Enter your password \t\t: ")
        admin_cpass = input("Enter your confirm password \t: ")
        admin_city = input("Enter your city name \t\t: ").upper
        print("Gender :  1 | male \n \t  2 | female")
        admin_gender = int(input())
        admin_job = input("Enter your joining date \t: ")
        user_status = True

        user_val = (user_id, admin_name, admin_pass, admin_gender ,admin_dob , admin_city, admin_job,user_status)
        QueryModule.insert_table('user_table',user_val)
    
        if validation.valid_name(admin_name):
            if validation.valid_name(user_id):
                if QueryModule.check_admin_exists(user_id):
                    print("Admin already exists. Please try a different user id.")
                    main.admin_signup()
                    return user_id
                else :
                    pass_val = validation.pass_valid(admin_pass,admin_cpass)
                if pass_val != True:
                    user_val = (user_id, admin_name, admin_pass, admin_gender ,admin_dob , admin_city, admin_job,user_status)
                    QueryModule.insert_table('user_table',user_val)
                return user_status
    
    def user_signup(self):
        user_status = False
        user_id = input("Enter your user id \t\t: ")
        user_name = input("Enter your name \t\t: ")
        user_dob = input("Enter your date of birth \t: ")
        user_pass = input("Enter your password \t\t: ")
        user_cpass = input("Enter your confirm password \t: ")
        user_city = input("Enter your city name \t\t: ").upper
        print("Gender :  1 | male \n \t  2 | female")
        user_gender = int(input())
        user_job = input("Enter your joining date \t: ")  

        if validation.valid_name(user_name):
            if validation.valid_name(user_id):
                if QueryModule.check_admin_exists(user_id):
                    print("User already exists. Please try a different user id.")
                    main.admin_signup()
                    return user_id
                else :
                    pass_val = validation.pass_valid(user_pass,user_cpass)
                if pass_val:
                    user_val = (user_id, user_name, user_pass, user_gender ,user_dob , user_city, user_job,user_status)
                    QueryModule.insert_table('user_table',user_val)
                return user_status        
        user_status = False
        return user_status

    def admin_login(self):
        login_admin = False
        admin_name = input("Your name : (ADMIN)")
        user_id = input("Enter your user id \t\t: ")
        login_pass = input("Enter your password \t\t: ")

        cols = (user_id,login_pass,password)
        table_name = user_table
        condition = f'user_id="{user_id}"'
        if QueryModule.log_varify(cols,table_name,condition):
            main.user_login()
        elif user_status != True:
            print("No admin found with this id")            
            main.user_login()
        elif validation.pass_valid(login_pass,password):
            main.user_login()
        else:
            print(f"Admin log in with user id {user_id} is done")
            login_user = True
        return user_name

    def user_login(self):
        login_user = False
        user_name = input("Your name : (user)")
        user_id = input("Enter your user id \t\t: ")
        login_pass = input("Enter your password \t\t: ")
        # user_status = True
        cols = (user_id,login_pass,password)
        table_name = user_table
        condition = f'user_id="{user_id}"'
        if QueryModule.log_varify(cols,table_name,condition):
            print("No user id found")            
            main.user_login()
        elif user_status != False:
            print("No user found with this id")            
            main.user_login()
        elif login_pass != password:
            main.user_login()
        else:
            print(f"User log in with user id {user_id} is done")
            login_user = True
        return user_name
    
    def choice_login(self):
        print("1 for log in as admin")
        print("2 for log in as user")
        # print("5 for ")
        choice = int(input("You want to ... "))
    
        while True:
            while choice > 2:
                print("Invalide number you entered.")
                print("Please enter valid number as per given : ")
                choice = int(input("You want to ... "))
                break
            if choice == 1:
                main.admin_login()
                break
            elif choice == 2:
                # if user_status == False:
                main.user_login()
                break

    def choice_signup(self):
        print("1 for sign up as admin")
        print("2 for log in as user")
        # print("5 for ")
        choice = int(input("You want to ... "))
    
        while True:
            while choice > 2:
                print("Invalide number you entered.")
                print("Please enter valid number as per given : ")
                choice = int(input("You want to ... "))
                break
            if choice == 1:
                main.admin_signup()
                break
            elif choice == 2:
                test = main.user_signup()
                print(test)
                break
    
    def choice(self):
        print("1 for sign up")
        print("2 for log in")
        # print("5 for ")
        choice = int(input("You want to ... "))

        while True:
            while choice > 2:
                print("Invalide number you entered.")
                print("Please enter valid number as per given : ")
                choice = int(input("You want to ... "))
                break
            if choice == 1:
                main.choice_signup()
                break
            elif choice == 2:
                main.choice_login()
                break

db = Database(user = "root",
    password = "newPass@123",
    host = "localhost",
    dbname = "quick_cart_hub")

main = Main()
main.choice()