#!/usr/bin/python
from wxpy import *
import time
bot=Bot()
my_group = bot.chats().search('MySQL运维内参一群')[0].search('Frank')
my_group.add_all()
