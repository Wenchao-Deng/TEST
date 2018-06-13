import random
import re
import time

names = ['tom','jerry','lucy','wade','james']
passwords = ['abc','123','aaa','bbb','ccc']
blacklist=[]
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
        login()

def update_password(name):
    x = input('是否修改%s用户的密码？(Y/N)' % name)
    if x == 'Y' or x == 'y':
        while True:
            p = input('请输入原密码密码...:')
            pwd = passwords[names.index(name)]
            if p == pwd:
                while True:
                    p1 = input('请输入新密码(密码为6位数字)...:')
                    p2 = input('请再次输入密码(密码为6位数字)...:')
                    if p1==p2:
                        if check_password(p1):
                            passwords[names.index(name)]=p1
                            print('密码修改完毕！')
                            break
                        else:
                            print('密码不符合要求，请重新输入')
                    else:
                        print('两次输入的密码不一致，请重试！')
                break
            else:
                print('原密码错误请重新输入！')
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

def check_password(password):

    if len(password)!=6:return False
    if password.isdigit():
        return True
    else:
        return False

def remove_user(name):
    x = input('是否注销%s用户？(Y/N)' % name)
    if x == 'Y' or x == 'y':
        count = 1
        while count<5:
            try:
                p = input('请输入密码...:')
                pwd = passwords[names.index(name)]
                if p == pwd:
                    del passwords[names.index(name)]
                    names.remove(name)
                    print('%s用户被注销！'% name)
                    break
                else:
                    print('密码错误请重新输入！还可以输入%d次'% (5-count))
                    count+=1
            except Exception as e:
                print('密码输入错误产生异常：',e)
                print('密码错误请重新输入！还可以输入%d次' % (5 - count))
                count += 1

def add_black_list(name):
    x = input('将哪位用户加入黑名单？')
    if x==name:
        print('不允许将自己加入黑名单！')
        return
    else:
        if x in names:
            idx = names.index(x)
            black = (x,passwords[idx])
            blacklist.append(black)
            names.remove(x)
            del passwords[idx]
            print('已将%s用户加入了黑名单'%x)
        else:
            print('该用户不存在！')

    print(blacklist)

def release_black_list():
    print('当前黑名单中的用户为：',blacklist)
    x = input('要将谁移出黑名单：')
    for black in blacklist:
        if x==black[0]:
            b= black
            names.append(black[0])
            passwords.append(black[1])
            blacklist.remove(b)
            break
    else:
        print('该用户不在黑名单中！')
    print(blacklist)
    print(names)





try:
    login()

    add_black_list(current_name)
    release_black_list()
except Exception:
    regist(current_name)
