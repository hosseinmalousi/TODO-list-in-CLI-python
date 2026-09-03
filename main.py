import os
import Asccii_art
import uuid
import datetime
import json

# where the tasks are saved on disk
file_path_undone = "undone_tasks.json"
file_path_done = "done_tasks.json"

def print_art():
    # prints the banner at the start of the program
    print()
    print(Asccii_art.art + "\n")

class Task:
    # one task = name + desc + date + done flag; the lists below are shared by ALL tasks (class level)

    undone_tasks=[]
    done_tasks = []
    # runs once when the file is imported: loads the saved tasks from json into the lists
    if os.path.exists(file_path_undone):
        with open(file_path_undone,"r") as f:
            data = json.load(f)
            for task in data :
                undone_tasks.append(task)
    if os.path.exists(file_path_done):
        with open(file_path_done,"r") as f:
                data = json.load(f)
                for task in data :
                    done_tasks.append(task)
    
    def __init__(self,task,desc="",date="nodate"):
        # builds a new task and puts it straight into the undone list
        self.uniq_code = str(uuid.uuid4())   # random id so every task is unique
        self.task = task
        self.date = date
        self.desc = desc
        self.done = False
        ### this line under must be changed i guess
        Task.undone_tasks.append({"uniq_code":self.uniq_code,"task":self.task,"desc":self.desc,"date":self.date , "done" : self.done})

        
    @staticmethod
    def showTime(date):
        today = datetime.date.today() 
        date = datetime.datetime.strptime(date,"%d/%m/%Y").date()
        
        if date == today:
            return "Today"
        elif (date - today) == datetime.timedelta(days=1):
            return "Tomorrow"
        elif (date - today) == datetime.timedelta(days=2):
            return "'The day after tomorrow'"
        else :
            return date
            
    
    @classmethod
    def list_tasks(cls):
        # prints every undone task with a number (1,2,3...) ; that number is what the user types later
        print("***************")
        print()
        ### show it as a string and sort them or with bullet points
        # it only effect on showing and the new ones also works
        if cls.undone_tasks :
            for i,task in enumerate(cls.undone_tasks,1):
                if task["done"] == False:
                    print(f"{i}. the task : {task["task"]}, is due to {cls.showTime(task["date"])}; descirption : '{task["desc"]}'")
            print()
        else :
            print("U have no task waiting for u ,go enjoy your day 🔥")
            print()
        print("***************")
    
    @classmethod
    def tick(cls):
        # marks a task as done : moves it from undone_tasks -> done_tasks
        # the while/try keeps asking until the user gives a valid number
        while True :
            try :
                option = int(input("which task are u done with :")) -1   # -1 because the list shows 1-based
                cls.undone_tasks[option]["done"] = True
                cls.done_tasks.append(cls.undone_tasks[option])
                cls.undone_tasks.pop(option)
            except IndexError :
                print("the number you have enterd is not in the tasks")
                continue
            except ValueError :
                print("Please insert a number")
                continue
            cls.write_to_file()
            print("The task has been ticked, good job")
            print(cls.done_tasks)
            break
                
    @classmethod
    def edit_task(cls):
        # lets the user change the name / date / description of an existing task
        # loops so you can edit more than one thing before going back to the menu
        while True:
            option = input("which task do you want to edit (insert the index) , (q for menu) : ")
            if option.lower() == "q":
                break
            elif option.isdigit():
                option = int(option)
                if option not in range(len(cls.undone_tasks)+1):
                    print("the index you have chosen,it does not exist ")
                    continue
            prop = int(input("which property do u want to edit\n 1. Task name\n2. Date\n3. Description \n : "))
            match prop:   # 1 = name , 2 = date , 3 = description
                case 1:
                    new_name = input("what's your new task name ? ")
                    cls.undone_tasks[option -1]["task"] = new_name
                case 2:
                    new_date =input("what's the new date (DD-MM-YYYY) (leave blank for no date)? ")
                    cls.undone_tasks[option - 1]["date"] = new_date
                case 3:
                    new_desc = input("what is the new decription ? ")
                    cls.undone_tasks[option-1]["desc"] = new_desc
            cls.write_to_file()
            if input("more edit ?\n(Y/N) : ").lower() != "y" :
                break
                     
    
    @classmethod
    def delete_task(cls):
        # removes one task by its index, or wipes the whole list if the user types A
        option = input("which task do you wanna delete (A for all) :")
        if option.isalpha() and option.upper() == "A" :
            cls.undone_tasks.clear()
        elif option.isnumeric() :
            option = int(option)
            try:
                cls.undone_tasks.pop(option -1)
            except IndexError :
                print("The index you have chosen is not in the tasks")
        else:
            print("Please choose a the index of the task or 'A' for deleting all the list ")
        cls.write_to_file()
    
    @classmethod
    def write_to_file(cls):
        # saves both lists back to the json files (call it after every change, else changes are lost)
        with open(file=file_path_undone,mode="w+" ) as file:
            json.dump(cls.undone_tasks,file,indent=4)
        
        with open(file=file_path_done,mode="w+") as f:
            json.dump(cls.done_tasks,f,indent=4)

def add_task():
    # asks the user name/date/desc , creates the Task object and saves it
    task_name=input("What do u wanna do champ ? 🎖️\n ")
    
    ### date should be formed correctly ### also the format and cooerct writing is really important
    date=input("when do u wanna do it (DD/MM/YYYY)? (leave blank for no date)\n")
    Task.showTime(date)
    if not date :
        date = "no date"    
    #     date = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    desc=input("is there any decription ? (enter to leave it blank) \n")
    Task(task_name,desc,date)
    Task.write_to_file()

def main():
    # the main menu loop : show date + tasks , ask what to do , repeat until "5"
    print_art()
    is_running = True
    while is_running:
        print(f"today is {datetime.date.today().strftime("%A")} {datetime.datetime.today().strftime("%H:%M:%S , %d/%m/%Y")} \n")
        
        Task.list_tasks()
        
        action = input("""1.tick a task \n2.add a task  \n3.delete a task \n4.edit a task \n5.quit the program\n\nplease add the index: """)
        
        if action.isdigit() :
            if Task.undone_tasks :
                match action:
                    case "1" :
                        Task.tick()
                    case "2":
                        ### make it a func and show the tasks more beutiful
                        add_task()
                    case "3":
                        Task.delete_task()
                    case "4":
                        Task.edit_task()
                    case "5":
                        break
            elif not Task.undone_tasks and action != "2" :
                print("the task list empty , please add a task first to continue")
                continue
            else :
                add_task()
        else :
            print("please insert a number")
    print()          

if __name__ == "__main__":
    # only runs main() when this file is started directly (not when imported)
    main()