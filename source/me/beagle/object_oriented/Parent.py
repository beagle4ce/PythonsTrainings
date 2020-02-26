from me.beagle.object_oriented.Person import Person # 命名空间一定要像这样写全包含到文件名为止,否则会出现 'typeerror module() takes at most 2 arguments (3 given)'错误
from me.beagle.object_oriented.Gender import Gender # 千万不能这样写 from me.beagle.object_oriented import Gender
from me.beagle.object_oriented.Abstract import Abstract # 这里是含有抽象方法的继承抽象类基类的自定义抽象类
import logging

# __私有变量/对象       __protectObject
# _受保护的变量/对象     _name
# __系统级别的方法__     __name__
# _受保护的方法()        _protectMethod()
# __私有方法()           __privateMethod()
# __系统方法__()         __init__()

class Parent(Person,Abstract):
    # __private_status = "Private field"
    # public_field = "Public field"
    address = ""
    role = ""

    @classmethod # 使该方法能够成为初始化该类的方法
    def init_other__(self):
        return Parent()

    # Python不需要重载方法，如果有可变参数，则使用下列形式制作方法即可
    # 使用带默认值的参数就可以在使用该方法时进行可变长度传入参数
    def __init__(self, name="", age=0, gender="", address="", role=""): # 带有父类参数的全参构造函数
        super(Parent, self).__init__(name, age, gender) # 使用super方法可以引入构造父类,然后实用父类的方法
        self.address = address
        self.role = role

    # 如果一个方法内含有带默认值和不带默认值的参数，
    # 则不带默认值的参数一定要放在 带默认值参数的前面，否则会报语法错误
    def sayHello(self, name, age=0):
        print(str(name) + "说到: Hello,world!")
        if age > 0 :
            print("我" + str(age) + "岁")


def __main__(*args):
    p2 = Parent.init_other__()
    p2.sayHello("hh")
    p1 = Parent()
    p = Parent("Name", 38, Gender.male, "Address", "Father")
    p.sayHello(input("怎么称呼?: "), int(input("年龄？：")))
    print([p.name, p.age, p.gender.name, p.address, p.role])

if __name__ == '__main__':
    __main__()
else:
    pass