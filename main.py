import os
import Asccii_art
import uuid

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
    def get_the_list(cls):
        pass   

    
def main():
    print_art()
    task_name=input("What do u wanna do champ ? 🎖️\n ")
    date=input("when do u wanna do it ? (leave blank for no date)\n")
    desc=input("is there any decription ? (enter to leave it blank) \n")
    task = Task(task_name,desc,date)
    print(task)
    print(Task.tasks)

if __name__ == "__main__":
    main()