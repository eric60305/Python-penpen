# 定義類別、與類別屬性(封裝在類別中的變數和函式)
#定義一個類別IO. 有兩個屬性 supportedSrcs 和 read
class IO:
    supportedSrcs = ["console", "file","e"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("No supported")
        else:
            print("Read from",src)

# 使用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("e")
IO.read("console")
IO.read("ce")