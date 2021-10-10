info = "my name is johnwest"
print(info)
print("connt:",info.count,"\n")

print(info[4])
print(info[-2]) #负数表示从后面开始数

print(info[0:2]) # 开始：结束 注意：开始的下表including 结束下标excluding
print(info[0:-2])
print(info[0:]) # 截取到最后，可以省略最后下标
print(info[:-1]) # 从头开始 可以省略开始下标
print(info[1:])
print(info[4:8])
#print(info[-3:info.count])

print(info[::-1]) #开始:结束:步长 