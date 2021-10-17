class Person:
    def __init__(self, name: str, sex: str = "未知", hobby: str = "递烟，送酒，给人烫头") -> None:
        self.name = name
        self.sex = sex
        self.hobby = hobby

    def Eat(self):
        print("eat something....")

    def Study(self, info):
        print(f"learning {info}")

    def ShowSelf(self):
        return f"name : {self.name}, sex : {self.sex}, hobby : {self.hobby}"


p1 = Person(name="Dio")
print(p1.hobby)

p1.Eat()
p1.Study("nothing")
print(p1.ShowSelf())


print("\n===== test =====")


class Student:
    def __init__(self, id: int, name: str, score: int, age: int) -> None:
        self.id = id
        self.name = name
        self.score = score
        self.age = age

    def Study(self, info):
        print(f"{self.name} is studying {info} ......")

    def toString(self):
        return f"id = {self.id}, name = {self.name}, score = {self.score}, age = {self.age}"


s1 = Student(id="000", name="Dio", score="100", age=200)
s1.Study("stand")
print(s1.toString())
