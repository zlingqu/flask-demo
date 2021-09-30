class Person:
    name = 'zhangsan'
    def a():
        print('abc')
one = Person()
one.height = 180
print(one.__dict__)
# print(one.name)