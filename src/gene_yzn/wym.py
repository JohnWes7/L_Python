
import os

import numpy as np


def read_list():
    # filename = input("输入文件名(与程序保持在相同目录下):")
    filename = "1-3"
    path = os.path.dirname(__file__) + "/" + filename
    f = open(path, 'r', encoding='utf-8')
    src_list = f.readlines()
    real_list = []
    for i in src_list:
        i = list(i.strip().split("\t"))
        real_list.append(i)
    f.close()
    return real_list


def get_only_element(lst):
    if len(lst) == 0:
        return []
    lst = np.array(lst)
    result = np.array([lst[0]])
    print(lst)

    #print_lst(lst[0:,0:2])
    # for item in lst[1:, :]:
    #     if item[0:2] not in result[0:, 0:2] and item[0:2:-1] not in result[0:, 0:2]:
    #         result = np.row_stack((result, item))

    for item in lst[1:,:]:
        is_same = None
        for row in result[:,:2]:
            is_same = True
            for num in item[0:2]:
                is_same = is_same and (num in row)
            if is_same == True:
                break
        if not is_same:
            result = np.row_stack((result,item))

    print(result)
    return result


def write_list(lst):
    f = open("./result", "w")
    for item in lst:
        f.write(str(item)+"\n")
    f.close()


def print_lst(lst):
    for item in lst:
        print(item)


if __name__ == '__main__':
    lst = read_list()
    #print(lst)
    lst = get_only_element(lst)
    #write_list(lst)

    # test_list=[
    #     [1,2,3],
    #     [2,1,4],
    #     [2,3,3]
    # ]

    # compare_list = [1,2,5]

    # test_list = np.array(test_list)
    # print(test_list)
    # ans = np.array([test_list[0]])
    
    # index = 0
    # for item in test_list[1:,:]:
    #     index+=1

    #     print(f"{item}\t{ans}")
    #     is_same = None
    #     for row in ans[:,0:2]:
    #         is_same = True
    #         for num in item[0:2]:
    #             print(f"判断{num}在{row}里面")
    #             is_same = is_same and (num in row)
            
    #         if is_same == True:
    #             break
        
    #     print(f"对比第{index}次 {is_same}")
    #     if not is_same:
    #         ans = np.row_stack((ans,item))
        
    # print(ans)

    # # a = np.array(test_list)
    # # b = np.array(compare_list)

    # # print(b[0:2] in a[:,0:2])

    # a = np.array([2,3,3])
    # b = np.array([[1,2,3],[2,1,4]])

    # c = np.array([5,1])
    # d = np.array([[1,2],[2,1]])

    # print()
    # print(a[0:2])
    # print(b[:,0:2])
    # print(a[0:2] in b[:,0:2])
    # print(c in d)

    


