class A:
    pass

class B(A):
    pass

print(type(B()) == A) # 判断类型是否相同,严格匹配,不支持子父级匹配
print(isinstance(B(),A)) # 判断子类型是否是父类