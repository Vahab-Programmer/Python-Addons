from datetime import datetime
from sys import stdout,stderr
from os import name
if name == "nt":
    from ctypes import windll,c_uint32,byref
    def enable_ansi(hid:int)->None:
        kernel32 = windll.kernel32
        handle=kernel32.GetStdHandle(hid)
        mode=c_uint32()
        kernel32.GetConsoleMode(handle,byref(mode))
        kernel32.SetConsoleMode(handle,mode.value|0x0004)
    enable_ansi(-10)
    enable_ansi(-11)
    enable_ansi(-12)