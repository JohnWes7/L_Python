import time
import math
from random import randint, randrange
import random


print(random.randint(0, 100))

print(randint(0, 100))
print(math.sqrt(9))
print(math.sqrt(16))

befor = time.time()

for i in range(10):
    time.sleep(1)
    after = time.time()
    #print(after)

print(after-befor)

