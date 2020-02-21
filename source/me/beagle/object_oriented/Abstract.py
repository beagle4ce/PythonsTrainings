from abc import ABCMeta,abstractmethod

'''
在Python中没有接口类,因为每个类都可以多继承
所以如果要实现接口类类似的无实现方法,就需要使用abc包里面的ABCMeta类,并且调用abstractmethod注解来标记无实现方法
'''
class Abstract(metaclass=ABCMeta): # 定义接口
    @abstractmethod # 标记该方法为无实现方法, 继承该类的子类强制要求实现该方法, 被标记为@abstractmethod的方法不能在里面编写语句
    def sayHello(self,_name):
        pass # 使用pass占位符占位这个无实现方法