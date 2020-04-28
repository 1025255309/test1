# 一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
# 定义一个fight方法：
# final_hp = hp-enemy_power
# enemy_final_hp = enemy_hp - power
# 两个hp进行对比，血量剩余多的人获胜

#定义Game类
class Game:
    # 使用构造函数定义Game类的两个变量hp和power并设置初始值,注意init中的变量需要加上self才能够被其他类调用，申明为实例变量
    def __init__(self):
        self.hp = 1000
        self.power = 200

    # 定义fight方法，并为enemy_hp和enemy_power传参
    def fight(self,enemy_hp,enemy_power):
        final_hp = self.hp-enemy_power
        enemy_final_hp = enemy_hp - self.power
        # 使用判断语句来进行实现“血量剩余多的人获胜”的对比功能
        if final_hp>enemy_final_hp:
            print("我赢了")
        elif final_hp<enemy_final_hp:
            print("我输了，敌人赢了")
        else:
            print("打成平局")
# 对类进行初始化
game=Game()
# 调用类的fight方法，并传两个参数
game.fight(1000,200)
