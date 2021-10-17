import os
import random

# print(os.getcwd())
# print("abspath:")
# print(os.path.abspath(__file__))
# print(os.path.abspath("aaaa.py"))
# print("realpath:")
# print(os.path.realpath(__file__))
# print(os.path.realpath("aaaa.py"))
# print(__file__)
# print(__name__)

# os.makedirs("tmp") #创建文件夹 已存在就不能创建了
# os.rmdir("tmp")  # 删除文件夹 找不到文件夹也会报错

f = open("data/aaa.txt", "w")
f.write("Hello Python\n")
f.write("aaa\n")
f.write("123\n")
f.close()

f = open("data/aaa.txt", "a")
f.write("Hello Python\n")
f.write("aaa\n")
f.write("123\n")
f.close()

with open("data/aaa.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("aaa\n")
    f.write("123\n")

with open("data/aaa.txt", "r") as f:
    print("======read:=====")
    #print(f.read())  # 读取指定数量字符的内容
    print("=====readline:=====")
    print(f.readline(),end="")  # 读取一行
    print("=====readlines:=====")
    print(f.readlines(),end="")  # 读取所有行

# print("================图片====================")
# with open("data/test_image.jpg","rb") as f:
#     # print(f.read())
#     with open("data/copy_image.jpg","wb") as ci:
#         ci.write(f.read())

print("\n====================test=====================")

# with open("data/test.txt","w") as file:
#     for i in range(100):
#         file.write(f"192.168.1.{random.randint(0,50)}\n")

with open("data/test.txt","r") as file:
    print("the count of 192.168.1.6 :", file.readlines().count("192.168.1.6\n"))