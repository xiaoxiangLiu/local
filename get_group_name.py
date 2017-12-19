#!/usr/bin/python
from wxpy import *
bot=Bot(console_qr=2)
group=bot.groups()
for g in group:
    print (str(g))

