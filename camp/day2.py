import random
import time

names = ['tom','jerry','lucy','wade','james']
passwords = ['abc','123','aaa','bbb','ccc']
name = input('请输入您的用户名...:')
print()
password=input('请输入您的密码...:')
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
if name in names :
    idx = names.index(name)
    if passwords[idx]==password:
        print('欢迎来到头号玩家的世界')
    else:
        print('登录失败！')
else:
    print('登录失败！')