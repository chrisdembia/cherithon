"""Error logging."""

import abc

class Log(object):

    __metaclass__ = abc.ABCMeta

    class Priority:
        NULL = 1
        CRITICAL = 2
        ERROR = 3
        WARNING = 4
        STATUS = 5
        DEBUG = 6

    @staticmethod
    def NULL(): return Log.Priority.NULL
    @staticmethod
    def CRITICAL(): return Log.Priority.CRITICAL
    @staticmethod
    def ERROR(): return Log.Priority.ERROR
    @staticmethod
    def WARNING(): return Log.Priority.WARNING
    @staticmethod
    def STATUS(): return Log.Priority.STATUS
    @staticmethod
    def DEBUG(): return Log.Priority.DEBUG

    @staticmethod
    @abc.abstractmethod
    def entry_new(priority, cond, obj=None, func_name=""):
        string = ""
        if obj != None: string += "'" + obj.name + "'."
        if func_name != "": string += func_name + "():"
        string += cond
        print string




