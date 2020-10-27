import pandas as pd

# 讀取資料
data = pd.read_csv("pandas example\googleplaystore.csv") # 把csv格式的檔案讀取成DataFrame

# 觀察資料
#print(data)
#print("資料數量", data.size)
print("資料形狀(列/欄)", data.shape)
print("資料欄位", data.columns)
print("=====================================")

# 分析資料 評分的各種統計數據
# print(data["Rating"])
# condition = data["Rating"] <= 5
# data = data[condition]
# # print(data)
# print("平均數",data["Rating"].mean())
# print("中位數", data["Rating"].median())
# print("取得前1000個應用程式的平均",data["Rating"].nlargest(1000).mean())

# print(data.iloc[:99, 2])
# a = data.iloc[:100, 2]
# print(a.mean())

# 分析資料 安裝數量的各種統計數據
# print(data["Installs"])
# print(data["Installs"][10472])
# print(data["Installs"][10471])
# print(data["Installs"][10470])
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "").replace("Free", ""))
# print(data["Installs"])

# print("平均數", data["Installs"].mean())
# condition = data["Installs"] > 100000
# print("安裝數量大於100000的應用程式有幾個",data[condition].shape[0]) # (4950,13) 0表示4950個 1表示13欄位

# 基於資料的應用 關鍵字搜尋應用程式名稱
keyword = input("請輸入關鍵字:")
condition = data["App"].str.contains(keyword, case=False) # case=False忽略大小寫
print(data[condition]["App"])
print("包含關鍵字應用程式的數量",data[condition].shape[0])
# print("包含關鍵字應用程式的數量",data[condition]["App"].shape)
# print("包含關鍵字應用程式的數量",len(data[condition]["App"]))
# print(data[condition]["App"][2036])