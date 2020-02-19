a = 2
b = 4

print("a ** b = ",a ** b) # 幂计算(指数计算) 优先级最高
print("a * b = ",a * b) # 优先级其次
print("a / b = ",a / b) # 优先级其次
print("a // b = ",a // b) # 只保留整数的除法  优先级其次
print("a % b = ",a % b) # 模除(取余数)   优先级其次
print("a + b = ",a + b) # 优先级相对较低
print("a - b = ",a - b) # 优先级相对较低


# 下列操作是 计算并赋值 a += b 其实等于 a = a + b
# a /= b其实等于 a = a / b
a **= b
print("a **= b : ", a)
a *= b
print("a *= b : ", a)
a /= b
print("a /= b : ", a)
a //= b
print("a //= b : ", a)
a %= b
print("a %= b : ", a)
a += b
print("a += b : ", a)
a -= b
print("a -= b : ", a)