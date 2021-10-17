print("===== while =====")
i = 0
while i < 10:
    print(i)
    i += 1

print("===== for =====")
for i in range(10):
    print(i)

# test
sum = 0
for i in range(1, 101):
    sum += i
print("sum of [1,100] :", sum)

sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i






    3
print("sum of odd numbers in [1,100] :", sum_odd)

sum_even = 0
for i in range(2, 101, 2):
    sum_even += i
print("sum of even numbers in [1,100] :", sum_even)

for i in range(5):
    for j in range(5):
        print(f"{i} ", end="")
    print()
