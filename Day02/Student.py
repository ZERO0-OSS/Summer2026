books = {
    "算法导论":50,
    "Python编程":40,
    "数据结构":60
}
operate=input("请输入你的操作")
if operate=='C':
    booksNmae=input("请输入书的名字")
    print(books[booksNmae])
elif operate=='A':
    booksNmae=input("请输入书的名字")
    price=int(input("请输入书的价格"))
    books[booksNmae]=price
elif operate=='M':
    Max=0
    for i in books:
        if books[i]>Max:
            Max=books[i]
            booksNmae=i
    print(f"最贵的书为{booksNmae},价格为{Max}")
