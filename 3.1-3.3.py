#3.1列表
name = ['sun','wang','li','liu']
print(name[0],name[1],name[2],name[3],name[-1])

#3.2
print(f'我是{name[0]}')
print(f'我是{name[1]}')
print(f'我是{name[2]}')
print(f'我是{name[3]}')

#3.4
old_man = ['张三','李四','王五']
print(f'我想邀请{old_man[0]}吃饭')

#3.5
print(f'因为{old_man[1]}缺席')
old_man[1] = '老六'
print(f'现在邀请{old_man[1]}来')

#3.6
old_man.insert(0,'老大')
old_man.insert(2,"老三")
old_man.append("老小")
print(old_man)

#3.7
print("只能来两个人")
new_man = old_man.pop()
print(old_man)
new_man = old_man.pop()
print(old_man)
new_man = old_man.pop()
print(old_man)
new_man = old_man.pop()
print(old_man)

print(f'欢迎{old_man[0]}的到来')
print(f'欢迎{old_man[1]}的到来')

old_man.remove('张三')
old_man.remove('老大')
print(old_man)