# from math import * # НЕ РЕКОМЕНДУЮ
# from math import cos as my_cos # alias = псевдонім
# from payments import do_pay_mono, do_pay_paypal
#
#
# if __name__ == "__main__":
#     do_pay_paypal()
#     do_pay_mono()


from payments import pay_mono


# print([x for x in dir(pay_mono) if not x.startswith("__")])


# lst = [1,2,3]
#
# for i in iter(lst):
#     print(i)
#
# for i in lst:
#     print(i)
#
#
# class MyIterable:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         return MyIterator(self.data)
#
#
# class MyIterator:
#     def __init__(self, data):
#         self.data = data
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         item = self.data[self.index]
#         self.index += 1
#         return item
#
# # Використання
# my_iterable = MyIterable([1, 2, 3, 4])
# for item in my_iterable:
#     print(item)

# it = iter([1,2,3])
#
# next(it) -> 1
# next(it) -> 2
# next(it) -> 3
# next(it) -> StopIteration


# from collections.abc import Iterable, Iterator
#
# print(isinstance([1,2,3], Iterable))
# print(isinstance([1,2,3], Iterator))
# print(isinstance(iter([1,2,3]), Iterator))


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         return False
#
#
# v1 = Vector(1, 2)
# v2 = Vector(1, 2)
#
# print(v1 == v2)


# class SuperList(list):
#
#    def __getitem__(self, item):
#         if len(self) <= item:
#             return super().__getitem__(len(self)-1)
#         if item < 0 and abs(item) > len(self):
#             return super().__getitem__(0)
#         return super().__getitem__(item)
#
#    def __setitem__(self, index, value):
#        if index >= len(self):
#            super().append(value)
#        elif index < 0:
#            super().insert(0, value)
#        else:
#            super().__setitem__(index, value)
#
# s = SuperList([1,2,3])
# print(s[-100])
# print(s[500])
#
# s[100] = 100
# s[-300] = 200
#
# print(s)


def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)]

for multiplier in create_multipliers():
    print(multiplier(2))