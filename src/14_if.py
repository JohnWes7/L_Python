import random

a = 2020
if a > 2020:
    print(f"{a}大于2020")
else:
    print(f"{a}小于等于2020")

if a > 2020:
    print(">")
elif a == 2020:
    print("=")
else:
    print("<")

b = -1
print(0 if b < 0 else b)

# test
# vector2 = input("输入点的坐标：x,y : ").split(",")
vector2 = [random.randint(-1, 1), random.randint(-1, 1)]
print(vector2)

if int(vector2[0]) > 0:
    if int(vector2[1]) > 0:
        print(f"({vector2[0]},{vector2[1]}) 在第一象限")
    elif int(vector2[1]) == 0:
        print(f"({vector2[0]},{vector2[1]}) 在x轴上")
    else:
        print(f"({vector2[0]},{vector2[1]}) 在第四象限")
elif int(vector2[0]) == 0:
    if int(vector2[1]) == 0:
        print(f"({vector2[0]},{vector2[1]}) 是原点")
    else:
        print(f"({vector2[0]},{vector2[1]}) 在y轴上")
else:
    if int(vector2[1]) > 0:
        print(f"({vector2[0]},{vector2[1]}) 在第二象限")
    elif int(vector2[1]) == 0:
        print(f"({vector2[0]},{vector2[1]}) 在x轴上")
    else:
        print(f"({vector2[0]},{vector2[1]}) 在第三象限")

# scorc = int(input("score [0-100] : "))
score = random.randint(0, 100)
print(f"score : {score}")

if score > 100:
    print("illegal score")
elif score <= 100 and score >= 90:
    print("A")
elif score < 90 and score >= 80:
    print("B")
elif score < 80 and score >= 70:
    print("C")
elif score < 70 and score >= 60:
    print("D")
else:
    print("E")
