a,b=map(int,input("What are your numbers?").split())#map将字符列表全部转化为int类型，input读取整一行，split将字符串分裂
print("What your operate?")##在Python中print自动换行，若不想要则print( ,end='')
temp=input()
if temp=='+':
    print(a+b)
elif temp=='-':
    print(a-b)
elif temp=='*':
    print(a*b)
elif temp=='/':
    print(a/b)
