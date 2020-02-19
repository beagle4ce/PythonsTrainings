set1 = {'abc','def','ghi','ghi'}
print(set1)
set2 = set({'abc1','def1','ghi1','ghi1'})  # 创建空集合需要用set() 因为空{} 是用来创建空字典的
print(set2)
list1 = ['list1','list2','list3']
print(list1)
list2 = list(['list1','list2','list3'])
print(list2)
list3 = list(set2)
print(list3)
tuple1 = ('tuple1','tuple2','tuple3')
print(tuple1)
tuple2 = tuple(('tuple1','tuple2','tuple3'))
print(tuple2)
tuple3 = tuple(list2)
print(tuple3)


print(list1[0])
print(list1[-1])
print(list1[0:-3])
print(list1 + list2)

print(tuple1[0])
print(tuple1[-1])
print(tuple1[0:-1])
print(tuple1 + tuple2)



# set 集合用法
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素