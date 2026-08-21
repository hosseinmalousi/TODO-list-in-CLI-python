import os
import Asccii_art
import uuid
import datetime

def print_art():
    print()
    print(Asccii_art.art + "\n")



class Task:
    
    tasks=[]
    
    def __init__(self,task,desc="",date="nodate"):
        self.uniq_code = str(uuid.uuid4())
        self.task = task
        self.date = date
        self.desc = desc
        self.done = False
        Task.tasks.append({"uniq_code":self.uniq_code,"task":self.task,"desc":self.desc,"date":self.date , "done" : self.done})
    
    def __str__(self):
        return f"the task : {self.task} is due to {datetime.date(self.date)}\ndescirption : '{self.desc}'"
        
    @classmethod
    def list_tasks(cls):
        print("***************")
        ### show it as a string and sort them or with bullet points
        for task in cls.tasks:
            print(f"{task["task"]} {(task["date"])} {task["desc"]} {task["done"]}")
        print("***************")

def add_task():
    task_name=input("What do u wanna do champ ? 🎖️\n ")
    ### date should be formed correctly
    date=input("when do u wanna do it (DD-MM-YYYY)? (leave blank for no date)\n")
    if date :
        date = datetime.datetime.strptime(date,"%d-%m-%Y").date()
    desc=input("is there any decription ? (enter to leave it blank) \n")
    Task(task_name,desc,date)

def main():
    print_art()
    is_running = True
    while is_running:
        print(f"today is {datetime.date.today().strftime("%A")} {datetime.date.today().strftime("%d:%m:%Y")}")
        if Task.tasks:
            Task.list_tasks()
        
        action = input("""1.tick a task \n2.add a task  \n3.delete a task \n4.edit a task \n5.quit the program\nplease add (1 , 2 , 3, 4)""")
        
        match action:
            case "1" :
                pass
            case "2":
                ### make it a func and show the tasks more beutiful
                add_task()
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
        
        
        
        

if __name__ == "__main__":
    main()