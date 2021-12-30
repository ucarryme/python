name = '123'
print('标识', id(name), 'sdfda')
print('类型', type(name))
# print("两数之和是"+str(int(input("第一个数是："))+int(input("第二个数是："))))
print(4757//5)
print(2**10)
# 余数 = 被除数 - 除数 * 商
print((-9) % 4)
print(5 >> 1)

print(list(range(2, 100, 5)))
for item in range(100, 999):
    if item == ((item % 10)**3 + (item//10 % 10)**3 + (item//100)**3):
        print(item)

for item in range(3):
    if item == 4:
        print("1")
else:
    print("all error")

lit = ["hello", 5.23, 123, 5.21, 12]
lit2 = list(["hello", 5.23, 12])
print(lit2[1], lit2[-3])
try:
    print(lit.index(12, 1, 4))  #不包括第五个索引
except ValueError:
    print("该值不存在与该范围内")

else:
    print("找到该值位置")

try:
    print(lit[5])
except IndexError:
    print("索引参数出界")
else:
    print("成功输出")

print(lit[:3:])  #this is a new list
print(lit[::-1])  #当索引为具体参数时，取值左开右闭

lit.append("world")
lit.append(lit2)
lit.extend(lit2)
lit.insert(1, "destroy")
print(lit, lit[7][1])
# lit3 = [True, False]
# lit[1:] = lit3    #lit1仍为原list
# print(lit)
lit.remove(5.23)
lit.pop(2)
newList = lit[1:6]
print(lit, newList)
lit[1:3] = []
