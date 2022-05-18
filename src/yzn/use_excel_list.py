import os
import random_stock
import pandas
import sys

list_file_path = os.path.dirname(__file__) + "/stock_list.xlsx"
save_path = os.path.dirname(__file__) + "/target_info.xlsx"

# 获取excel里面的数据


def get_stocklist_from_excel(excel_path) -> list:
    data = pandas.read_excel(excel_path)

    test = data.iloc[0:, 0]
    print(type(test))
    print(test)

    select_list = []
    for index, row in data.iterrows():
        code = "%06d" % row[0]

        temp_dict = {
            "href": f"http://guba.eastmoney.com/list,{code}.html",
            "code": code,
            "name": row[1]
        }

        select_list.append(temp_dict)

    return select_list


def main():
    # 设定参数
    temp = input("输入每种股票评论数量:\n")
    com_num = int(temp)
    is_divide_sheet = False
    while True:
        temp = input("是否分开sheet保存 y/n\n")
        if temp == "y":
            is_divide_sheet = True
            break
        elif temp == "n":
            is_divide_sheet = False
            break
        else:
            print("输入有误请重新输入")

    select_list = get_stocklist_from_excel(list_file_path)

    random_stock.get_all_comment(
        select_list=select_list, is_divide_sheet=is_divide_sheet, com_num=com_num, save_path=save_path)

    print("done")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("错误 建议截图发给我")
        info = sys.exc_info()
        print(info)
        print(e)
        input("回车退出")
