class student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def show_me(self):
        print(self.name, self.age)