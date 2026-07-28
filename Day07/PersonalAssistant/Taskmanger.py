import json
from Task import Task
class Taskmanger:

    def __init__(self):
        self.tasks=[]
    
    def add_task(self,task):
        self.tasks.append(task)
        print("新建成功")
        self.dump()
        

    def delet_task(self,id):
        self.tasks[:]=[task for task in self.tasks if task.id!=id]
        self.dump()
        

    def show_tasks(self):
        for task in self.tasks:
            print(task.id,task.name,task.done)
            
    def dump(self):
        data=[]

        for task in self.tasks:
            data.append({"id":task.id,"name":task.name,"done":task.done})

        with open("data.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

    def load(self):
        try:
            with open("data.json","r",encoding="utf-8") as file:
                data=json.load(file)
                for item in data:
                    task=Task(item["id"],item["name"])
                    task.done=item["done"]
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks=[]

    