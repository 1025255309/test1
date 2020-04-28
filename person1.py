
class Person():
    # 公共的属性
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    # 定义一个方法，私有属性
    def set_att(self,value):
        self.value=value

    def eat(self):
        print(f"name: {self.name},age:{self.age},gender:{self.gender} 我最爱吃饭")

    def drink(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender} 我最爱喝水")

    def run(self):
        print(f"name: {self.name}, age: {self.age}, gender: {self.gender} 我最爱跑步")

xiaoming = Person("xiaoming",12,"male")
xiaohong = Person("xiaohong",20,"female")
print(xiaoming.name)
xiaoming.eat()

print(xiaohong.name)
xiaohong.run()
print(xiaohong.age)

xiaohong.set_att("fit")
print(xiaohong.value)

