'''
使用图灵机器人
'''
# -*- coding: utf-8 -*-：
from wxpy import *
import requests
import re
import time

bot = Bot(cache_path=True)

KEY = '7cceb23d71834b508dd29d2f133a044e'

girl_friend = bot.friends().search('Ying shenG')[0]

def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key'    : KEY,
		'info'   : msg,
		'userid' : 'wechat-robot',
		}
	try:
		r = requests.post(apiUrl, data=data).json()
		return r.get('text')
	except:
		return
# group = bot.groups()
# friend = bot.friends()
# 注册好友请求类消息

@bot.register(msg_types=FRIENDS)

def auto_accept_friends(msg):

	if 'wxpy' in msg.text.lower():

		new_friend = bot.accept_friend(msg.card)

		new_friend.send('请求已经接受咯')




@bot.register(Group, TEXT)
def message_set(msg):
	if(msg.is_at):
		mess, num = re .subn(r'@(.+?)\s', ' ', msg.text)
		testmain = msg.sender
		return '{} '.format(get_response(mess.replace(' ','')))

@bot.register(Friend, TEXT)
def message_set(msg):

	mess = get_response(msg.text) 
	if mess !='':
		return '{}'.format(mess)
	else:
		return '机器人离开了'

@bot.register(girl_friend)
def ignore(msg):
	return


embed()
