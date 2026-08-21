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
        Task.tasks.append({"uniq_code":self.uniq_code,"task":self.task,"desc":self.desc,"date":self.date})
    
    def __str__(self):
        return f"the task : {self.task} is due to {self.date} with descirption of '{self.desc}'"
        
    @classmethod
    def list_tasks(cls):
        print("***************")
        ### show it as a string and sort them or with bullet points
        for task in cls.tasks:
            print(task)
        print("***************")

    
def main():
    print_art()
    is_running = True
    while is_running:
        print(f"today is {datetime.date.today().strftime("%A")} {datetime.date.today().strftime("%d:%m:%Y")}")
        ### show it only when u have a task 
        Task.list_tasks()
        
        action = input("""1.tick a task \n2.add a task  \n3.delete a task \n4.edit a task \n5.quit the program\nplease add (1 , 2 , 3, 4)""")
        
        match action:
            case "1" :
                pass
            case "2":
                ### make it a func and show the tasks more beutiful
                task_name=input("What do u wanna do champ ? 🎖️\n ")
                date=input("when do u wanna do it ? (leave blank for no date)\n")
                desc=input("is there any decription ? (enter to leave it blank) \n")
                Task(task_name,desc,date)
            case "3":
                pass
            case "4":
                pass
            case "5":
                break
        
        
        
        

if __name__ == "__main__":
    main()