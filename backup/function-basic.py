# 定義函式
# 函式內部的程式碼 若是沒有呼叫 就不會執行
# def multiply(n1,n2):
#     #print(n1*n2)
#     #result =n1*n2
#     return n1*n2

# 呼叫函式
# value = multiply(3,4)+multiply(10,5) #(3*4)+(10*5)
# print(value)
# multiply(3,4)
# multiply(10,8)

# 函式可用來做程式的包裝 同樣的邏輯可以重複利用
def calculate(n):
    sum =0
    for i in range(1,n+1):   # 尾數不包含尾巴 故+1
        sum +=i
    print (sum)

n = int(input("輸入一個數字:"))
calculate(n)


# sum =0
# for i in range(21):
#     sum +=i
# print (sum)

 

