#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict, **kwargs):
        super().__init__(clsname, bases, clsdict, **kwargs)
        # _fields = clsdict.get("_fields", [])
        try:
            _fields = cls._fields
        except AttributeError:
            _fields = []
        for i, field in enumerate(_fields):
            setattr(cls, field, property(itemgetter(i)))


class Tuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args, **kwargs):
        if len(args) != len(cls._fields):
            raise TypeError(f"Must supply {len(cls._fields)} args")
        return super().__new__(cls, args)


class Point(Tuple):
    _fields = ["x", "y"]


class Exercise(Tuple):
    _fields = ["exercise_name", "weight", "reps"]


if __name__ == "__main__":
    # p = Point(10, 12, 13)
    p = Point(10, 12)
    print(p.x)
    print(p)
    e = Exercise("Squat", 90.0, 3)
    print(e)
