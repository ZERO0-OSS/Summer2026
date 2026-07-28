class Task:
    def __init__(self,id,name):
        self.name=name
        self.id=id
        self.done=False

    def upate_taskname(self,newName):
        self.name=newName
    
    def finish_task(self,id):
        self.done=True

    def show_task(self):
        print(self.id,self.name,self.done)