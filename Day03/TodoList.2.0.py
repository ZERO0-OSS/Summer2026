import json

def load():
    try:
        with open("data.json","r",encoding="utf-8") as file:
            tasks=json.load(file)
            return tasks
    except FileNotFoundError:#不要漏写
        return []

def dump(tasks):
    with open("data.json","w",encoding="utf-8") as file:
        json.dump(tasks,file,indent=4,ensure_ascii=False)


tasks=load()

def show_task():
    for task in tasks:
        print(task["id"],task["name"],task["done"])

def add_task():
    taskname=input("请输入要添加的任务名称 ")
    if tasks:
        new_id=tasks[-1]["id"]+1
    else:
        new_id=1
    tasknew={"id":new_id,"name":taskname,"done":False}
    tasks.append(tasknew)
    dump(tasks)
    print("添加成功")

def delete_task():
    id=int(input("请输入要删除的任务编号 "))

    '''#在遍历列表是从前往后删除列表元素，危险！！！
    #因为删除后，元素自动向前，会有部分元素遍历失败
    #可以从后往前，或者用列表推导式
    for task in tasks:
        if task["id"]==id:
            tasks.remove(task)
            print("已删除")
            break'''
    tasks[:]=[task for task in tasks if task["id"]!=id]
    dump(tasks)

            
def update_task():
    taskId=int(input("要修改的任务编号 "))
    tasknewName=input("新的名字 ")
    for task in tasks:
        if task["id"]==taskId:
            task["name"]=tasknewName
            print("修改成功")
            break
    dump(tasks)

def finish_task():
    id=int(input("你已经完成的操作 "))
    for task in tasks:
        if task["id"]==id:
            task["done"]=True
            print("修改成功")
            break
    dump(tasks)



if __name__=="__main__":
    show_task()
    while(1):
        operate=input("你的操作:  ")
        if operate=='S':
            show_task()
        elif operate=='A':
            add_task()
        elif operate=='D':
            delete_task()
        elif operate=='U':
            update_task()
        elif operate=='F':
            finish_task()
        elif operate=='0':
            break
        





