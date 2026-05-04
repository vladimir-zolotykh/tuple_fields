#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter


class TupleMeta(type):
    def __init__(cls, clsname, bases, clsdict, **kwargs):
        fields = clsdict.get("fields", [])
        for i, field in enumerate(fields):
            setattr(cls, field, itemgetter(i))


class Tuple(tuple, metaclass=TupleMeta):
    def __new__(cls, *args, **kwargs):
        if len(args) != len(cls.fields):
            raise TypeError(f"Must supply {len(cls.fields)} args")
        return super().__new__(cls, args)


class Point(Tuple):
    fields = ["x", "y"]


class Exercise(Tuple):
    fields = ["exercise_name", "weight", "reps"]


if __name__ == "__main__":
    # p = Point(10, 12, 13)
    p = Point(10, 12)
    print(p)
    e = Exercise("Squat", 90.0, 3)
    print(e)
