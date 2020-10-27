# 載入 pandas 模組
import pandas as pd

# 資料索引 pd.DataFrame(字典,index = 索引列表)
data = pd.DataFrame({"name":["Amy", "John", "Bob"],
                     "salary": [30000, 50000, 40000]},
                     index=["a", "b", "c"])

print(data)
print("=======================")

# 觀察資料
# print("資料數量", data.size)
# print("資料形狀(列/欄)", data.shape)
# print("資料索引", data.index)

# 取得列(Row/橫向) 的 Series資料 根據順序 根據索引
# print("取得第二列", data.iloc[1], sep="\n")
# print("=======================")
# print("取得第c列", data.loc["c"], sep="\n")

# 取得(Column/直向)的 Series資料 根據欄位的名稱
# print("取得name欄位", data["name"], sep="\n")
# names = data["name"]  # 取得單維度的Series資料
# print("把name全部轉大寫", names.str.upper(), sep="\n")

# 計算薪水的平均值
# salarys = data["salary"]
# print("薪水平均值", salarys.mean())

# 建立新的欄位
data["revenue"] = [500000, 400000, 300000]  # data[新欄位的名稱]=列表
data["rank"] = pd.Series([3, 6, 1], index=["a", "b", "c"])  # data[新欄位的名稱]=Series的資料
data["CP"] = data["revenue"]/data["salary"]
print(data)
