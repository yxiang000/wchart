import tkinter
import math
import tkinter.messagebox


class jsp:
    #界面布局方法
    #定义初始化方法
    def __init__(self):

        #创建主界面，并且保存到成员属性中
        self.root = tkinter.Tk()
        self.root.minsize(320, 440)
        self.root.maxsize(320, 475)
        self.root.resizable(False, False)
        self.root.title('Just Do IT')
        #设置显示面板的变量
        self.result = tkinter.StringVar()
        self.result.set(0)
        self.aa = tkinter.StringVar()
        self.aa.set('')
        #设置一个全局变量  运算数字和符号的列表
        self.lists = []
        #添加一个用于判断是否按下运算符号的标志
        self.isPressSign = False
        #界面布局
        self.layout()
        #下拉菜单
        self.pulldown_menu()
        # 循环显示
        self.root.mainloop()

    #界面组建摆放
    def layout(self):


        # 显示框

        text = tkinter.Label(self.root, textvariable=self.result, bg='white', fg='black', bd=3, font=('黑体', 12, 'bold'),anchor='e')
        text.place(x=30, y=20, height=40, width=260)

        #显示计算过程的显示框
        entrys = tkinter.Label(self.root, textvariable=self.aa, bg='white', fg='black', bd=3, font=('黑体', 12, 'bold'), anchor='e')
        entrys.place(x=30, y=50, height=20, width=260)
        # 功能键  第一行
        btn1 = tkinter.Button(self.root, text='MC', bg='gray', fg='black', bd=3,command = self.press_MC)
        btn1.place(x=20, y=80, height=40, width=40)
        btn2 = tkinter.Button(self.root, text='MR', bg='gray', fg='black', bd=3,command = self.press_MR)
        btn2.place(x=80, y=80, height=40, width=40)
        btn3 = tkinter.Button(self.root, text='MS', bg='gray', fg='black', bd=3,command = self.press_MS)
        btn3.place(x=140, y=80, height=40, width=40)
        btn4 = tkinter.Button(self.root, text='M+', bg='gray', fg='black', bd=3,command = self.press_MAdd)
        btn4.place(x=200, y=80, height=40, width=40)
        btn5 = tkinter.Button(self.root, text='M-', bg='gray', fg='black', bd=3,command = self.press_MSub)
        btn5.place(x=260, y=80, height=40, width=40)

        # 功能键 第二行
        btn_del = tkinter.Button(self.root, text='<--', bg='gray', fg='black', bd=3, command=self.pressDel)
        btn_del.place(x=20, y=140, height=40, width=40)
        btn6 = tkinter.Button(self.root, text='CE', bg='gray', fg='black', bd=3, command=self.pressDelete)
        btn6.place(x=80, y=140, height=40, width=40)
        btn_c = tkinter.Button(self.root, text='C', bg='gray', fg='black', bd=3, command=self.pressClear)
        btn_c.place(x=140, y=140, height=40, width=40)
        btnzhengfu = tkinter.Button(self.root, text='+/-', bg='gray', fg='black', bd=3, command=self.zhengFu)
        btnzhengfu.place(x=200, y=140, height=40, width=40)
        btn6 = tkinter.Button(self.root, text='√', bg='gray', fg='black', bd=3, command=self.numSqrt)
        btn6.place(x=260, y=140, height=40, width=40)

        # 数字键  7 8 9 / %
        num7 = tkinter.Button(self.root, text='7', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('7'))
        num7.place(x=20, y=200, height=40, width=40)
        num8 = tkinter.Button(self.root, text='8', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('8'))
        num8.place(x=80, y=200, height=40, width=40)
        num9 = tkinter.Button(self.root, text='9', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('9'))
        num9.place(x=140, y=200, height=40, width=40)
        num_chu = tkinter.Button(self.root, text='/', bg='gray', fg='black', bd=3, command=lambda: self.pressComputer('/'))
        num_chu.place(x=200, y=200, height=40, width=40)
        num_quyu = tkinter.Button(self.root, text='%', bg='gray', fg='black', bd=3, command= lambda: self.pressComputer('%'))
        num_quyu.place(x=260, y=200, height=40, width=40)

        # 数字键  4 5 6 * 1/x
        num4 = tkinter.Button(self.root, text='4', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('4'))
        num4.place(x=20, y=260, height=40, width=40)
        num5 = tkinter.Button(self.root, text='5', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('5'))
        num5.place(x=80, y=260, height=40, width=40)
        num6 = tkinter.Button(self.root, text='6', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('6'))
        num6.place(x=140, y=260, height=40, width=40)
        num_cheng = tkinter.Button(self.root, text='*', bg='gray', fg='black', bd=3, command=lambda: self.pressComputer('*'))
        num_cheng.place(x=200, y=260, height=40, width=40)
        num_ = tkinter.Button(self.root, text='1/x', bg='gray', fg='black', bd=3,command  = self.grade)
        num_.place(x=260, y=260, height=40, width=40)

        # 数字键  1 2 3 - =
        num1 = tkinter.Button(self.root, text='1', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('1'))
        num1.place(x=20, y=320, height=40, width=40)
        num2 = tkinter.Button(self.root, text='2', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('2'))
        num2.place(x=80, y=320, height=40, width=40)
        num3 = tkinter.Button(self.root, text='3', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('3'))
        num3.place(x=140, y=320, height=40, width=40)
        num_jian = tkinter.Button(self.root, text='-', bg='gray', fg='black', bd=3, command=lambda: self.pressComputer('-'))
        num_jian.place(x=200, y=320, height=40, width=40)
        num_eq = tkinter.Button(self.root, text='=', bg='gray', fg='black', bd=3, command=lambda: self.pressEqual())
        num_eq.place(x=260, y=320, height=100, width=40)

        # 最后按键
        num0 = tkinter.Button(self.root, text='0', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('0'))
        num0.place(x=20, y=380, height=40, width=100)
        num_p = tkinter.Button(self.root, text='.', bg='gray', fg='black', bd=3, command=lambda: self.pressNum('.'))
        num_p.place(x=140, y=380, height=40, width=40)
        num_add = tkinter.Button(self.root, text='+', bg='gray', fg='black', bd=3, command=lambda: self.pressComputer('+'))
        num_add.place(x=200, y=380, height=40, width=40)

    #定义下拉菜单
    def pulldown_menu(self):
        # 创建总菜单
        menubar = tkinter.Menu(self.root)
        # 创建 查看 下拉菜单 ，并加入总菜单
        findmenu = tkinter.Menu(menubar, tearoff=0)
        # 创建 编辑 下拉菜单 并加入总菜单
        modifmenu = tkinter.Menu(menubar, tearoff=0)
        # 创建  帮助 下拉菜单  并加入总菜单
        helpmenu = tkinter.Menu(menubar, tearoff=0)

        # 增加紫菜单  查看
        # findmenu.add_separator()
        findmenu.add_command(label='标准',command = self.standard)
        findmenu.add_command(label='科学型',command = self.science)
        findmenu.add_command(label = '程序员',command = self.programmer)
        findmenu.add_command(label = '统计信息',command = self.statinfo)

        findmenu.add_command(label='程序员')
        # 增加子菜单  编辑
        # findmenu.add_separator()
        modifmenu.add_command(label='复制',command = self.nono)

        modifmenu.add_command(label='粘贴',command = self.nono)
        modifmenu.add_command(label='历史记录',command = self.nono)
        # 增加子菜单  帮助
        helpmenu.add_command(label='查看帮助',command = self.nono)

        helpmenu.add_command(label='关于计算器')

        # 添加总菜单显示
        menubar.add_cascade(label='查看', menu=findmenu)
        menubar.add_cascade(label='编辑', menu=modifmenu)
        menubar.add_cascade(label='帮助', menu=helpmenu)

        # 显示总菜单
        self.root.config(menu=menubar)


    def standard(self):
        tkinter.messagebox.showinfo('', '别乱点啦  你用的就是标准型～→_→')
    def science(self):
        tkinter.messagebox.showinfo('', '假装这里是科学型计算器～╰(*´︶`*)╯')
    def programmer(self):
        tkinter.messagebox.showinfo('', '假装这里是程序员计算器～╰(*´︶`*)╯')
    def statinfo(self):
        tkinter.messagebox.showinfo('', '放弃吧！没啥可统计的～(;¬_¬)')
    def helpview(self):
        tkinter.messagebox.showinfo('', '不想帮助你～→_→')
    def aboutcc(self):
        tkinter.messagebox.showinfo('', '程序员回家种田了 不再更新！！！')
    def nono(self):
        tkinter.messagebox.showinfo('','太多了 不想写了～=_=')





    #定义获取数字方法
    def pressNum(self,num):
        # 判断是否按下了运算符号
        if self.isPressSign == False:
            pass
        else:
            self.result.set(0)
            isPressSign = False

        # 获取面板中的原有数字
        oldnum = self.result.get()
        # 判断是否位0
        if oldnum == '0':
            self.result.set(num)
        else:
            # 链接新按下的数字
            newnum = oldnum + num
            # 将按下的数字写到面板中
            self.result.set(newnum)
    #定义运算方法
    #运算函数
    def pressComputer(self,sign):

        # 保存已经按下的数字和运算符号

        if self.isPressSign == True:
            self.lists.pop()
        else:
            # 获取界面数字
            num = self.result.get()
            self.lists.append(num)

        # 保存按下的操作符号
        self.lists.append(sign)
        # 设置运算符号为按下状态)
        self.isPressSign = True



    #获取运算结果
    def pressEqual(self):
        # 获取所有的类表中的内容以及获取当前界面的数字
        curnum = self.result.get()
        self.lists.append(curnum)
        # 将列表转为字符串
        computeStr = ''.join(self.lists)
        endNum = eval(computeStr)
        # 将运算过程放在显示界面
        self.aa.set(computeStr)
        # 将运算结果显示在界面
        self.result.set(endNum)

        # 清空运算列表
        self.lists.clear()

    #制作 C 归零按键
    def pressClear(self):
        self.lists.clear()
        self.result.set(0)
        self.aa.set('')
    #制作 CE 删除当前数值
    def pressDelete(self):
        self.a = self.result.get()
        self.lists.append(self.a)
        self.lists.pop(-1)
        self.result.set('')
    #制作 <-- 删除按键
    def pressDel(self):
        self.a = self.result.get()
        self.result.set(self.a[0:-1])
    #制作开平方运算
    def numSqrt(self):
        self.result.set(math.sqrt(float(self.result.get())))
    #制作正负号
    def zhengFu(self):
        a = int(self.result.get()) * (-1)
        self.result.set(a)

    #制作 1 / X  的方法
    def grade(self):
        a = float(self.result.get())
        b = 1 / a
        self.result.set(b)


    errorlist = ['除数不能为0', '请输入一个正数']
    # 定义MC
    def press_MC(self):
        tkinter.messagebox.showinfo('SORRY(>_<)', '还没做 别乱点！请试一下MR~ (`･ω･´)')

    # 定义MR
    def press_MR(self):
        tkinter.messagebox.showinfo('SORRY(>_<)', '还没做 别乱点！请试一下MS~ (`･ω･´)')

    # 定义MS
    def press_MS(self):

        tkinter.messagebox.showinfo('SORRY(>_<)', '还没做 别乱点！请试一下M+~ (`･ω･´)')

    # 定义M+
    def press_MAdd(self):

        tkinter.messagebox.showinfo('SORRY(>_<)', '还没做 别乱点！请试一下M-~ (`･ω･´)')

    # 定义M-
    def press_MSub(self):
        tkinter.messagebox.showinfo('SORRY(>_<)', '除了这一行其他都做了 真的~ (•ิ_•ิ)')

#实例化对象
myjsq = jsp()