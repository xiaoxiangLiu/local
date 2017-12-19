# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.py'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    # 所有的pyqt5应用必须创建一个应用(Application)对象,
    # sys.argv参数是一个来自命令行的参数列表
    # python脚本可以在shell中运行，这是我们用来控制我们应用的一种方法
    app = QApplication(sys.argv)

    # QWidget组件是pyqt5中所有用户界面类的基础类,我们给QWidget提供了默认的构造方法
    # 默认构造方法没有父类，没有父类的QWidget组件将被作为窗口使用.
    w = QWidget()
    # resize()方法调整了widget组件的大小，单位是px
    w.resize(800, 150)
    # move()方法移动QWidget组件到一个位置，参数是x=300,y=300
    w.move(300,300)
    # setWindowTitle()方法给组件一个标题
    w.setWindowTitle('simple')
    # show()方法是展示在桌面上
    w.show()
    # app.exec_()让应用进入主循环直到sys.exit()被调用
    # 不使用sys.exit()也是可以的，但是进程不会退出
    # app.exec_()返回0
    #
    sys.exit(app.exec_())



