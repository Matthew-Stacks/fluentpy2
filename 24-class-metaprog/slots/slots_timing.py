#!/usr/bin/env python3

class Wrong:

    def __init_subclass__(cls):
        cls.__slots__ = ('x', 'y')


class Klass0(Wrong):
    pass


o = Klass0()
o.z = 3
print('o.z = 3  # did not raise Attribute error because __slots__ was created too late')


class Correct1(type):

    def __new__(cls, cls_name, bases, cls_dict):
        cls_dict['__slots__'] = ('x', 'y')
        return super().__new__(cls, cls_name, bases, cls_dict)


class Klass1(metaclass=Correct1):
    pass

o = Klass1()
try:
    o.z = 3
except AttributeError as e:
    print('Raised as expected:', e)


class Correct2(type):
    def __prepare__(self, bases):
        return dict(__slots__=('x', 'y'))

class Klass2(metaclass=Correct2):
    pass

o = Klass2()
try:
    o.z = 3
except AttributeError as e:
    print('Raised as expected:', e)

