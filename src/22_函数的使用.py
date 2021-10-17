def PrintName():
    print("hello world")


def PrintInfo(info):
    print(f"info : {info}")


PrintName()
PrintInfo("010110101010000111100010101")


def ParamsFunction(*list):
    for i in list:
        print(i)


ParamsFunction(1, 2, 3, 4, "johnwest")


def DictFunction(**dict):
    print(type(dict))
    print(dict.get("name"))


DictFunction(name="johnwest", id="jw7")


def AddInteger(a: int, b: int):
    print(a+b)


AddInteger(5, 3)


def ExchangeParameter(info1: str, info2: str = "johnwest"):
    print(f"info1 : {info1}, info2 : {info2}")


ExchangeParameter("12345", "56789")
ExchangeParameter("12345")
ExchangeParameter(info2="12345", info1="56789")


def Add(a: int, b: int):
    return a + b


sum = Add(5, 9)
sum2 = Add(sum, 5)
print(sum, sum2)
