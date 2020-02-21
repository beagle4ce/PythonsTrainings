from me.beagle.object_oriented.Person import Person # 命名空间一定要像这样写全包含到文件名为止,否则会出现 'typeerror module() takes at most 2 arguments (3 given)'错误
from me.beagle.object_oriented.Gender import Gender # 千万不能这样写 from me.beagle.object_oriented import Gender
from me.beagle.object_oriented.Abstract import Abstract

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

    def __init__(self, name, age, gender, address, role): # 带有父类参数的全参构造函数
        super(Parent, self).__init__(name, age, gender) # 使用super方法可以引入构造父类,然后实用父类的方法
        self.address = address
        self.role = role

    def sayHello(self, name):
        print(str(name) + "说到: Hello,world!")


def __main__(*args):
    p = Parent("Name", 38, Gender.male, "Address", "Father")
    p.sayHello(input("怎么称呼?: "))
    print([p.name, p.age, p.gender.name, p.address, p.role])

if __name__ == '__main__':
    __main__()
else:
    pass