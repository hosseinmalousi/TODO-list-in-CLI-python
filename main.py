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
    
    
    tasks=[]
    with open(file_path,"r") as f:
        data = json.load(f)
        for task in data :
            tasks.append(task)
    
    def __init__(self,task,desc="",date="nodate"):
        self.uniq_code = str(uuid.uuid4())
        self.task = task
        self.date = date
        self.desc = desc
        self.done = False
        ### this line under must be changed i guess
        Task.tasks.append({"uniq_code":self.uniq_code,"task":self.task,"desc":self.desc,"date":self.date , "done" : self.done})
    
    def __str__(self):
        return f"the task : {self.task} is due to {datetime.date(self.date)}\ndescirption : '{self.desc}'"
        
    @classmethod
    def list_tasks(cls):
        print("***************")
        ### show it as a string and sort them or with bullet points
        enu_list = enumerate(cls.tasks,1) ### it only effect on showing and the new ones also works 
        for i,task in enu_list:
            # print()
            print(f"{i}. the task : {task["task"]}, is due to {task["date"]}; descirption : '{task["desc"]}'")
        print("***************")
    
    @classmethod
    def write_to_file(cls):
        with open(file=file_path,mode="w+" ) as file:
            json.dump(cls.tasks,file,indent=4)

def add_task():
    task_name=input("What do u wanna do champ ? 🎖️\n ")
    ### date should be formed correctly
    date=input("when do u wanna do it (DD-MM-YYYY)? (leave blank for no date)\n")
    if date :
        date = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    else :
        date = "no date"
    desc=input("is there any decription ? (enter to leave it blank) \n")
    Task(task_name,desc,date)

def main():
    print_art()
    is_running = True
    while is_running:
        print(f"today is {datetime.date.today().strftime("%A")} {datetime.date.today().strftime("%d:%m:%Y")}")
        if Task.tasks :
            Task.list_tasks()
        
        action = input("""1.tick a task \n2.add a task  \n3.delete a task \n4.edit a task \n5.quit the program\nplease add (1 , 2 , 3, 4)""")
        
        match action:
            case "1" :
                pass
            case "2":
                ### make it a func and show the tasks more beutiful
                add_task()
                Task.write_to_file()
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
                

if __name__ == "__main__":
    main()