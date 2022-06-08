import os
import random

#输入文件路径
gene_file_path = os.path.dirname(__file__) + "/1-3"
#输出文件路径
ans_file_path = os.path.dirname(__file__) + "/ans"


def main():
    ans_list = []

    while True:
        gene_file_path = input("输入文件绝对或者相对路径\n")

        if os.path.exists(gene_file_path):
            break
        else:
            print("未找到文件")
    input(f"已找到文件 确认路径为:{gene_file_path} 回车开始执行\n")

    with open(gene_file_path, "r", encoding='utf-8') as file:
        line_count = 0
        same_count = 0
        while True:
            line = file.readline()
            if line == "":
                break
            line = line.strip()
            line = line.split("\t")

            is_same = False
            for item in ans_list:
                if item[0].__eq__(line[0]) and item[1].__eq__(line[1]):
                    is_same = True
                    break
                if item[0].__eq__(line[1]) and item[1].__eq__(line[0]):
                    is_same = True
                    break

            if not is_same:
                ans_list.append(line)
            else:
                same_count += 1
            print(f"对比{line_count}完成 {line} ans:{is_same}")
            line_count += 1

        print(f"一共{same_count}个重复")

    with open(ans_file_path, "w", encoding='utf-8') as file:
        templist = []
        for line in ans_list:
            templist.append("\t".join(line) + "\n")
        ans_list = templist

        file.writelines(ans_list)


if __name__ == "__main__":
    # try:
    #     main()
    # except Exception as e:
    #     print(e)
    #     input("回车退出")
    print(random.randint(1,100))
