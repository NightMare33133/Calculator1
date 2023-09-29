>

[toc]

 

## 作业基本信息...

| 这个作业属于哪个课程 | [2301-计算机学院-软件工程社区-CSDN社区云](https://bbs.csdn.net/forums/ssynkqtd-05) |
| -------------------- | ------------------------------------------------------------ |
| 这个作业要求在哪里   | [软件工程实践第一次作业-CSDN社区](https://bbs.csdn.net/topics/617294583) |
| 这个作业的目标       | 完成一个具有可视化界面的计算器                               |
| 其他参考文献         | [Python制作一个科学计算器_python科学计算器_滑稽研究所的博客-CSDN博客](https://blog.csdn.net/weixin_45067072/article/details/118373399?ops_request_misc=%7B%22request%5Fid%22%3A%22169595584216800227441072%22%2C%22scm%22%3A%2220140713.130102334..%22%7D&request_id=169595584216800227441072&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-2-118373399-null-null.142)[python简单计算器异常处理_python-异常处理try_except-CSDN博客](https://blog.csdn.net/weixin_39972151/article/details/110999151?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_utm_term~default-9-110999151-blog-79569406.235) [tkinter案例_计算器P2逻辑编写_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Ma411x76d/?p=2&spm_id_from=333.880.my_history.page.click&vd_source=4f24f3057448527deda5427be06a7763) |

## Gitcode项目地址[NightMare33133/Calculator1 (github.com)](https://github.com/NightMare33133/Calculator1)

## PSP表格

| PSP                                     |        Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| :-------------------------------------- | --------------------------------------: | :--------------: | ---------------- |
| Planning                                |                                    计划 |        30        | 30               |
| • Estimate                              |              • 估计这个任务需要多少时间 |        15        | 15               |
| Development                             |                                    开发 |       300        | 450              |
| • Analysis                              |            • 需求分析 (包括学习新技术） |        60        | 120              |
| • Design Spec                           |                          • 生成设计文档 |        60        | 60               |
| • Design Review                         |                              • 设计复审 |        20        | 20               |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范) |        10        | 10               |
| • Design                                |                              • 具体设计 |        20        | 20               |
| • Coding                                |                              • 具体编码 |        60        | 60               |
| • Code Review                           |                              • 代码复审 |        10        | 10               |
| • Test                                  |  • 测试（自我测试，修改代码，提交修改） |        40        | 60               |
| Reporting                               |                                    报告 |        40        | 60               |
| • Test Repor                            |                              • 测试报告 |        20        | 30               |
| • Size Measurement                      |                            • 计算工作量 |        20        | 30               |
| • Postmortem & Process Improvement Plan |          • 事后总结, 并提出过程改进计划 |        30        | 40               |
|                                         |                                    合计 |       735        | 1015             |

## 成果展示

四则运算以及相应退格

![](C:\Users\Administrator\Desktop\Calculator\四则运算以及退格.gif)

科学计算以及相应退格

![科学计算以及相应退格](C:\Users\Administrator\Desktop\Calculator\科学计算以及相应退格.gif)

异常情况报错

![](C:\Users\Administrator\Desktop\Calculator\异常情况报错.gif)

## 解题思路描述

### 问题1

**功能：具有基本功能的计算器**

实现加、减、乘、除、归零基本操作。

### 问题2

**附加功能：具有科学计算的计算器**

实现次方、幂、三角函数等操作。

先通过CSDN和B站了解制作一个可视化计算器可以选择的环境和相应的库

在查询资料后，选择使用Python的tkinter库完成本次作业

先通过视频教程和文档教程学习了tkinter各函数的使用，以及了解实现可视化计算器所需要调用的相应函数。

先通过教程相关的实例学习如何实现了具备基础功能的计算器，再通过细致化的资料查询了解实现科学计算器的所需要学习到的相关知识





## 接口设计和实现过程

定义了多个函数接口用于实现可视化计算器中视图控件触发具体功能的实现

接口click_button用于点击按钮后将对应的参数显示在最上方的屏幕

接口calculation()用于触发等号按钮

接口clear()用于触发C按钮

接口back()用于触发退格按钮

 以下代码为各按钮与接口函数的绑定

```
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
```

本次的代码的实现过程是先完成代码的UI界面以及相应按钮进行绑定后，接着通过依次实现按钮对应功能，把具体表达式输出到上方屏幕，其中的四则运算主要以来eval函数识别表达式后再将结果输出到屏幕，后续的科学计算器则是通过调用math库的相应函数来进行算术表达式的计算



## 关键代码展示

 以下为可视化窗口的初始化以及部分按钮界面设置的部分相关代码

```
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
```

点击按钮后将对应的字符输入到上方屏幕，在用户界面所显示字符与eval函数中所执行的代码具有差异，为了便于用户理解，分别使用不同的字符串变量result_num，result_outer存取表达式，将更易懂的表达式呈现在界面。

```
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
```

 

```
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
```



## 性能改进

对比windows自带的计算机后发现触发等号运行出结果以后，点击任意键位就会开始新一轮的运算，但原先抛出结果后，甚至可以通过退格键删改报错提示

因此在calculation函数的代码中，在运行等号运算时，将eval实际执行的表达式清空

```
def calculation():
    try:
        opt_str = result_num.get()
        result = eval(opt_str)
        result_num.set("")
        result_outer.set(str(result))
```

在click_button（）的函数中的开头增加以下代码

```
if result_num.get() == "" and result_outer.get() != "" :
    result_outer.set("")
```

该代码在识别到result_num字符串为空时，可以直接将result_outer同时置空



将原先杂乱的代码整理好后，分成了计算器类和测试类，以便于后续的调试和调用

```
class calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("计算器")
        #root.geometry('450x330')#该尺寸可以在底部显示eval实际执行算术式用于调试
        self.root.geometry('450x290')
        self.root.resizable(0,0)#锁住尺寸调整
```

```
class Test(unittest.TestCase):
    def test1(self):
        root = Tk()
        c = calculator(root)
        result_num.set("5+1")
        result = c.calculation()
        self.assertEqual(result, '6',"test1 fail")
```

 

## 单元测试

 单元测试分别测试了四则运算，科学计算，π的调用，以及除0情况的报错![单元测试](C:\Users\Administrator\Desktop\Calculator\单元测试.png)

| 输入表达式 | 运行结果           |
| ---------- | ------------------ |
| 5+1        | 6                  |
| sin(1)     | 0.8414709848078965 |
| log10(10)  | 1.0                |
| π          | 3.141592653589793  |
| 10/0       | 除数不能为零       |

```
class Test(unittest.TestCase):
    def test1(self):
        root = Tk()
        c = calculator(root)
        result_num.set("5+1")
        result = c.calculation()
        self.assertEqual(result, '6',"test1 fail")
```

 

## 异常处理

 常见的报错一般出现于除数为0的情况，以及使用科学计算时未加上括号，还有连续使用”+“，”-“等异常表达式出现的报错，成果展示中的gif图有展示以下三种异常情况的触发

```
except ZeroDivisionError as e:
    result_num.set("")
    result_outer.set("除数不能为零")
except SyntaxError:
    result_num.set("")
    result_outer.set("运算结果存在异常")
except AttributeError:
    result_num.set("")
    result_outer.set("请加上括号")
```



 

## 心得体会

 通过本次的作业感受到了，从一片空白的代码文档中开始构建一个完整的项目是与以往的PTA类的做题完全不同，相当的考验我们的信息检索能力，以及学习能力，需要临时学习许多从未接触过的知识，并且需要不断的报错中寻找解决的途径，最终优化出更好的项目，虽然还存在有很多不足，但是我会想办法优化得更好的。
