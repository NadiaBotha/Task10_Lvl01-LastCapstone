# Task10_Lvl01-LastCapstone

The program enables task management, where new users can be added to use the program. Tasks can be created, tracked and assigned to existing users. The program also keeps track of completed, uncompleted and overdue tasks.

## Functions
The program stores the existing users in the user.txt file and all tasks that have generated in tasks.txt file. 

The program 7 main functions:
- Register a new user
- Add a task
- View all tasks
- View my tasks
- Generate reports
- Generate statistics
- Exit

### Register a new user
This functionality is only available to the admin user. If the user logs in with the admin username and password, and he/she selects the option to register a new user, a username and password is requested for the new user. If the username entered does not exist yet, meaning it is not a duplicate, the username and password is written to the user.txt file. This user is now able to login to the program. 

### Add a task
Any user can create/add a new task. If this option is selected by the user, the user needs to provide the task assignee, a title and description for the task as well as the due date. 
The task is then written to the tasks.txt file, with the date the task was assigned set as the date the task was created. The task is also created with the status set as incomplete.

### View all tasks
Any user can view all tasks. When this option is selected, all the tasks in the tasks.txt file is displayed in an easy to read format.

### View my tasks
Any user can view my tasks. If this option is selected, all the tasks assigned to the username currently logged is displayed in an easy to read format, with each task assigned a number. The user has the option to select a specific number to see more details about the task, exit to the main menu or to edit the task. If the user select the option to edit the task, they can change the status of the task to complete, or they can change the assignee/due date. This updated information is then written back to the tasks.txt file.

### Generate reports
This functionality is only available to the admin user.
When this option is selected, two text files, task_overview.txt and user_overview.txt is created.

The task_overview.txt displays:
- The total number of tasks that have been generated. 
- Total number of completed and uncompleted tasks.
- Total number of tasks that are uncompleted tasks that are overdue.
- The percentage of tasks that are uncomplete and overdue.

The user_overview.txt, displays:
- The number of users generated. 
- Total number of tasks generated, 
- Total number of tasks assigned to each user.
- The percentage that of tasks assigned to each user.
- The percentage that have been completed for each user.
- The percentage that must still be completed for each user.
- The percentage of uncompleted tasks for each user.
- The percentage of uncompleted tasks that are overdue for each user.

### Generate statistics
This option is only available to the admin user. When it is selected, it displays the information from the above mentioned task_overview.txt and user_overview.txt files. If the generate reports option has not been selected and the reports have not been generated, this is done first and then the information is displayed.

## Use
This program is useful for small businesses to track multiple tasks that are completed by different people. It is also useful for resource management as the statistics option can indicate if a person is overloaded. It can alse be used to track efficiency as it tracks tasks that are incomplete and overdue.

## Contributors
Contributors include Nadia Botha and HyperionDev. 

Please send an email to nadiamarais@live.co.za regarding any issues. Provide include a brief description and screenshot of the issue in the email, with Task Manager as the email subject. 

## Installing and running the program
Install Python 3.7 or a later version by clicking [here](https://www.python.org/downloads/).

Download the files from the Github repository. Ensure that all the text files and the task_manager.py is saved in the same folder. 

To remove existing users and tasks, in order to start with a clean program, the follwoing steps need to be carried out:

- Delete all the users, except the admin user, which is the user in the first line of the user.txt file.

![](Images/Users.PNG)

- Clear the tasks.txt file.

![](Images/Tasks.PNG)


Open Python IDE, IDLE, from the start menu. In IDLE, select file, open, and open the task_manager.py file. 

Select Run from the top bar, Run the Module, and follow the instructions displayed.




