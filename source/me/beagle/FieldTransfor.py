
def method(inputStr):
    while not inputStr.isdigit():
        print("Err not digital!", inputStr)
        inputStr = input("Input something:") # 这里并没有把inputStr对象传递出去,而Python默认每个对象都是终态,不可被改变,只能被重新赋值
    return int(inputStr)


while True:
    inputStr = input("Input something:")
    inputNum = method(inputStr)
    print("inputStr", inputStr)
    print("inputNum", inputNum)

