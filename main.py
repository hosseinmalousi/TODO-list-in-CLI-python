import os
import Asccii_art
import uuid
import datetime
import json

file_path = "tasks.json"

def print_art():
    print()
    print(Asccii_art.art + "\n")

class Task:
    
    undone_tasks=[]
    done_tasks = []
    with open(file_path,"r") as f:
        data = json.load(f)
        for task in data :
            undone_tasks.append(task)
    
    def __init__(self,task,desc="",date="nodate"):
        self.uniq_code = str(uuid.uuid4())
        self.task = task
        self.date = date
        self.desc = desc
        self.done = False
        ### this line under must be changed i guess
        Task.undone_tasks.append({"uniq_code":self.uniq_code,"task":self.task,"desc":self.desc,"date":self.date , "done" : self.done})

        
    @classmethod
    def list_tasks(cls):
        print("***************")
        print()
        ### show it as a string and sort them or with bullet points
        # it only effect on showing and the new ones also works 
        if cls.undone_tasks :
            for i,task in enumerate(cls.undone_tasks,1):
                if task["done"] == False:
                    print(f"{i}. the task : {task["task"]}, is due to {task["date"]}; descirption : '{task["desc"]}'")
            print()
        else :
            print("U have no task waiting for u ,go enjoy your day 🔥")
            print()
        print("***************")
    
    @classmethod
    def done(cls):
        while True :
            try :
                option = int(input("which task are u done with :")) -1
                cls.undone_tasks[option]["done"] = True
                cls.done_tasks.append(cls.undone_tasks[option])
                cls.undone_tasks.pop(option)
            except IndexError :
                print("the number you have enterd is not in the tasks")
                continue
            except ValueError :
                print("Please insert a number")
                continue
            print("The task has been ticked, good job")
            print(cls.done_tasks)
            break
                
            
            
    
    @classmethod
    def delete_task(cls):
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
        with open(file=file_path,mode="w+" ) as file:
            json.dump(cls.undone_tasks,file,indent=4)

def add_task():
    task_name=input("What do u wanna do champ ? 🎖️\n ")
    
    ### date should be formed correctly ### also the format and cooerct writing is really important
    date=input("when do u wanna do it (DD-MM-YYYY)? (leave blank for no date)\n")
    if date :
        date = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    else :
        date = "no date"
    desc=input("is there any decription ? (enter to leave it blank) \n")
    Task(task_name,desc,date)
    Task.write_to_file()

def main():
    print_art()
    is_running = True
    while is_running:
        print(f"today is {datetime.date.today().strftime("%A")} {datetime.date.today().strftime("%d:%m:%Y")}")
        
        Task.list_tasks()
        
        action = input("""1.tick a task \n2.add a task  \n3.delete a task \n4.edit a task \n5.quit the program\n\nplease add the index: """)
        
        match action:
            case "1" :
                Task.done()
            case "2":
                ### make it a func and show the tasks more beutiful
                add_task()
            case "3":
                Task.delete_task()
            case "4":
                pass
            case "5":
                break
    print()          

if __name__ == "__main__":
    main()