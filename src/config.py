import os
import sys

class config:
    absolute_create_files_PATH = os.path.dirname(os.path.dirname(__file__)) + "/create_files"
    absolute_data_PATH = os.path.dirname(os.path.dirname(__file__)) + "/data"
    absolute_src_PATH = os.path.dirname(__file__)


"""
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。
如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，
并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，
即引用的是实例属性，除非删除了该实例属性。
"""

if __name__ == "__main__":
    print("config: __file__",__file__)
    print("config: abs__file__", os.path.abspath(__file__))
    for i in sys.path:
        print(i)
    print()
    # import module1
    
    input("done.")