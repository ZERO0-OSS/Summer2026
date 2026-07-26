# Day04 Notes —— Python面向对象重构 TodoList 项目
## 今日目标

将之前的函数式 TodoList：
main.py
 |
 tasks列表
 |
 函数操作dict
```
升级为：
```
main.py
 |
 TaskManager对象
 |
 管理Task对象
 |
 JSON持久化
```

学习：

* Python class
* 对象设计
* 类之间关系
* 多文件项目结构
* JSON持久化
* 对象与数据转换

---

# 1. 为什么需要面向对象重构？

之前版本：

```python
task={
    "id":1,
    "name":"学习Python",
    "done":False
}
```

通过函数：

```python
add_task()
delete_task()
update_task()
```

操作数据。

问题：

随着功能增加：

任务可能增加：

```python
{
"id":1,
"name":"学习Python",
"done":False,
"priority":"high",
"deadline":"2026-08-01"
}
```

所有函数都需要知道dict内部结构。

例如：

```python
task["done"]
```

大量出现。

如果以后修改：

```python
task["status"]
```

需要修改很多地方。

所以引入对象：

---
# 2. Task类：表示一个任务

一个任务本身：

具有：

属性：

```python
id
name
done
```

行为：

```python
完成任务
修改名字
展示信息
```

设计：

```python
class Task:

    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.done=False


    def finish_task(self):
        self.done=True


    def update_taskname(self,newName):
        self.name=newName
```

---

创建对象：

```python
task=Task(1,"学习Python")
```

内存：

```
Task对象

id=1
name=学习Python
done=False
```

---

# 3. TaskManager：管理任务

关键理解：

## Task ≠ TaskManager

Task：

> 一个任务

TaskManager：

> 管理很多任务

关系：

```
TaskManager

      |
      |
      ↓

 tasks列表

      |
      |
      ↓

 Task对象
 Task对象
 Task对象
```

---

错误理解：

```
TaskManager = tasks列表
```

正确：

```
TaskManager拥有tasks列表
```

代码：

```python
class TaskManager:

    def __init__(self):
        self.tasks=[]
```

这里：

```python
self.tasks
```

是TaskManager的属性。

---

# 4. 为什么不用Task类代替TaskManager？

思考：

为什么：

```python
class Task:
```

里面不直接管理所有任务？

因为：

一个任务：

```
Task
```

不应该负责：

* 创建其他任务
* 删除其他任务
* 保存所有任务

类似：

学生：

```
Student
```

不是：

```
StudentManager
```

汽车：

```
Car
```

不是：

```
CarManager
```

这是对象职责划分。

---

# 5. is-a 和 has-a

面向对象两个重要关系：

---

## is-a

表示继承：

例如：

```
狗 是一种 动物
```

代码：

```python
class Dog(Animal):
```

---

## has-a

表示拥有：

例如：

```
汽车 有一个 发动机
```

代码：

```python
class Car:

    def __init__(self):
        self.engine=Engine()
```

TodoList：

属于：

```
TaskManager has Task
```

所以使用组合：

```python
self.tasks=[]
```

---

# 6. 多文件结构设计

项目：

```
TodoList

├── main.py
│
├── Task.py
│
├── TaskManager.py
│
└── data.json
```

职责：

---

## Task.py

负责：

任务对象。

例如：

```python
class Task:
```

---

## TaskManager.py

负责：

任务管理。

例如：

```python
class TaskManager:
```

包括：

```python
add_task()

delete_task()

save()

load()
```

---

## main.py

负责：

程序入口。

不是类。

只是：

```python
if __name__=="__main__":
```

启动程序。

main不负责：

* 保存数据
* 操作列表
* JSON处理

它只负责：

调用对象。

---

# 7. main函数执行流程

正确流程：

```
程序启动

    ↓

main.py

    ↓

创建TaskManager对象

    ↓

manager.load()

    ↓

JSON数据恢复成Task对象

    ↓

用户操作

    ↓

manager.add_task()

manager.delete_task()

manager.save()
```

---

# 8. JSON持久化

持久化：

就是：

程序关闭后数据不会丢失。

流程：

## 保存

```
Task对象

↓

dict

↓

JSON文件
```

例如：

Task对象：

```python
Task(1,"学习Python")
```

转换：

```json
{
"id":1,
"name":"学习Python",
"done":false
}
```

---

## 读取

相反：

```
JSON

↓

dict

↓

Task对象

↓

self.tasks
```

---

# 9. 为什么load不能直接append JSON数据？

错误：

```python
def load(self):

    data=json.load(file)

    for item in data:
        self.tasks.append(item)
```

结果：

```
self.tasks

[
 dict,
 dict
]
```

但是程序需要：

```
[
 Task对象,
 Task对象
]
```

因为后续：

```python
task.id
```

而dict需要：

```python
task["id"]
```

所以需要转换：

```python
task=Task(
    item["id"],
    item["name"]
)

task.done=item["done"]

self.tasks.append(task)
```

---

# 10. 类里面调用自己的方法

问题：

在：

```python
add_task()
```

里面能不能调用：

```python
save()
```

答案：

可以。

但是：

错误：

```python
save()
```

正确：

```python
self.save()
```

原因：

self表示当前对象。

例如：

```python
class TaskManager:


    def add_task(self,task):

        self.tasks.append(task)

        self.save()


    def save(self):

        pass
    
# 12. 今天遇到的重要Bug

## Bug1：

```python
manager.tasks[-1]
```

报：

```
IndexError
```

原因：

列表为空：

```python
[]
```

解决：

```python
if manager.tasks:

    id=manager.tasks[-1].id+1

else:

    id=1
```

---

## Bug2：

load读取后类型错误

JSON：

```
dict
```

程序：

需要：

```
Task对象
```

需要反序列化。

---

# 今日核心收获

今天真正学习的不是：

“怎么写class”

而是：

## 软件设计思想

以前：

```
数据
+
函数
```

现在：

```
对象

包含：

数据
+
行为
```

程序结构：

```
main
 |
 ↓
TaskManager
 |
 ↓
Task对象
 |
 ↓
JSON文件
```

这已经接近真实后端项目的数据流：

```
数据库

↓

对象模型

↓

业务逻辑

↓

用户操作
```

---

# Day04完成状态

✅ Python class基础
✅ 对象创建
✅ self理解
✅ 类之间关系
✅ 组合(has-a)
✅ 多文件项目结构
✅ JSON持久化思想
✅ load/save设计
✅ 方法之间调用

待完成：

⬜ 完整跑通TodoList 4.0
⬜ 优化TaskManager接口
⬜ 写README
⬜ GitHub提交

---

这一份可以直接保存为：

```
Summer2026/Python/Day04/Notes.md
```

另外提醒一下：你 Day04 最大的突破不是代码量，而是你今天连续问的几个问题：

* “为什么TaskManager不是列表？”
* “为什么不能合并？”
* “为什么JSON不能直接append？”
* “为什么类里面要self.save？”

这些问题其实都是**软件设计层的问题**，比单纯完成TodoList功能价值更高。你今天的学习方向是对的。
