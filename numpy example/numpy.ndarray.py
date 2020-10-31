# 載入 numpy 套件
import numpy as np

# 建立一維陣列
# data = np.array([3,2,6,4])
# print(data)

# data = np.empty(4) # 創造一個有四個資料的一維陣列 資料未指定
# print(data)

# data = np.zeros(3)
# print(data)

# data = np.ones(3)
# print(data)

# data = np.arange(8)
# print(data)

# 建立二維陣列
# data = np.array([  # 創造一個 3*3 的二維陣列
#     [2,3,2],
#     [1,5,2],
#     [4,2,1]
# ])
# print(data)

# data = np.empty([3,3]) # # 創造一個3*3的二維陣列 資料未指定
# print(data)

# # data = np.empty([5,5]) # # 創造一個5*5的二維陣列 資料未指定
# # print(data)

# data = np.ones([2,3])
# print(data)

# 建立三維陣列
# data = np.array([  # 根據列表創造一個 2*2*2 的三維陣列
#     [
#         [3,1],
#         [1,2]
#     ],
#     [
#         [2,5],
#         [10,2]
#     ]
# ])
# print(data)

# data = np.zeros([3, 1, 3]) # 創造一個3*1*3的三維陣列 資料都是0
# print(data)

# data = np.zeros([3, 2, 3]) # 創造一個3*1*3的三維陣列 資料都是0
# print(data)

# 建立高維陣列
# data = np.array([  # 根據列表創造一個 1*1*2*3 的四維陣列
#     [
#         [
#             [3, 2, 1],
#             [5, 5, 10]
#         ]

#     ]

# ])
# print(data)

data = np.ones([2,1,1,2]) # # 創造一個2*1*1*2的三維陣列 資料都是1
print(data)

# data = np.ones([2,1,3,2]) # # 創造一個2*1*3*2的三維陣列 資料都是1
# print(data)