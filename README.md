# Python Add-ons
I programmed This Module for python which<br>
add some ability python don`t have<br>
like **Overloading**
## Overloading
the class uses Type Hints for Overloading
sample of Overloading in python

    from addons import Overload

    @Overload # Always Need Type Hint
    def printer(data:str)->None:
        print("String Data:",data)

    @printer.overload # automate overloading using Type Hint
    def printer_int(data:int)->None:
        print("Integer Data:",data)

    @printer.overload_manual(float) # manual function overloading
    def printer_float(data)->None:
        print("Float Data:",data)

    @printer.default
    def printer_default(data)->None:
        print("Other Data:",data)

    printer("123")   # output: String Data: 123
    printer(123)     # output: Integer Data: 123
    printer(12.3)    # output: FLoat Data: 12.3
    printer([1,2,3]) # output: Other Data: [1,2,3]
## Logging
sample of logging in python using **Logger**

    from addons import Logger,DEBUG,INFO,WARNING,ERROR,CRITICAL,UNKNOWN

    logger=Logger(log_level=DEBUG)
    logger.log("This is A Debug Message",DEBUG)
    logger.log("This is A Info Message",INFO)
    logger.log("This is A Warning Message",WARNING)
    logger.log("This is A Error Message",ERROR)
    logger.log("This is A Critical Message",CRITICAL)
    logger.log("This is A Unknown Message",UNKNOWN)

## Thread With Return
sample of creating and getting the Thread return using **ThreadReturn**

    from addons import ThreadReturn

    def pow(x:int,y:int)->int:
        return x**y
    
    thread=ThreadReturn(target=pow,args=(2,16))
    thread.start()
    thread.join()
    print(thread.return_value) # output: 65536
## Creator
**Author**: **Vahab Programmer**<br>
**Github Page**: **[Vahab-Programmer](https://github.com/Vahab-Programmer)**<br>
**Email**: **vahab.goudarzi.2011@gmail.com**<br>
**Telegram**: **[Vahab Programmer Channel](https://t.me/VPPchl)**<br>