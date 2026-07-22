def add(a,b):
    return a+b
def delince(a,b):
    return a-b
def chne(a,b):
    if b=='0':
        return "Don't chu yu 0"
    return a*b
def chu(a,b):
    return a/b

if __name__=="__main__":
    a,b=map(int,input("What are your numbers").split())
    print("What is your operate")
    temp=input()
    if temp=="+":
        print(add(a,b))
    elif temp=="-":
        print(delince(a,b))
    elif temp=="/":
        print(chu(a,b))
    elif temp=="*":
        print(chne(a,b))