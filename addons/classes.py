from .imports import stdout,stderr,datetime,Thread
DEBUG=1
INFO=2
WARNING=3
ERROR=4
CRITICAL=5
UNKNOWN=6
class Overload:
    def __init__(self,function):
        self.__funcmap={}
        self.__default=function
        self.__return_function=True
        self.overload(function)
    def overload(self,function):
        args = function.__annotations__.copy()
        args.pop("return",None)
        args = tuple(args.values())
        self.__funcmap[args] = function
        return function if self.__return_function else None
    def overload_manual(self,*args):
        args=tuple([arg.__class__ if type(arg) != type else arg for arg in args])
        funcmap=self.__funcmap
        return_function=self.__return_function
        def wrapper(function):
            funcmap[args]=function
            return function if return_function else None
        return wrapper
    def default(self,function)->None:self.__default=function
    def __call__(self, *args, **kwargs) -> any:
        arg = [type(a) for a in args] + [type(k) for k in kwargs.values()]
        func = self.__funcmap.get(tuple(arg), self.__default)
        return func(*args, **kwargs) if func else None
    def return_function(self,status:bool)->None:self.__return_function=status
class SpecialAscii:
    reset = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"
    invert = "\033[7m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    bg_black = "\033[40m"
    bg_red = "\033[41m"
    bg_green = "\033[42m"
    bg_yellow = "\033[43m"
    bg_blue = "\033[44m"
    bg_purple = "\033[45m"
    bg_cyan = "\033[46m"
    bg_white = "\033[47m"
    bright_black = "\033[90m"
    bright_red = "\033[91m"
    bright_green = "\033[92m"
    bright_yellow = "\033[93m"
    bright_blue = "\033[94m"
    bright_purple = "\033[95m"
    bright_cyan = "\033[96m"
    bright_white = "\033[97m"
    bg_bright_black = "\033[100m"
    bg_bright_red = "\033[101m"
    bg_bright_green = "\033[102m"
    bg_bright_yellow = "\033[103m"
    bg_bright_blue = "\033[104m"
    bg_bright_purple = "\033[105m"
    bg_bright_cyan = "\033[106m"
    bg_bright_white = "\033[107m"
class Logger:
    colorized={DEBUG:SpecialAscii.bright_cyan+"DEBUG"+SpecialAscii.reset,INFO:SpecialAscii.bright_green+"INFO"+SpecialAscii.reset,WARNING:SpecialAscii.bright_yellow+"WARNING"+SpecialAscii.reset,ERROR:SpecialAscii.red+"ERROR"+SpecialAscii.reset,CRITICAL:SpecialAscii.bright_white+SpecialAscii.bg_red+"CRITICAL"+SpecialAscii.reset,UNKNOWN:SpecialAscii.white + SpecialAscii.bg_purple+"UNKNOWN"+SpecialAscii.reset}
    non_colorized={DEBUG:"DEBUG",INFO:"INFO",WARNING:"WARNING",ERROR:"ERROR",CRITICAL:"CRITICAL",UNKNOWN:"UNKNOWN"}
    def __init__(self,name:str,log_level:int=INFO,color:bool=True,std_out=stdout,std_err=stderr):
        self.__name=name
        self.__textmap=self.colorized if color else self.non_colorized
        self.__level=log_level
        self.__stdout=std_out
        self.__stderr=std_err
    def log(self,message:str,level:int)->None:
        if level <self.__level:return
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        level_msg=self.__textmap.get(level)
        if not level_msg:level_msg=self.__textmap.get(UNKNOWN)
        print("[{}] [{}] {}: {}".format(time,level_msg,self.__name,message),file=self.__stdout if level <=WARNING else self.__stderr)
class ThreadReturn(Thread):
    def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group,target=target,name=name,args=args,kwargs=kwargs,daemon=daemon)
        self.return_value=None
        self._target=self.__runner
        self.__target=target
    def __runner(self,*args,**kwargs)->None:self.return_value=self.__target(*args,**kwargs)