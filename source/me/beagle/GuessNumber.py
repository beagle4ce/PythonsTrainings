import os # 引入操作系统对象
import random # 引入随机对象

def exitInput(keyword = None):  # 检测退出输入
    if keyword in ["quit","exit"]: # 如果输入的字符属于"quit"或者"exit" 则执行程序推出命令
        os._exit(0) # 程序正常退出返回0 错误退出返回 -1 和C语言类似


def inputNum(promptStr = None): # 创建方法 promptStr = None 表示该参数为不可变参数 类似java的final修饰
    guessNumInput = input(promptStr) # 输入文字
    exitInput(guessNumInput) # 检测退出输入
    while not guessNumInput.isdigit():  # 判断输入的内容是不是数字类型
        print(guessNumInput, "不是数字")  # 上述判断如果不是数字类型则打印该字符并告知不是数字
        guessNumInput = input(promptStr)  # 同时给用户提供新的输入框等待输入
        exitInput(guessNumInput) # 检测退出输入

    return int(guessNumInput)  # 若是数字类型则转换为整数型并压入对象内

# 这是一段函数说明
def initList():
    # 在循环内语句只有一行且有完整方法包裹时可采用这种方式
    # 集合也支持列推导 a = {x for x in 'abracadabra' if x not in 'abc'}
    '''
    # [[row[i] for row in matrix] for i in range(4)]
    [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
    用列推导执行矩阵对置

    # {x: x**2 for x in (2, 4, 6)} 字典也可使用列推导
    {2: 4, 4: 16, 6: 36}
    '''
    return [int((random.random() * 10) + 1) for idx in range(10)]  # 设置10次循环,每次注入0,9的随机数
    # 采用列推导模式Python的蜜糖


def __running__():
    numList = initList()  # 调用初始化
    countor = 0;  # 初始化计数器

    while True:  # 这个就是强制循环来模拟do while,条件写在循环体内
        if countor > len(numList) - 1:  # 计数器从0到N - 1为止,超过了就输出下列文字,并且结束该循环
            print("猜了" + str(countor) + "遍都没猜中,运气是真的差啊")  # 打印提示文字,并加入输入的次数
            break  # 结束整个while循环

        guessNum = inputNum("猜猜数组内的数字:")  # 这里使用自定义方法来获取数字类型参数

        # if not guessNum in numList: # 下列判断的第二种写法
        if guessNum not in numList:  # 判断该对象是否不属于列表内的值
            print(str(guessNum) + " 不是列表里的数字哦")  # 若不属于则打印该数字并提示
            countor += 1  # 同时计数器自增1
            continue  # 并继续从循环头开始执行
        else:  # 若该对象属于列表内的值
            print("猜对了:", str(guessNum))  # 则打印猜对了的值
            break  # 并且终止循环

    print("列表是: ", numList)  # 最后输出随机生成的列表


def __main__(): # 如果要作为入口模块,则必须要 __main__() 方法
    __running__()

if __name__ == '__main__': # __name__ 属性属于系统属性,用来控制当前模块运行的时候谁自动运行,谁被动运行 当'__name__' == '__main__'的时候
    __main__() # 启动方法   GuessNumber.py 模块自己运行的时候启动这个
else:
    pass  # pass是占位符,必须要有else: 块儿,但块儿里不执行任何代码,则使用pass占位符
         # 如果GuessNumber.py是被其它模块引用的则不执行 __main__() 方法
