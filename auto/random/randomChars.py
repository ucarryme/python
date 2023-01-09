import random, string
length = 7
num = 200
chars = string.ascii_letters + string.digits
for i in range(num):
 
    s = [random.choice(chars) for i in range(length)]
    with open("./auto/random/rd.txt", 'a+') as fp:
        fp.writelines("{0}\n".format("".join(s)))