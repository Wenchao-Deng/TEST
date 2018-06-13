import random
import time

names = ['tom','123']
name = input('请输入您的用户名...:')
password=input('请输入您的密码...:')
print('接入主机......')
time.sleep(2)
print('玩家信息核对...')
if name ==names[0] and password==names[1]:
    print('欢迎来到头号玩家的世界')
else:
    print('登录失败！')
