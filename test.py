#
# import numpy
# def method(a,b=[]):
#     """
#
#     :param a:
#     :return:
#     """
#     #print(a)
#     #return
#     #return a+2
#     b.append(a)
#     return b
# #method()
#
# print(method(1))
# print(method(2))
# print(method(3))
# def func(letter):
#     print(letter)
#     return 1
# func(letter="flower")
def m(a,b):
    # print(a,b)
    print(a)
    print(b)
# 定义一个元组
tuple1=(1,2)
#print(*tuple1)
#元组传参需要加*，可以理解为解压
m(*tuple1)

# 定义字典的两种方式
dict1={"a":1,"b":2}
dict2=dict(a=1,b=2)
# 字典进行传参需要加**，注意字典传参是通过关键字传参的，所以上一条的a如果换成c就会失败
m(**dict1)
m(**dict2)

apple="banana"
print(f"I have an {apple}")

# 默认参数是指定义的时候就给赋予初始值，如果调用的时候不传参，则打印默认值，如果调用的时候传参了，则打印所传的参数
def mmmmm(a="aaaaaa"):
    print(a)
mmmmm()
mmmmm("bbbbb")