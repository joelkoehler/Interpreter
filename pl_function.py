#!/usr/bin/env python

import math

""" generated source for module Function """
class Function(object):
    """ generated source for class Function """

    def __init__(self, arg, expr):
        """ generated source for method __init__ """
        #print("arg", arg, 'expr', expr)
        self.arg = arg
        self.expr = expr

    def call(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return self.expr.eval(copy)

    def callSin(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return math.sin(x)

    def callCos(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return math.cos(x)

    def callTan(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return math.tan(x)

    def callAbs(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return abs(x)

    def callLog(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return math.log(x)

    def callLn(self, env, x):
        """ generated source for method call """
        copy = env.copy()
        copy.put(self.arg, x)
        return math.log(x)
