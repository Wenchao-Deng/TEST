import random
import time

names = ['tom','jerry','lucy','wade','james']
passwords = ['abc','123','aaa','bbb','ccc']
current_name=None

def regist(name):
    x = input('是否注册%s为新用户？(Y/N)'% name)
    if x=='Y' or x=='y':
        while True:
            p1 = input('请输入密码...:')
            p2 = input('请再次输入密码...:')
            if p1==p2:
                names.append(name)
                passwords.append(p1)
                print('新用户注册完毕！')
                break
            else:print('两次密码输入不一致，请重新输入')

        print(names)
        print(passwords)
        login()

def login():
    global current_name
    name = input('请输入您的用户名...:')
    password = input('请输入您的密码...:')
    print('接入主机...', end='')
    for _x in range(1, 10):
        print('..', end='', flush=True)
        time.sleep(random.uniform(0, 1))
    print()
    print('玩家信息核对...', end='')
    for _x in range(1, 10):
        print('..', end='', flush=True)
        time.sleep(0.2)
    print()
    if name in names:
        idx = names.index(name)
        if passwords[idx] == password:
            print('欢迎来到头号玩家的世界')
            current_name=name
        else:
            print('登录失败！')
            current_name = None
    else:
        print('该用户不存在！')
        current_name=name
        raise Exception('用户不存在')

try:
    login()
except Exception:
    regist(current_name)


