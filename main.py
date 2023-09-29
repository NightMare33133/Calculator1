import tkinter
from tkinter import *
import math

class calculator:
    def __init__(self):
        root = Tk()
        root.title("计算器")
        #root.geometry('450x330')#该尺寸可以在底部显示eval实际执行算术式用于调试
        root.geometry('450x290')
        root.resizable(0,0)#锁住尺寸调整

        # root.attributes("-alpha",0.9)
        # root["background"] = "#ffffff"
        font_20 = ("宋体", 20)
        font_16 = ("宋体", 16)
        result_num = tkinter.StringVar()
        result_outer = tkinter.StringVar()
        result_num.set("")
        result_outer.set("")
        # 第一行结果显示
        # 屏幕显示结果
        tkinter.Label(root, font=font_20, height=2, width=30, textvariable=result_outer, justify=tkinter.LEFT,
                      anchor=tkinter.SE).grid(row=1, column=1, columnspan=6)
        # eval函数实际运算代码
        tkinter.Label(root, font=font_20, height=2, width=30, textvariable=result_num, justify=tkinter.LEFT,
                      anchor=tkinter.SE).grid(row=7, column=1, columnspan=6)
        # 第二行按钮布局
        button_clear = tkinter.Button(root, text='C', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")  # relif样式 bg底色
        button_back = tkinter.Button(root, text='←', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_mul = tkinter.Button(root, text='×', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_div = tkinter.Button(root, text='÷', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_sin = tkinter.Button(root, text='sin', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_l_bracket = tkinter.Button(root, text='(', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")

        button_clear.grid(row=2, column=1, padx=4, pady=2)  # pad用于按钮间距
        button_back.grid(row=2, column=2, padx=4, pady=2)
        button_mul.grid(row=2, column=3, padx=4, pady=2)
        button_div.grid(row=2, column=4, padx=4, pady=2)
        button_sin.grid(row=2, column=5, padx=4, pady=2)
        button_l_bracket.grid(row=2, column=6, padx=4, pady=2)
        # 第三行按钮布局
        button_seven = tkinter.Button(root, text='7', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_eight = tkinter.Button(root, text='8', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_nine = tkinter.Button(root, text='9', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_sub = tkinter.Button(root, text='-', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_cos = tkinter.Button(root, text='cos', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_r_bracket = tkinter.Button(root, text=')', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")

        button_seven.grid(row=3, column=1, padx=4, pady=2)
        button_eight.grid(row=3, column=2, padx=4, pady=2)
        button_nine.grid(row=3, column=3, padx=4, pady=2)
        button_sub.grid(row=3, column=4, padx=4, pady=2)
        button_cos.grid(row=3, column=5, padx=4, pady=2)
        button_r_bracket.grid(row=3, column=6, padx=4, pady=2)
        # 第四行按钮布局
        button_four = tkinter.Button(root, text="4", width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_five = tkinter.Button(root, text='5', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_six = tkinter.Button(root, text='6', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_add = tkinter.Button(root, text='+', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_tan = tkinter.Button(root, text='tan', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_log10 = tkinter.Button(root, text='log10', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")

        button_four.grid(row=4, column=1, padx=4, pady=2)
        button_five.grid(row=4, column=2, padx=4, pady=2)
        button_six.grid(row=4, column=3, padx=4, pady=2)
        button_add.grid(row=4, column=4, padx=4, pady=2)
        button_tan.grid(row=4, column=5, padx=4, pady=2)
        button_log10.grid(row=4, column=6, padx=4, pady=2)
        # 第五行按钮布局
        button_one = tkinter.Button(root, text="1", width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_two = tkinter.Button(root, text='2', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_three = tkinter.Button(root, text='3', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_pow = tkinter.Button(root, text='^', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_equal = tkinter.Button(root, text='=', width=5, height=3, font=font_16, relief=tkinter.FLAT, bg="#E799B0")
        button_ln = tkinter.Button(root, text='ln', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")

        button_one.grid(row=5, column=1, padx=4, pady=2)
        button_two.grid(row=5, column=2, padx=4, pady=2)
        button_three.grid(row=5, column=3, padx=4, pady=2)
        button_pow.grid(row=5, column=4, padx=4, pady=2)
        button_equal.grid(row=5, column=5, padx=4, pady=2, rowspan=2)  # rowspan跨行
        button_ln.grid(row=5, column=6, padx=4, pady=2)
        # 第六行按钮布局
        button_zero = tkinter.Button(root, text="0", width=12, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_point = tkinter.Button(root, text='.', width=5, font=font_16, relief=tkinter.FLAT, bg="#FFEBB5")
        button_sqrt = tkinter.Button(root, text='√', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")
        button_π = tkinter.Button(root, text='π', width=5, font=font_16, relief=tkinter.FLAT, bg="#39C5BB")

        button_zero.grid(row=6, column=1, padx=4, pady=2, columnspan=2)
        button_point.grid(row=6, column=3, padx=4, pady=2)
        button_sqrt.grid(row=6, column=4, padx=4, pady=2)
        button_π.grid(row=6, column=6, padx=4, pady=2)

        # 点击事件
        def click_button(x):
            #用于等号清空后同步显示结果
            if result_num.get() == "" and result_outer.get() != "" :
                result_outer.set("")
            old_str = result_num.get()
            if old_str[-1:] == "." and x == ".":#此处还需要优化，可能出现1.1.1这样的情况
                return
            i = ["log",'sqrt', 'sin', 'cos', 'tan','log10','pi']
            if x in i:
                result_num.set(result_num.get() + 'math.' + (str(x)))
            else:
                result_num.set(result_num.get() + (str(x)))

            if x == "**":
                result_outer.set(result_outer.get() + (str("^")))
            elif x == "log":
                result_outer.set(result_outer.get() + (str("ln")))
            elif x == "pi":
                result_outer.set(result_outer.get() + (str("π")))
            else:
                result_outer.set(result_outer.get() + (str(x)))



        def calculation():
            try:
                opt_str = result_num.get()
                result = eval(opt_str)
                result_num.set("")
                result_outer.set(str(result))
            except ZeroDivisionError as e:
                result_num.set("")
                result_outer.set("除数不能为零")
            except SyntaxError:
                result_num.set("")
                result_outer.set("运算结果存在异常")
            except AttributeError:
                result_num.set("")
                result_outer.set("请加上括号")


        def clear():
            result_num.set("")
            result_outer.set("")
        def back():
            old_str = result_num.get()
            old_str2 =result_outer.get()
            i = ['log', 'sqrt', 'sin', 'cos', 'tan']
            j = ['sqrt']
            k = ['**','pi']
            l = ["log10"]
            if old_str[-3:] in i:
                if old_str[-3:] == "log":
                    new_str2 = old_str2.replace(old_str2[-2:], "")
                else:
                    new_str2 = old_str2.replace(old_str2[-3:], "")
                new_str = old_str.replace(old_str[-8:], "")
                result_num.set(new_str)
                result_outer.set(new_str2)

            elif old_str[-4:] in j:
                new_str = old_str.replace(old_str[-9:], "")
                new_str2 = old_str2.replace(old_str2[-4:], "")
                result_num.set(new_str)
                result_outer.set(new_str2)
            elif old_str[-2:] in k:
                if old_str[-2:] == "**":
                    new_str2 = old_str2.replace(old_str2[-1:], "")
                elif old_str[-2:] == "pi":
                    new_str2 = old_str2.replace(old_str2[-1:], "")
                else:
                    new_str2 = old_str2.replace(old_str2[-2:], "")
                new_str = old_str.replace(old_str[-7:], "")
                result_num.set(new_str)
                result_outer.set(new_str2)
            elif old_str[-5:] in l:
                new_str = old_str.replace(old_str[-10:], "")
                new_str2 = old_str2.replace(old_str2[-5:], "")
                result_num.set(new_str)
                result_outer.set(new_str2)
            elif old_str == "":
                pass
            else:
                new_list = list(old_str)
                new_list2 = list(old_str2)
                new_list.pop()
                new_list2.pop()
                new_str = "".join(new_list)
                new_str2 = "".join(new_list2)
                result_num.set(new_str)
                result_outer.set(new_str2)






        button_one.config(command=lambda: click_button("1"))#给函数传递参数的时候用lambda
        button_two.config(command=lambda: click_button("2"))
        button_three.config(command=lambda: click_button("3"))
        button_four.config(command=lambda: click_button("4"))
        button_five.config(command=lambda: click_button("5"))
        button_six.config(command=lambda: click_button("6"))
        button_seven.config(command=lambda: click_button("7"))
        button_eight.config(command=lambda: click_button("8"))
        button_nine.config(command=lambda: click_button("9"))
        button_zero.config(command=lambda: click_button("0"))
        button_add.config(command=lambda: click_button("+"))
        button_sub.config(command=lambda: click_button("-"))
        button_div.config(command=lambda: click_button("/"))
        button_mul.config(command=lambda: click_button("*"))
        button_point.config(command=lambda: click_button("."))

        button_sin.config(command=lambda: click_button("sin"))
        button_cos.config(command=lambda: click_button("cos"))
        button_tan.config(command=lambda: click_button("tan"))
        button_l_bracket.config(command=lambda: click_button("("))
        button_r_bracket.config(command=lambda: click_button(")"))
        button_pow.config(command=lambda: click_button("**"))
        button_sqrt.config(command=lambda: click_button("sqrt"))
        button_log10.config(command=lambda: click_button("log10"))
        button_ln.config(command=lambda: click_button("log"))
        button_π.config(command=lambda: click_button("pi"))

        button_equal.config(command=calculation)
        button_clear.config(command=clear)
        button_back.config(command=back)

        root.mainloop()

if __name__ == '__main__':
    calculator()

