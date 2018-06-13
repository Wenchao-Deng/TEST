import random
import time

names = ['tom','jerry','lucy','wade','james']
passwords = ['abc','123','aaa','bbb','ccc']

name = input('请输入您的用户名...:')

print('接入主机...',end='')
for _x in range(1,10):
    print('..',end= '',flush=True)
    time.sleep(random.uniform(0,1))
print()
print('玩家信息核对...',end='')
for _x in range(1,10):
    print('..',end= '',flush=True)
    time.sleep(0.2)
print()
try:
    idx = names.index(name)
    print(name,'是存在的玩家')
except Exception as e:
    print('尚不存在姓名为%s的玩家' % name)

