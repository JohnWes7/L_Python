dict1 = {}
dict2 = dict()
dict3 = {"name": "johnwest", "from": "???", "date": "2021.10.12"}

dict1["name"] = "亚丝娜"
print(dict1)

print("===== 获取 ======")
print(dict3["from"])  # 没索引到会报错
print(dict3.get("name"))  # 返回none
print(dict3.keys())
print(dict3.values())

# test
rank_list = [8, 8.5, 9, 9.5, 8.2, 10, 6, 8.8, 9.2, 8.2]
print(f"has 10 : {10 in rank_list}")
print(f"has 0 : {0 in rank_list}")
rank_list.sort()
del rank_list[0]
del rank_list[rank_list.__len__() - 1]
print(rank_list)
print("done")

input("直接关闭 或者 按回车键结束窗口")