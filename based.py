# list.sort()对其排序，reverse=True倒排
# 形参*a是一个元组，**a是一个dict
# 类的初始化函数,调用父类的初始化函数,类的实例也可以作为另一个类的属性
class Animal():
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Dog(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def run(self):
        print(self.name+" run")

# 异常处理
try:
    answer = int(input()) / int(input())
except ZeroDivisionError:
    print('can`t divide 0')
else:
    print(answer)

# json文件 同样的数据格式共享
# json.dump()
# json.load()

# 模块测试
import unittest
unittest.TestCase.assertEquals()
unittest.main()