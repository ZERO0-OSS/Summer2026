import json
import user
class userManger:
    def __init__(self):
        self.user_manger=[]

    def register(self,name,password):
        User=user(name,password)
        self.user_manger.append(User)
        print("注册成功")

        

    def load(self):
        try:
            with open("user.json","r",encoding="utf-8") as file:
                data=json.load(file)
                for user in data:
                    User=user(user["name"],user["password"])
                    self.user_manger.append(User)
        except FileNotFoundError:
            self.user_manger=[]

    def dump(self):
        data=[]
        for user in self.user_manger:
            data.append({"name":user.name,"password":user.password})
        with open("user.json","w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)



    