import time
import sys

def progress_bar():
  for i in range(1, 101):
    print("\r", end="")
    print("Download progress: {}%: ".format(i), "▋" * (i // 2), end="")
    sys.stdout.flush()
    time.sleep(0.05)

def test1():
    for i in range(5):
        print(i,end='')
        sys.stdout.flush()
        time.sleep(0.5)

def test2():
    s = 'dwaiusdouwaodn'
    print(s,end='')
    for i in range(s.__len__()):
        print(f'\r{s[:len(s)-i-1]}',end='')
        time.sleep(0.5)

def test3():
    s = 'dwasfafawda'
    print(s,end='')
    time.sleep(2)

    print(f'\r{s[:6]}')

def test4():
    s = "no way to escape"
    l = len(s)
    for i in range(l):
        space = '  '
        print(f'\r{space*l}',end='')
        print("\r" + s[:l-1-i] + '|', end="")
        time.sleep(1)

def test5(judge):
    if judge:
        print(judge)
        exit(1)
    
    return judge

if __name__ == '__main__':
    # test3()
    print(test5(True))