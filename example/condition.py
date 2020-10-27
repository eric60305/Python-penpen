# 判斷式
#x=input("請輸入數字: ") # 取得字串形式的使用者輸入
#x=int(x) # 將字串型態轉換成數字型態
#if x>200:
    #print("大於200")
#elif x>100:
    #print("大於100 小於等於200")
#else:
    #print("小於等於 100")

#四則運算 (更改 循環 跳出)

while True:
    n1=input("輸入數字1: ")
    if n1 == "q":
        break
    n2=input("輸入數字2: ")

    op=input("請選擇運算字符: + - * /")
    
    if op == "+":
        print(int(n1)+int(n2))
    elif op == "-":
        print(int(n1)-int(n2))
    elif op == "*":
        print(int(n1)*int(n2))
    elif op == "/":
        print(int(n1)/int(n2)) 
    else:
        print("不支援的運算")
    
   
    