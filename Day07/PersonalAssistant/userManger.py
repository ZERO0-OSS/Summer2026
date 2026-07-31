import json
from user import User

class userManger:
    def __init__(self):
        self.user_manger=[]

    def register(self,name,password):

        User=User(name,password)
        self.user_manger.append(User)
        print("注册成功")
        self.dump()

    def login(self,name,password):
        self.load()
        for item in self.user_manger:
            if item.name==name and item.password==password:
                print("登陆成功")
                return item.name

        print("登陆失败")
        return None
        

    def load(self):
        try:
            with open("user.json","r",encoding="utf-8") as file:
                data=json.load(file)
                for user in data:
                    user=User(user["name"],user["password"])
                    self.user_manger.append(user)
        except FileNotFoundError:
            self.user_manger=[]

    def dump(self):
        data=[]
        for user in self.user_manger:
            data.append({"name":user.name,"password":user.password})
        with open("user.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)



    