from random import randint

while True:
    num = randint(0, 100)
    print(num)
    if num == 66:
        break

print("====================================")

count = 0
for i in range(0, 101):
    if i % 6 == 0:
        continue

    print(i, end="\t")
    count += 1
    if count % 10 == 0:
        print()
else:
    print("\n======== done =========")