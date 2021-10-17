print("===== append =====")
name_list = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list)
name_list.append("亚丝娜")
print(name_list)
name_list.append(["白", "雪乃"])
print(name_list)

print("===== extend =====")
name_list1 = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list1)
name_list1.extend(["白", "雪乃"])
print(name_list1)
name_list1.extend("abc")
print(name_list1)
name_list1.extend(["abc"])
print(name_list1)

print("===== insert =====")
name_list2 = ["唐可可", "南小鸟", "小鸟游六花"]
name_list2.insert(1, "abc")
print(name_list2)

print("===== del =====")
name_list3 = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list3)
del name_list3[1]
print(name_list3)
#del name_list3 全部删除 相当于复制null

print("===== pop =====")
name_list4 = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list4.pop(1))
print(name_list4)

print("===== remove =====")
name_list5 = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list5)
name_list5.remove("南小鸟")
print(name_list5)

print("===== clear =====")
name_list6 = ["唐可可", "南小鸟", "小鸟游六花"]
print(name_list6)
name_list6.clear()
print(name_list6)

print("===== 修改 =====")
name_list7 = ["唐可可", "南小鸟", "小鸟游六花"]
name_list7[2] = "白"
print(name_list7)

print("===== reversse =====")
name_list8 = ["唐可可", "南小鸟", "小鸟游六花"]
name_list8.reverse()
print(name_list8)

print("===== sort =====")
name_list9 = ["唐可可", "南小鸟", "小鸟游六花"]
name_list9.sort()
print(name_list9)

print("===== in =====")
name_list0 = ["唐可可", "南小鸟", "小鸟游六花"]
print("唐可可" in name_list0)
print("???" in name_list0)

