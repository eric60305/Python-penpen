# 載入 pandas 模組
import pandas as pd

# 篩選練習 - Series Series
# data = pd.Series([30, 15, 20])
# # condition = [True, False, True]
# condition = data > 18
# print(condition)
# filteredData = data[condition]
# print(filteredData)

# data = pd.Series(["您好", "Python", "Pandas"])
# condition = data.str.contains("P")
# print(condition)
# # condition = [False, True, True]
# filteredData = data[condition]
# print(filteredData)

# 篩選練習 - DataFrame
data = pd.DataFrame({"name":["Amy", "John", "Bob"],
                    "salary": [30000, 50000, 40000]})
# print(data)
condition = data["name"] == "Amy"
print(condition)
# condition = [False, True, True]
filteredData = data[condition]
print(filteredData)
