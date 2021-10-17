info = "hello world and a and b"
# find index count
print("="*10, "find", "="*10)
print(info.find("and"))
print(info.find("and", 15, 30))
print(info.find("ands"))  # 没有找到会返回-1

print("="*10, "index", "="*10)
print(info.index("and"))
print(info.index("and", 15, 30))
# print(info.index("ands")) #没有找到会直接报错

print("="*10, "count", "="*10)
print(info.count("and"))
print(info.count("and", 15, 30))
print(info.count("ands"))

print("="*10, "upper", "="*10)
print(info.upper())
print(info.lower())
print(info.title())  # 首字母大写
print(info.capitalize())  # 只有第一个单词的首字母大写

print("="*10, "replace", "="*10)
print(info.replace("and", "addd"))  # 全部替换
print(info.replace("and", "odd", 1))  # 只要替换一次

print("="*10, "split", "="*10)
print(info.split())  # 默认是按照空格来分割
print(info.split("and"))

print("="*10, "join", "="*10)
temp = info.split()
# Concatenate any number of strings. The string whose method is called is inserted in between each given string. The result is returned as a new string.
print("\t".join(temp))

print("="*10, "strip", "="*10)
info2 = "   python nice!   "
print(info2.strip())
print(info2.lstrip())
print(info2.rstrip())

# startwith endwith 判断是否以指定字符开始或者结尾
print("="*10, "start end", "="*10)
print(info.startswith("python"))
print(info.startswith("hello"))
print(info.endswith('b'))


print("="*10, "判断字符串是否满足某一格式", "="*10)
info3 = "123"
info4 = "abc"
info5 = "abc123"
info6 = "abc_123"
print(info3.isdigit())  # 纯数字
print(info4.isalpha())  # 纯字母
print(info5.isalnum())  # 数字+字母
print(info6.isalnum())

#homework
print("love you!"*100)
print("to be or not to be"[::-1])
info0 = "chinachinachina"
