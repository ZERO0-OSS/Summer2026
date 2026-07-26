from Taskmanger import Taskmanger
from Task import Task

if __name__=="__main__":
    manger=Taskmanger()
    manger.load()
    manger.show_tasks()
    while(True):
        operate=input("你要进行的操作：  ")
        if operate=='A':
            new_name=input("你要新建的任务名称： ")
            if manger.tasks:
                task=Task(manger.tasks[-1].id+1,new_name)
            else:
                task=Task(1,new_name)
            manger.add_task(task)
        elif operate=='D':
            id=int(input("你要删除的任务的编号"))
            manger.delet_task(id)
        elif operate=='S':
                manger.show_tasks()
        elif operate=='U':
            id=int(input("你要修改的任务编号"))
            newName=input("你要更新的名字")
            for task in manger.tasks:
                if task.id==id:
                    task.upate_taskname(newName)
                    print("修改成功")
                    break
        elif operate=='F':
            id=int(input("你已经完成的任务编号"))
            for task in manger.tasks:
                if task.id==id:
                    task.finish_task(id)
                    print("再接再厉")
                    break
        elif operate=='0':
            manger.dump()
            break
        


