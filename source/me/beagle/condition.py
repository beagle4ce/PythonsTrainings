import sys
import random

source = input("请输入数字:")

countor = 0;
while not source.isdigit():
    print("输入的不是数字")
    countor += 1; # 步进1
    if countor > 2:
        sys.exit("exit")
    source = input("请输入数字:")

num = int(source)

if num > 0 and num < 20:
    print("数字小于20")
elif num > 20 and num < 30:
    print("数字在20和30之间")
else:
    print("数字大于30")







