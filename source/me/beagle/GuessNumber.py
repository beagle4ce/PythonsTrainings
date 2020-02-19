import random # 引入随机对象

def inputNum(promptStr = None): # 创建方法 promptStr = None 表示该参数为不可变参数 类似java的final修饰
    guessNumInput = input(promptStr) # 输入文字
    while not guessNumInput.isdigit():  # 判断输入的内容是不是数字类型
        print(guessNumInput, "不是数字")  # 上述判断如果不是数字类型则打印该字符并告知不是数字
        guessNumInput = input(promptStr)  # 同时给用户提供新的输入框等待输入

    return int(guessNumInput)  # 若是数字类型则转换为整数型并压入对象内


numList = list() # 初始化列表
for idx in range(10): # 设置10次循环
    numList.append(int(random.random() * 10)) # 随机抽取0-10的数压入列表


countor = 0; # 初始化计数器

while True: # 这个就是强制循环来模拟do while,条件写在循环体内

    if countor > 9: # 计数器从0到9为止,超过了就输出下列文字,并且结束该循环
        print("猜了" + str(countor) + "遍都没猜中,运气是真的差啊") # 打印提示文字,并加入输入的次数
        break # 结束整个while循环

    guessNum = inputNum("猜猜数组内的数字:") # 这里使用自定义方法来获取数字类型参数

    # if not guessNum in numList: # 下列判断的第二种写法
    if guessNum not in numList: # 判断该对象是否不属于列表内的值
        print(str(guessNum) + " 不是列表里的数字哦") # 若不属于则打印该数字并提示
        countor += 1 # 同时计数器自增1
        continue # 并继续从循环头开始执行
    else: # 若该对象属于列表内的值
        print("猜对了:", str(guessNum)) # 则打印猜对了的值
        break # 并且终止循环

print("列表是: ",numList) # 最后输出随机生成的列表

