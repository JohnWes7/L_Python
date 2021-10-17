import os

def test1(a: int, b: int):
    print(a + b)

if __name__ == "__main__":
    test1(5,3)

    print("__file__",__file__)
    print("abs__file__", os.path.abspath(__file__))