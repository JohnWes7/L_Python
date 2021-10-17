import os

print(os.getcwd())  # 获取当前工作目录
print(os.path.abspath("src/person.py"))  # 获得文件的绝对路径 就是个字符串拼接
print(os.path.dirname("D:\L_Python\src\person.py"))

print(os.path.exists("D:\L_Python\src\person.py"))  # 判断文件存在
print(os.path.exists("D:\L_Python\src"))
print(os.path.exists("D:\L_Python\s"))

print(os.path.split("D:\L_Python\src\person.py")) # 字符串操作返回最后一个/之后的所有字符
print(os.path.split("D:\L_Python\src"))
print(os.path.split("D:\L_Python\s"))

print(os.path.splitext("D:\L_Python\src\person.py")) # 字符串操作返回 .之后的所有字符 没有.返回""
print(os.path.splitext("D:\L_Python\src\p.txt"))
print(os.path.splitext("D:\L_Python\src\p"))

print(os.path.isfile("person.py")) #只能判断当前文件夹下 判断是否是文件
print(os.path.isfile("D:\L_Python\src\person.py"))
print(os.path.isfile("D:\L_Python\src\per.py")) # 判断的文件和文件夹一定要存在
print(os.path.isfile("D:\L_Python\src"))

print("="*30)

print(os.path.isdir("D:\L_Python\src\person.py")) # 判断是否是文件夹
print(os.path.isdir("D:\L_Python\src\per.py"))
print(os.path.isdir("D:\L_Python\src"))
print(os.path.isdir("D:\L_Python\s"))#判断的文件和文件夹一定要存在

print("="*30)

print(os.listdir('.'))

