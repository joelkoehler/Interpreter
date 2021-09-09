#!/usr/bin/env python
""" generated source for module Environment """
#  (C) 2013 Jim Buffenbarger
#  All rights reserved.
from pl_evalexception import EvalException
from pl_function import Function
from pl_node import NodeSin
from pl_node import NodeCos
from pl_node import NodeTan
from pl_node import NodeAbs
from pl_node import NodeLog
from pl_node import NodeLn
import math

class Environment(object):
    """ generated source for class Environment """

    def __init__(self):
        """ generated source for method __init__ """
        self.map = {}
        self.funcMap = {}

        sinN = NodeSin()
        sinF = Function('meaningless', sinN)
        self.putFunc("sin", sinF)

        cosN = NodeCos()
        cosF = Function('meaningless', cosN)
        self.putFunc("cos", cosF)

        tanN = NodeTan()
        tanF = Function('meaningless', tanN)
        self.putFunc("tan", tanF)

        absN = NodeAbs()
        absF = Function('meaningless', absN)
        self.putFunc("abs", absF)

        logN = NodeLog()
        logF = Function('meaningless', logN)
        self.putFunc("log", logF)

        lnN = NodeLn()
        lnF = Function('meaningless', lnN)
        self.putFunc("ln", lnF)


    def put(self, var, val):
        """ generated source for method put """
        self.map[var] = val
        return val

    def putFunc(self, var, f):
        """ generated source for method put_0 """
        self.funcMap[var] = f
        return f

    def get(self, pos, var):
        """ generated source for method get """
        if var in self.map:
            return self.map[var]
        raise EvalException(pos, "undefined variable: " + var)

    def getFunc(self, pos, var):
        """ generated source for method getFunc """
        if var in self.funcMap:
            return self.funcMap[var]
        raise EvalException(pos, "undefined function: " + var)

    def copy(self):
        """ generated source for method copy """
        newEnv = Environment()
        for var in self.map:
            newEnv.put(var, self.map[var])
        for var in self.funcMap:
            newEnv.putFunc(var, self.funcMap[var])
        return newEnv

