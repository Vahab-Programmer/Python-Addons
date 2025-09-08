# Python Add-ons
I programmed This Module for python which<br>
add some ability python don`t have<br>
like **Overriding**
## Overriding
the class uses Type Hints for Overriding
sample of Overriding in python

    from addons import Override

    @Override # Always Need Type Hint
    def printer(data:str)->None:
        print("String Data:",data)

    @printer.override # automate overriding using Type Hint
    def printer_int(data:int)->None:
        print("Integer Data:",data)

    @printer.override_manual(float)
    def printer_float(data)->None:
        print("Float Data:",data)

    @printer.default
    def printer_default(data)->None:
        print("Other Data:",data)

    printer("123")   # output: String Data: 123
    printer(123)     # output: Integer Data: 123
    printer(12.3)    # output: FLoat Data: 12.3
    printer([1,2,3]) # output: Other Data: [1,2,3]
## Creator
**Author**: **Vahab Programmer**<br>
**Github Page**: **[Vahab-Programmer](https://github.com/Vahab-Programmer)**<br>
**Email**: **vahab.goudarzi.2011@gmail.com**<br>
**Telegram**: **[Vahab Programmer Channel](https://t.me/VPPchl)**<br>