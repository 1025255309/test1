# 定义一个人类
class Person():
    # 定义人类的一个name属性
    name="小果果"
    # 定义一个get_name方法，方法是指定义在类中的函数，自带self参数
    def get_name(self):
        return self.name
#实例化类就是在类后面加（），然后加上一个变量的名字，通过这个变量的名字p就可以调用类的属性和方法了
p=Person()
print(p.name)
print(p.get_name())
#也可以不实例化，直接调用类的名字再调用它的属性
print(Person.name)

# 修改实例的属性,类的属性不受影响
p.name="花花"
print(p.name)
print(Person.name)
# 如果实例的属性不修改，只修改类的属性，实例的属性也会跟着修改；如果修改实例的属性，则修改类的属性只能修改类的属性，影响不到实例的属性了
Person.name="jerry"
print(Person.name)
print(p.name)