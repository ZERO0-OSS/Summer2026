task=[{"id":1,"name":"学习Python","done":False}]

def show_task():
    for tasks in task:
        print(tasks["id"],tasks["name"],tasks["done"])

def add_task():
    taskname=input("请输入要添加的任务名称 ")
    tasknew={"id":len(task)+1,"name":taskname,"done":False}
    task.append(tasknew)
    print("添加成功")

def delete_task():
    id=int(input("请输入要删除的任务编号 "))
    for tasks in task:
        if tasks["id"]==id:
            task.remove(tasks)
            print("已删除")

def update_task():
    taskId=int(input("要修改的任务编号 "))
    tasknewName=input("新的名字 ")
    for tasks in task:
        if tasks["id"]==taskId:
            tasks["name"]=tasknewName
            print("修改成功")

if __name__=="__main__":
    show_task()
    while(1):
        operate=input("你的操作:  ")
        if operate=='S':
            show_task()
        if operate=='A':
            add_task()
        if operate=='D':
            delete_task()
        if operate=='U':
            update_task()
        if operate=='0':
            break
        





