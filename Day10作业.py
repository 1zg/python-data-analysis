'''
作业：
下面的代码可以输出”hello”字符，你需要完成对应函数或类的封装

a = a().b.c().d

print(a) # hello

'''
class D:
    d='hello'

class C:
    def c(self):
        return D

class B:
    b=C()

class A:
    def __call__(self, *args, **kwargs):
        return B

a=A()
a = a().b.c().d
print(a)






# class Hello3:
#     d='hello'
#
# class Hello2:
#     def c(self):
#         return Hello3
#
# class Hello1:
#     b=Hello2()
#
# class Hello:
#     def a(self):
#         return Hello1()
#
# a=Hello()
# s=a.a().b.c().d
# print(s)
# # a = a().b.c().d
# # print(a)