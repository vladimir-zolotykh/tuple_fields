#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from operator import itemgetter


class Point(tuple):
    def __new__(cls, *args):
        assert len(args) == 2
        return super().__new__(cls, args)

    def getx(self):
        return self[0]

    def gety(self):
        return self[1]

    x = property(getx)
    y = property(gety)
    z = property(itemgetter(0))
    w = itemgetter(0)


# >>> p.w
# operator.itemgetter(0)
