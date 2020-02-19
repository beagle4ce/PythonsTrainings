
# 这是一个注释

'''
这是多行注释
可以实现在这个范围内的
多行注释
'''

# 这里开始创建变量(也称为对象) Python是弱类型语言,不需要声明变量类型,直接赋值就好
# 最后由解释器自动推断变量类型,变量在操作过程中有可能导致类型发生变化
string = "这是一个字符串类型用来存放文字"
integer = 10 # 这是数字类型里面的整形
float = 10.334 # 这个代表浮点数,带小数点的
bool = True # 这是布尔型

print(string)
print(string * 2)
print(string[4:6])
print(string[4:])
print(string[:6])
print("测试截取字符串 " + string[:6])
print(integer)
print(float)
print(bool)


strArr = {"这是","一个","无序","字符串","集合"} # 这是一个 set
strArr2 = ["这是","一个","有序","字符串","数组"] # 这是一个list
print(type(strArr)) # 查看该对象类型
print(strArr)
print(type(strArr2)) # 查看该对象类型
print(strArr2)

# 多行语句放在一行写,中间可以用分号隔开
str1 = "打印数字" ; number = 202 ; print(str1) ; print(number)

# 一行多个对象赋值
a,b,c = 1,2,"char"
print(a)
print(b)
print(c)

a=b=c="共同赋值"
print(a)
print(b)
print(c)

# del用于删除某个对象
del c
del a,b
# print(a) 这里会报错,因为已经没有这个对象了  NameError: name 'a' is not defined
# print(b) 这里会报错,因为已经没有这个对象了 NameError: name 'b' is not defined


print('ab\cdef')
print(r'ab\cdef') # 这个功能似乎已经失效了,默认就是带r的状态


word = 'python'
print(word[:2],word[4:])


