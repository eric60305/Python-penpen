#集合的運算
#s1={3,4,5}
#print(10 not in s1)
#s1={3,4,5}
#s2={4,5,6,7}
#s3=s1&s2 #交集 取兩個集合中 相同的資料
#s3=s1|s2 #聯集 取兩個集合中的所有資料 但不重覆取
#s3=s1-s2 #差集 從s1中 減去和s2重疊的部分
#s3=s1^s2 #反交集 取兩個集合中 不重疊的部分
#print(s3)
#s=set("hello") #把字串中的字母拆解成集合 #set(字串)
#print("h" in s)
#print("A" in s)
#字典的運算 ket-value配對
#dict={"apple":"蘋果","bug":"蟲蟲" }
#dict["apple"]="小蘋果"
#print(dict["apple"])
#dict={"apple":"蘋果","bug":"蟲蟲" }
#print("test" not in dict) #判斷key是否存在
#dict={"apple":"蘋果","bug":"蟲蟲" }
#print(dict)
#del dict["apple"] #刪除字典中的鍵值對(key-value pair)
#print(dict)
dict={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dict)

