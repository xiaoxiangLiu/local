__author__ = '38720'
# coding=utf-8

from pymouse import PyMouse
from pykeyboard import PyKeyboard


m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
print(x_dim, y_dim)