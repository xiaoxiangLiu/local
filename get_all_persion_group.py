#!/usr/bin/python
from wxpy import *
import time
bot=Bot(console_qr=2,cache_path=True)
#boring_group = bot.groups().search('中国IT联盟')[0]
boring_group=bot.chats().search('中国IT联盟')[0]
for member in boring_group:
	print (str(member))
	#boring_group.add_all()
	#time.sleep(60)
