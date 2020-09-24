import os
import datetime
from datetime import date

# Define a function which reuests the user to input a username.
# Checks if the username entered is in the "user.txt" file. If it is, then the
# user already exists and cannot be registered. If it is not, a password is
# requested.
# The user must also retype/confirm the password. If it matches with the original
# password, the username and pasword is written to the "user.txt" file and the
# user is registered.
def reg_user(new_username):

    while new_username in username_array:
        print()
        print("The user already exists, please select another username: ")
        new_username = input()
    else:
        print()
        new_password = input("Please enter the password here: ")

    print()
    confirm_new_password = input("Please confirm the password: ")

    while new_password != confirm_new_password:
        print()
        print("The passwords entered does not match, please try again: ")
        confirm_new_password = input()
    else:
        new_user_login = new_username + ", " + new_password
        f.seek(0, os.SEEK_END)
        f.write("\n" + new_user_login)
        print()
        print("{}, has been registered".format(new_username))

# Define a function which enables the user to create a new task.
# When the user chooses the option to create a new task, they have to provide
# the username of the assignee, the task title, the description and the due
# date.
# Firstly, the function checks if the assignee username is in the "user.txt" file,
# if it is not, than the user does not exist and the task cannot be created.
# If the user exists, a task title, description and due date is requested.
# The function also assignes the assigned date as the date the task was created and
# automatically sets the completed field to "No".
# Lastly the function writes the task to the "task.txt" file.
def add_task(task_username):

    while task_username not in username_array:
        print()
        print("The user does not exist, please select an existing user: ")
        task_username = input()

    else:
        print()
        print("Please enter the title of the task (do not use commas): ")
        task_title = input()

        print()
        print("Please enter a description of the task (do not use commas): ")
        task_descrip = input()

        print()
        print("Please enter the due date for the task (for example 10 Oct 2020): ")
        task_due_date = input()

        date_assigned = datetime.datetime.today()
        day = date_assigned.day
        month = date_assigned.strftime("%B")
        month = month[:3]
        year = date_assigned.year
        format_date_assign = ("{} {} {}".format(day, month, year))

        completed = "No"

        task_line = "{}, {}, {}, {}, {}, {}".format(task_username, task_title, task_descrip, format_date_assign, task_due_date, completed)

        g = open("tasks.txt", "r+")
        g.seek(0, os.SEEK_END)
        g.write("\n" + task_line)

        print("The task has been added")
# Define a function that allows the user to view all the tasks in an easy to read
# format.
# "task.txt" if opened in read only mode, every line is saved as an array value
# The function loops through every entry in the array and splits the different
# words (assignee name, title, description etc) and uses f-strings to display
# these parameters.
# This is then printed for the user to read.
def view_all(tasks_content):
    task_length = len(tasks_content)
    print()
    print("\t\t\t\t\t\t\t\tTASKS LIST: ")
    
    for m in range(0, task_length):
        print()
        print("Task Details: ")
        print("-"*150)
        task_line = tasks_content[m]
        task_line_split = task_line.split(", ")
        print()
        print("Task title:\t\t{}".format(task_line_split[1]))
        print("Task description:\t{}".format(task_line_split[2]))
        print("Responsible person:\t{}".format(task_line_split[0]))
        print("Date assigned:\t\t{}".format(task_line_split[3]))
        print("Due date:\t\t{}".format(task_line_split[4]))
        print("Completed:\t\t{}".format(task_line_split[5]))

        
    print()
    print("*"*150)
    print("\t\t\t\t\t\t\t\tEND OF TASKS LIST")
    print("*"*150)
    
# Define a function which writes a file that displays an overview of all the tasks.
# The function stores each task as an array entry. The number of tasks are
# calculated (as the length of the array).
# The function loops through each tasks and checks if the last value is Yes.
# If it is, the task is added to the completed tasks array. Otherwise it is added
# to the uncompleted tasks.
# The function then loops through the uncompleted tasks array and checks if the
# due date is earlier than the current date. If it is, the tasks is added to the
# overdue tasks array,
# The function then calculated the number of completed, uncompleted and overdue
# tasks.
# The percentage is calculated for each of these, by dividing the number by the
# total number of tasks and multiplying it by 100.
# These values are concatenated in strings and written to the "task_overview.txt"
# file in an easy to read format.
def gen_task_overview(tasks_content):
    tasks_content_length = len(tasks_content)
    completed_tasks_array = []
    uncompleted_tasks_array = []
    overdue_tasks_array = []
    for task in range(0, tasks_content_length):
        tasks_eval = tasks_content[task]
        tasks_eval_split = tasks_eval.split(", ")
        
        if tasks_eval_split[5] == "Yes\n":
            completed_tasks_array.append(tasks_eval)
        else:
            uncompleted_tasks_array.append(tasks_eval)

    num_uncompleted_tasks = len(uncompleted_tasks_array)
    num_completed_tasks = len(completed_tasks_array)
    
    for uncom_task in range(0, num_uncompleted_tasks):
        uncom_tasks_eval = uncompleted_tasks_array[uncom_task]
        uncom_tasks_eval_split = uncom_tasks_eval.split(", ")
        due_date = uncom_tasks_eval_split[4]
        due_date_day = int(due_date[:3])
        due_date_month = due_date[3:6]
        due_date_month = due_date_month.lower()
        due_date_year = int(due_date[7:])
        today = date.today()
        today_string = str(today)
        today_day = int(today_string[8:])
        today_month = int(today_string[6:7])
        today_year = int(today_string[:4])

        month_comparison_dir = {"jan":"1",
                                "feb":"2",
                                "mar":"3",
                                "apr":"4",
                                "may":"5",
                                "jun":"6",
                                "jul":"7",
                                "aug":"8",
                                "sep":"9",
                                "oct":"10",
                                "nov":"11",
                                "dec":"12"}
        
        due_date_month_val = int(month_comparison_dir[due_date_month])

        if (today_year > due_date_year):
            overdue_tasks_array.append(uncom_tasks_eval)

        elif (today_year == due_date_year):
            
            if (today_month == due_date_month_val):
                if(today_day > due_date_day):
                    overdue_tasks_array.append(uncom_tasks_eval)

            elif (today_month > due_date_month_val):
                overdue_tasks_array.append(uncom_tasks_eval)


    num_overdue_tasks = len(overdue_tasks_array)
    per_incomplete_tasks = (num_uncompleted_tasks/tasks_content_length)*100
    per_incomplete_tasks = round(per_incomplete_tasks, 1)
    per_overdue_tasks = (num_overdue_tasks/tasks_content_length)*100
    per_overdue_tasks = round(per_overdue_tasks, 1)

    

    disp_string_01 = "The total number of tasks that have been generated:\t{}".format(tasks_content_length)

    disp_string_02 = "The total number of completed tasks:\t\t\t{}".format(num_completed_tasks)

    disp_string_03 = "The total number of uncompleted tasks:\t\t\t{}".format(num_uncompleted_tasks)

    disp_string_04 = "The total number of uncompleted tasks that are overdue:\t{}".format(num_overdue_tasks)

    disp_string_05 = "The percentage of tasks that are incomplete:\t\t{}".format(per_incomplete_tasks)

    disp_string_06 = "The percentage of tasks that are overdue: \t\t{}".format(per_overdue_tasks)

    
    gg = open("task_overview.txt", "w")
    gg.write(disp_string_01)
    gg.close

    hh = open("task_overview.txt", "a")
    hh.seek(0,os.SEEK_END)
    hh.write("\n"+ disp_string_02 +"\n" + disp_string_03 + "\n" + disp_string_04 + "\n" + disp_string_05 + "\n" + disp_string_06)

# Define a function that writes a user_overview text file.
# The function loops through the "user.txt" file adn calcualted the number of
# users. The same is done for the "task.txt" file.
# For every user in the "user.txt" file the function loops through the "task.txt"
# file and checks if the task is assigned to the user. If it is, that task is added
# to the user_task array.
# The function then loops through each of the user_task entries and checks if
# the task has been completed. If true, the task is added to the user_completed_task
# array, otherwise it is added to the user_incomplete_task array.
# The function then loops through each incomplete tasks and check if the due date
# is earlier than the current date, the task is added to the overdue_tasks_array.
# The number of tasks assigned to the user, the number of completed, incompleted tasks
# and overdue tasks are determined.
# The percentage of these values is determined by didviding them through the total
# number of tasks.
# The values are concatenated in strings and written to the "user_overview.txt" file
# in an easy to read format.
def gen_user_overview(user_content, tasks_content):
    num_users = len(user_content)
    tasks_lookin_array = []


    num_tasks = len(tasks_content)

    disp_string_06 = "The total number of users are: {}".format(num_users)
    disp_string_18 = "The total number of tasks are: {}".format(num_tasks)
    disp_string_19 = "Summary Per User"

    hh = open("user_overview.txt","w")
    hh.write(disp_string_06+"\n"+disp_string_18+"\n"+"\n"+disp_string_19+"\n"+"\n")
    hh.close()

    for user in range(0, num_users):
        user_eval = user_content[user]
        user_eval_split = user_eval.split(", ")
        user_username = user_eval_split[0]
        username_array.append(user_username)


    for task in range(0, num_tasks):
        task_lookin = tasks_content[task]
        task_lookin_split = task_lookin.split(", ")
        task_assignee_lookin = task_lookin_split[0]
        tasks_lookin_array.append(task_assignee_lookin)


    for users in range(0, num_users):
        user_task = []
        user_completed_task = []
        user_incomplete_task = []
        overdue_tasks_array = []
        lookfor_user = username_array[users]
        if lookfor_user in tasks_lookin_array:
            disp_string_16 = "-"*80
            disp_string_07 = "{}".format(lookfor_user)
            ii = open("user_overview.txt", "a")
            ii.seek(0,os.SEEK_END)
            ii.write(disp_string_16+"\n"+ disp_string_07+"\n")
            ii.close()
    
            for tasks in range(0, num_tasks):
                comparison_value = tasks_lookin_array[tasks]
                if comparison_value == lookfor_user:
                    user_task.append(tasks_content[tasks])
                    disp_string_08 = tasks_content[tasks]
                    disp_string_08 = disp_string_08.replace("\n","")
                    split_disp_string_08 = disp_string_08.split(", ")
                    lenght_split_disp_string_08 = len(split_disp_string_08)
            
            
                    if split_disp_string_08[5]== "Yes":
                        user_completed_task.append(tasks_content[tasks])
                    else:
                        user_incomplete_task.append(tasks_content[tasks])
         
        num_user_tasks_incomplete = len(user_incomplete_task)
        
        
        for uncom_task in range(0, num_user_tasks_incomplete):
            uncom_tasks_eval = user_incomplete_task[uncom_task]
            uncom_tasks_eval_split = uncom_tasks_eval.split(", ")
            due_date = uncom_tasks_eval_split[4]
            due_date_day = int(due_date[:3])
            due_date_month = due_date[3:6]
            due_date_month = due_date_month.lower()
            due_date_year = int(due_date[7:])
            today = date.today()
            today_string = str(today)
            today_day = int(today_string[8:])
            today_month = int(today_string[6:7])
            today_year = int(today_string[:4])

            month_comparison_dir = {"jan":"1",
                                    "feb":"2",
                                    "mar":"3",
                                    "apr":"4",
                                    "may":"5",
                                    "jun":"6",
                                    "jul":"7",
                                    "aug":"8",
                                    "sep":"9",
                                    "oct":"10",
                                    "nov":"11",
                                    "dec":"12"}
        
            due_date_month_val = int(month_comparison_dir[due_date_month])

            if (today_year > due_date_year):
                overdue_tasks_array.append(uncom_tasks_eval)

            elif (today_year == due_date_year):
                if (today_month == due_date_month_val):
                    if(today_day > due_date_day):
                        overdue_tasks_array.append(uncom_tasks_eval)
                elif (today_month > due_date_month_val):
                    overdue_tasks_array.append(uncom_tasks_eval)
                      
        num_user_tasks = len(user_task)

        if num_user_tasks != 0:            
            per_user_tasks = round((num_user_tasks/num_tasks)*100,1)
            num_user_task_completed = len(user_completed_task)
            per_tasks_completed = round((num_user_task_completed/num_user_tasks)*100,1)
            per_tasks_incomplete = round((num_user_tasks_incomplete/num_user_tasks)*100,1)
            num_incomplete_tasks = len(overdue_tasks_array)
            per_overdue_tasks = round((num_incomplete_tasks/num_user_tasks)*100,1)
        
    
            disp_string_11 = "Number of tasks assigned:\t\t\t\t{}".format(num_user_tasks)
            disp_string_12 = "Percentage of total tasks assigned to the user:\t\t{}".format(per_user_tasks)
            disp_string_13 = "Percentage of tasks assigned that are completed:\t{}".format(per_tasks_completed)
            disp_string_14 = "Percentage of tasks still to be completed:\t\t{}".format(per_tasks_incomplete)
            disp_string_15 = "Percentage of tasks assigned to user, overdue:\t\t{}".format(per_overdue_tasks)

            vv = open("user_overview.txt", "a")
            vv.seek(0, os.SEEK_END)
            vv.write("\n"+disp_string_11+"\n"+disp_string_12+"\n"+disp_string_13+"\n"+disp_string_14 +"\n"+disp_string_15+"\n")
            vv.close()

# Define a function that only displays the users tasks, gives them the choice
# to edit the task or go back to the main menu.
# The function loops through the "task.txt" file and checks if the task is assigned
# to the user which is logged in. If true, the task is added to the "my_tasks_array".
# The function then loops through this array and assigns a unigue number to it.
# The user can then choose which number to edit. The input number is used to
# edit that array index.
# If the user chooses to go back to the main menu, it is displayed and the depending
# on the choice of the user, the above functions are called.
def view_mine(login_username):
    l = open("tasks.txt", "r+")
    tasks_content = l.readlines()
    task_length = len(tasks_content)
    my_tasks_array = []
    my_task_num_array = []
    my_task_index_array = []
    my_task_num = 0

    l.close()
    print()
    print("Your tasks are:")
    print()
    print("-"*80)
    
    for m in range(0,task_length):
        task_details = tasks_content[m]
        task_details_split = task_details.split(", ")
        user_assigned = task_details_split[0]
        
    
        if user_assigned == login_username:
            line_number_of_task = tasks_content.index(task_details)
            my_tasks_array.append(task_details)
            my_task_num +=1
            my_task_num_array.append(my_task_num)
            my_task_index_array.append(line_number_of_task)

            print()
            print("Task Number:\t\t{}".format(my_task_num))
            print("Taks Title:\t\t{}".format(task_details_split[1]))

    print("-"*80)       
    print()   
    print("""Please enter the task number you want to view or edit, otherwise enter -1
to go back to the main menu: """)
    my_tasks_option = int(input())
    

    if my_tasks_option in my_task_num_array:
        index_lookfor = my_task_num_array.index(my_tasks_option)
        actual_index = my_task_index_array[index_lookfor]
        print()
        print("""Please select what operation you would like to perform:
1. Mark tasks as complete
2. Change asignee
3. Change due date
4. Exit""")
        print()
        user_operation = int(input("Please enter your option here: "))


        line_to_change = tasks_content[actual_index]
        split_line_to_change = line_to_change.split(", ")

        if user_operation == 1:
            if split_line_to_change[5] == "Yes\n":
                print()
                print("The task is already complete.")
            else:
                split_line_to_change[5] = "Yes\n"
                updated_line = ", ".join(split_line_to_change)
                tasks_content[actual_index] = updated_line
                print()
                print("The task is complete.")
        

        elif user_operation == 2:
            if split_line_to_change[5] == "Yes\n":
                print()
                print("The task is complete and can no longer be edited.")
            else:
                print()
                split_line_to_change[0] = input("Please enter the username: ")
                while split_line_to_change[0] not in username_array:
                    print()
                    print("The user does not exist, please select a valid user.")
                    split_line_to_change[0] = input("Please enter the username: ")
                updated_line = ", ".join(split_line_to_change)
                tasks_content[actual_index] = updated_line
                print()
                print("The asignee has been changed.")

        elif user_operation == 3:
            if split_line_to_change[5] == "Yes\n":
                print()
                print("The task is complete and can no longer be edited.")
            else:
                print()
                split_line_to_change[4] = input("Please enter the new due date (for example 10 Oct 2020): ")
                updated_line = ", ".join(split_line_to_change)
                tasks_content[actual_index] = updated_line
                print()
                print("The due date has been changed.")

        else:
            print("Exiting the program")

        s = open("tasks.txt", "w+")
    
        for r in range(0, task_length):
            if r == 0:
                s.seek(0)
                s.write(tasks_content[r])
            else:
               s.seek(0,os.SEEK_END)
               s.write(tasks_content[r])
               
        s.close()
   

    else:
        print()
        if login_username == "admin":
            print("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""")

        else:
            print("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit""")
        user_selection = input("Please enter option here: ").lower()

        while login_username != "admin" and user_selection == "r":
            print()
            print("Unfortunately, you do not have access to this function.")
            user_selection = input("Please select another option here: ")

        while login_username != "admin" and user_selection == "gr":
            print()
            print("Unfortunately, you do not have access to this function.")
            user_selection = input("Please select another option here: ")

        while login_username != "admin" and user_selection == "ds":
            print()
            print("Unfortunately, you do not have access to this function.")
            user_selection = input("Please select another option here: ")

        while user_selection != "r" and user_selection != "a" and user_selection != "va" and user_selection != "vm" and user_selection != "e" and user_selection != "ds" and user_selection != "gr":
            print()
            print("Selection invalid, please select a valid option.")
            user_selection = input("Please enter option here: ").lower()
            
        if user_selection == "r":
            print()
            new_username = input("Please enter the username: ")
            register_new_user = reg_user(new_username)

        if user_selection == "a":
            print()
            print("Please enter the username of the assignee: ")
            task_username = input()
            create_new_task = add_task(task_username)

        if user_selection == "va":
            h = open("tasks.txt", "r")
            tasks_content = h.readlines()
            view_all_tasks = view_all(tasks_content)
            h.close()

        if user_selection == "gr":
            ff = open("tasks.txt", "r")
            tasks_content = ff.readlines()
            generate_tasks_report = gen_task_overview(tasks_content)
            jj = open("tasks.txt", "r")
            tasks_content = jj.readlines()
            generate_user_overview_report = gen_user_overview(user_content, tasks_content)
            ff.close()
            jj.close()

    
        if user_selection == "vm":
            view_my_tasks_call = view_mine(login_username)

        if user_selection == "e":
            print()
            print("Closing the program...")
            print("*"*80)
    
        
# Requests the user to input a username.
print("Please enter your username: ")
login_username = input()

# Open the users text file.
f = open("user.txt","r+")

# Split the usernames and passwords into different array entries.
user_content = f.readlines()

# Determine the amount of users.
num_users = len(user_content)

# Create empty arrays for the usernames, passwords and final formatted password.
username_array = []
password_array = []
fin_password_array = []

# Loop through data content array and split the username and password.

for i in range(0, num_users):
    user_login = user_content[i]
    user_login_split = user_login.split(", ")
    username_array.append(user_login_split[0])
    password_array.append(user_login_split[1])

# Remove the \n from the password and save it back to a new formatted password
# array.
for k in range(0, len(password_array)):
    new_pw_values = password_array[k].replace("\n","")
    fin_password_array.append(new_pw_values)

# Check if the username provided is in the list of users. While it is not, provide
# the option to try again.
while login_username not in username_array:
    print()
    print("The user does not exist, please enter a valid username: ")
    login_username = input()

# If the username entered is in text file, ask for the user to input their pass-
# word.
else:
    print()
    array_value = username_array.index(login_username)
    print("Please enter your password: ")
    login_password = input()

# Check if the password entered agrees with the password associated with the
# specific username. If it doesn't, provide the user the option to try again.
while login_password != fin_password_array[array_value]:
    print()
    print("Incorrect password, please try again:  ")
    login_password = input()

# If the password entered is the right one allow access to the program.
# Two different menus are displayed, one for admin and one for all other users.
# If the user logging in is admin the first menu gets displayed, otherwise, the
# second menu is displayed.
# The same code is used above in the view_my function, which runs when the user
# chooses the option to go back to the main menu.
else:
    print()
    if login_username == "admin":
        print("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit""")
    else:
        print("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit""")

    print()    
    user_selection = input("Please enter option here: ").lower()

# Prevents non-admin users from creating new users.   
while login_username != "admin" and user_selection == "r":
    print()
    print("Unfortunately, you do not have access to this function.")
    user_selection = input("Please select another option here: ")

# Prevents non-admin users from generating statisictacl reports.
while login_username != "admin" and user_selection == "gr":
    print()
    print("Unfortunately, you do not have access to this function.")
    user_selection = input("Please select another option here: ")

# Prevents non-admin users from displaying statistical reports.
while login_username != "admin" and user_selection == "ds":
    print()
    print("Unfortunately, you do not have access to this function.")
    user_selection = input("Please select another option here: ")

# Checks if the user entered a valid option, if not an error message is displayed.
while user_selection != "r" and user_selection != "a" and user_selection != "va" and user_selection != "vm" and user_selection != "e" and user_selection != "ds" and user_selection != "gr":
    print()
    print("Selection invalid, please select a valid option.")
    user_selection = input("Please enter option here: ").lower()
    
# Checks if the user wants to view all tasks.
# If true, the view_all function is called.
if user_selection == "va":
    h = open("tasks.txt", "r")
    tasks_content = h.readlines()
    view_all_tasks = view_all(tasks_content)

# Checks if the user wants to view their tasks.
# If true, it calls the view_tasks.
if user_selection == "vm":
    view_my_tasks_call = view_mine(login_username)

# Checks if the user wants to regiser a new user.
# If true, calls the reg_user function. 
if user_selection == "r":
    print()
    new_username = input("Please enter the username here: ")
    create_new_user = reg_user(new_username)
    
# Checks if the user wants to add a task.
# If true, it calls the add_task function.
if user_selection == "a":
    print()
    print("Please enter the username of the assignee: ")
    task_username = input()
    create_new_task = add_task(task_username)
    
# Checks if the user wants to generate statistical reports.
# If true, it calls the ger_user_overview and gen_user_overview functions.
if user_selection == "gr":
    ff = open("tasks.txt", "r")
    tasks_content = ff.readlines()
    generate_tasks_report = gen_task_overview(tasks_content)
    jj = open("tasks.txt", "r")
    tasks_content = jj.readlines()
    generate_user_overview_report = gen_user_overview(user_content, tasks_content)
    ff.close()
    jj.close()
    
# Checks if the user wants to display statistical reports.
# If true, it calls the gen_user_overview and gen_user_overview function to generate the reports.
# It then reads the reports and prints out the result in an easy to read format.
if user_selection == "ds":
    ff = open("tasks.txt", "r")
    tasks_content = ff.readlines()
    generate_tasks_report = gen_task_overview(tasks_content)
    jj = open("tasks.txt", "r")
    tasks_content = jj.readlines()
    generate_user_overview_report = gen_user_overview(user_content, tasks_content)
    ff.close()
    jj.close()

    ll = open("task_overview.txt", "r")
    task_overview_content = ll.read()
    print()
    print("*"*80)
    print("Statistics For Task Overview: ")
    print()
    print(task_overview_content)
    ll.close()
    print("*"*80)

    mm = open("user_overview.txt", "r")
    user_overview_content = mm.read()
    print()
    print()
    print("*"*80)
    print("Statistics For User Overview: ")
    print()
    print(user_overview_content)
    mm.close()
    print("*"*80)
    
# checks if the user wants to exit the program.
# If true, display an exit message.
if user_selection == "e":
    print()
    print("Closing the program...")
    print("*"*80)

# Close the user.txt file.
f.close()     
