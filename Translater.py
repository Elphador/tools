from pyrogram import Client , filters 
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

#from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResulArticle, InputMessageContent 
from googletrans import Translator
from gtts import gTTS
import qrcode 
import os
#import zbar
#import pyzbar
#from PIL import Image
#from pyzbar.pyzbar import decode
#import pyqrcode
from tool import headers 
#import cv2
from pytube import YouTube 
from bs4 import BeautifulSoup 
import requests 
whisper = {}
whispe = {}



elpha = Client ( "Tools",  api_id =18802415,  api_hash = "a8993f96404fd9a67de867586b3ddc92" , bot_token = "5942042027:AAFguYxw9ojuX8nIgYAGA6zPLNT1-k-AGS8")


@elpha.on_message(filters.private & filters.command("start"))
def start (bot, msg):
    format = msg.from_user.first_name 
    text = f"**Hello sir {format} I'm multi purpose bot \n i can do some cool  tasks  .......etc** \n ||what if you joined my little channel🤕||"
    mark = InlineKeyboardMarkup ([[InlineKeyboardButton("Channel",url="https://t.me/developerspage"),InlineKeyboardButton("Group",url="https://t.me/developerschat")], [InlineKeyboardButton("Developer", url="https://t.me/e_phador"),InlineKeyboardButton("♧Moderator", url="https://t.me/the_ep")]])
    msg.reply(text=text , reply_markup = mark )
@elpha.on_message(filters.private & filters.regex("http"))
def http (bot,msg):
    kb =InlineKeyboardMarkup ([[InlineKeyboardButton("Scrap Page ",callback_data="source")],
                                [InlineKeyboardButton("Download mp3 ",callback_data="ytaudio")],
                                [InlineKeyboardButton("Download Video ",callback_data="ytvideo")]])
    msg.reply ("`Just Click Something `",reply_markup=kb,  quote=True)    

        
 


@elpha.on_message(filters.private & filters.video|filters.document|filters.audio)

def dllink(bot ,msg):

    text  = msg.reply("Detecting File ")

    def progress(current, total):

        text.edit(f"**Downloading to My server😇 {current*100/total:.1f}% **")

    file = msg.download(progress=progress)


    files = {

    'sess_id': (None, 'y3stdcwgd2eksu0c'),

    'utype': (None, 'prem'),

    'file_0': open(file, 'rb'),}

    response = requests.post('https://31.filelu.com/cgi-bin/upload.cgi', files=files)

    t = json.loads(response.text)

    f = t[0].get("file_code")

    #msg.reply_document(file, caption=json.loads(response.text))

    params = {

    'file_code': f ,

    'key':"22168q9ibs27178io1aan"}

    response = requests.get('https://filelu.com/api/file/direct_link', params=params)

    li= json.loads(response.content)

    lin = li.get("result").get("url")

    text.edit(f".      [📥͌̿͝D͒͋̽o͊̒̚w͐͑͘n̽͊͘l͆͛̒o͌͋̕ä́͌͋d̒̈́̈́📥̾̿̕]({lin}) \n\n\n||Sponsor Us for more GB File Direct Download Link||" ,reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton("Sponsor", url="https://t.me/developerschat")]]) ,disable_web_page_preview=True)


@elpha.on_message(filters.private & filters.photo)   
def encoder (bot,msg):
    text = msg.reply ("`if you sent Qr I'll try to read but not be sure on me it will works 10% and return success for lucky ones`/n||the developers are working to fix this wait until release ||")
    dl = str(msg.from_user.id)
    dwd = ''
    qr= ''
    try:
        dwd = msg.download(file_name=dl + '.png')
    except Exception as error:
        msg.reply(text=error)
        return
    try:
        qrdata = decode(Image.open(dwd))
        qrl = list(qrdata[0])
        qext = str(qr_text_list[0]).split("'")[1]
        qtext = "".join(qr_text_ext)
    except Exception as error:
        msg.reply(text=error)
        return
    msg.reply(f"**Your Qr Data**:-\n` {qr_text}`",	reply_markup=InlineKeyboardMarkup( [[InlineKeyboardButton("Say Hi The Devs", url=f"https://t.me/developerschat")]] ), disable_web_page_preview=True)

@elpha.on_message(filters.private & filters.text)
def tools(bot , update):
    text = "`Just Click Something `"
    mark = InlineKeyboardMarkup ([
            [InlineKeyboardButton("Translation", callback_data="trans")],
            [InlineKeyboardButton("Genrate QR", callback_data="genqr")],
            [InlineKeyboardButton("Text to Speech", callback_data= "tts")]
            ])
    update.reply_text (text=text , reply_markup = mark, quote = True)
    
    
    
    
    
    
play1 =  InlineKeyboardMarkup ([
                                    [InlineKeyboardButton("Africans", callback_data="af"),
                                    InlineKeyboardButton("Albanian", callback_data="sq"), 
                                    InlineKeyboardButton("Amaharic",callback_data="am"),
                                    InlineKeyboardButton("Arabic", callback_data="ar")],
                                    [InlineKeyboardButton("Armenian", callback_data="hy"), 
                                    InlineKeyboardButton("Azerbaijan",callback_data="az"), 
                                    InlineKeyboardButton("Basque",callback_data="eu"),
                                    InlineKeyboardButton("Belarusian", callback_data="be")],
                                    [InlineKeyboardButton("Bengali", callback_data="bn"), 
                                    InlineKeyboardButton("Bosnian",callback_data="bs"), 
                                    InlineKeyboardButton("Bulgarian",callback_data="bg"),
                                    InlineKeyboardButton("Catalan",callback_data="ca")],
                                    [InlineKeyboardButton("Cebuano",callback_data="ceb"),
                                    InlineKeyboardButton("Chichewa",callback_data="ny"), 
                                    InlineKeyboardButton("Chinese🧓",callback_data="zh-tw"),
                                    InlineKeyboardButton("Chinese🧒",callback_data="zh-cn")],
                                    [InlineKeyboardButton("Corsican",callback_data="co"), 
                                    InlineKeyboardButton("Croatian", callback_data="hr"), 
                                    InlineKeyboardButton("Czech",callback_data="cs"),
                                    InlineKeyboardButton("Danish", callback_data="da")],
                                    [InlineKeyboardButton("Dutch", callback_data="nl"), 
                                    InlineKeyboardButton("English", callback_data="en")],
                                    [InlineKeyboardButton("Back",callback_data="back1"),
                                    InlineKeyboardButton ("Next",callback_data="next1")]])   
                                
                                
play2 =  InlineKeyboardMarkup ([[InlineKeyboardButton("Esperanto", callback_data="eo"),
                                    InlineKeyboardButton("Estonian", callback_data="et"), 
                                    InlineKeyboardButton("Filipino", callback_data="tl"),
                                    InlineKeyboardButton("Finnish", callback_data="fi")],
                                    [InlineKeyboardButton("French", callback_data="fr"), 
                                    InlineKeyboardButton("Frisian",callback_data="fy"), 
                                    InlineKeyboardButton("Galician",callback_data="gl"),
                                    InlineKeyboardButton("Georgian",callback_data="ka")],
                                    [InlineKeyboardButton("German", callback_data="de"), 
                                    InlineKeyboardButton("Greek",callback_data="el"), 
                                    InlineKeyboardButton("Gujarati",callback_data="gu"),
                                    InlineKeyboardButton("Hitan",callback_data="ht")],
                                    [InlineKeyboardButton("Hausa",callback_data="ha"),
                                    InlineKeyboardButton("Hawaian",callback_data="haw"), 
                                    InlineKeyboardButton("Hebrew",callback_data="iw"),
                                    InlineKeyboardButton("Hebrew",callback_data="he")],
                                    [InlineKeyboardButton("Hindi",callback_data="hi"), 
                                    InlineKeyboardButton("Hmong",callback_data="hmn"), 
                                    InlineKeyboardButton("Hungarian", callback_data="hu"),
                                    InlineKeyboardButton("Iceland", callback_data="is")],
                                    [InlineKeyboardButton("Igbo",callback_data ="ig"), 
                                    InlineKeyboardButton("Indonesian",callback_data="id")],
                                    [InlineKeyboardButton("Previous", callback_data="next0"),
                                    InlineKeyboardButton ("Next",callback_data="next2")]
                                ])  
                                    
play3 =  InlineKeyboardMarkup ([[InlineKeyboardButton("Irish", callback_data="ga"),
                                    InlineKeyboardButton("Italian", callback_data="it"), 
                                    InlineKeyboardButton("Japanese", callback_data="ja"),
                                    InlineKeyboardButton("Javanese",callback_data = "jw")],
                                [InlineKeyboardButton("Kannada",callback_data="kn"), 
                                    InlineKeyboardButton("Kazakh", callback_data="kk"), 
                                    InlineKeyboardButton("Khmer",callback_data="km"),
                                    InlineKeyboardButton("Korean" ,callback_data="ko")],
                                [InlineKeyboardButton("Kurdish", callback_data="ku"), 
                                    InlineKeyboardButton("Kyrgyzstan", callback_data="ky"), 
                                    InlineKeyboardButton("Lao",callback_data="lo"),
                                    InlineKeyboardButton("Latin",callback_data="la")],
                                [InlineKeyboardButton("Latvian", callback_data="lv"),
                                    InlineKeyboardButton("Lithuanian",callback_data="lt"), 
                                    InlineKeyboardButton("Luxembourg", callback_data="lb"),
                                    InlineKeyboardButton("Macedonian", callback_data="mk")],
                                [InlineKeyboardButton("Malagasy",callback_data="mg"), 
                                    InlineKeyboardButton("Malay",callback_data="ms"), 
                                    InlineKeyboardButton("Malayalam",callback_data="ml"),
                                    InlineKeyboardButton("Maltese",callback_data="mt")],
                                [InlineKeyboardButton("Maori", callback_data="mi"), 
                                InlineKeyboardButton("Marathi",callback_data="mr")],
                                [InlineKeyboardButton("Previous", callback_data="next1"),
                                InlineKeyboardButton ("Next", callback_data="next3")]
                                ])   
                                    
play4 =  InlineKeyboardMarkup ([[InlineKeyboardButton("Mongolian",callback_data="mn"),
                                    InlineKeyboardButton("Myanmar", callback_data="my"), 
                                    InlineKeyboardButton("Nepali",callback_data="ne"),
                                    InlineKeyboardButton("Norwegian", callback_data="no")],
                                    [InlineKeyboardButton("Odia",callback_data="or"), 
                                    InlineKeyboardButton("Pashto",callback_data="ps"), 
                                    InlineKeyboardButton("Persian", callback_data="fa"),
                                    InlineKeyboardButton("Polish", callback_data="pl")],
                                    [InlineKeyboardButton("Portuguese", callback_data="pt"), 
                                    InlineKeyboardButton("Punjabi",callback_data="pa"), 
                                    InlineKeyboardButton("Romanian", callback_data="ro"),
                                    InlineKeyboardButton("Russian", callback_data="ru")],
                                    [InlineKeyboardButton("Samoan", callback_data="sm"),
                                    InlineKeyboardButton("Scots gailic",callback_data="gd"), 
                                    InlineKeyboardButton("Serbian", callback_data="sr"),
                                    InlineKeyboardButton("sesotho",callback_data="st")],
                                    [InlineKeyboardButton("Shona",callback_data="sn"), 
                                    InlineKeyboardButton("Sindhi",callback_data="sd"), 
                                    InlineKeyboardButton("Sinhala",callback_data="si"),
                                    InlineKeyboardButton("Slovak",callback_data="sk")],
                                    [InlineKeyboardButton("Slovenian", callback_data="sl"), 
                                    InlineKeyboardButton("Somali",callback_data="so")],
                                    [InlineKeyboardButton("Previous", callback_data="next2"),
                                    InlineKeyboardButton("Next", callback_data="next4") ]])   
        
play5 =  InlineKeyboardMarkup ([[InlineKeyboardButton("Spanish", callback_data="es"),
                                    InlineKeyboardButton("Sudanese", callback_data="su"), 
                                    InlineKeyboardButton("Swahili",callback_data="sw"),
                                    InlineKeyboardButton("Swedish", callback_data="sv")],
                                    [InlineKeyboardButton("Tajik",callback_data="tg"), 
                                    InlineKeyboardButton("Tamil",callback_data="ta"), 
                                    InlineKeyboardButton("Telugu",callback_data="te"),
                                    InlineKeyboardButton("Thai",callback_data="th")],
                                    [InlineKeyboardButton("Turkish", callback_data="tr"), 
                                    InlineKeyboardButton("Ukrainian", callback_data="uk"), 
                                    InlineKeyboardButton("Urdu",callback_data="ur"),
                                    InlineKeyboardButton("Uyghur",callback_data="ug")],
                                    [InlineKeyboardButton("Uzbek",callback_data="uz"),
                                    InlineKeyboardButton("Vietnamese", callback_data="vi"), 
                                    InlineKeyboardButton("Welsh",callback_data="cy"),
                                    InlineKeyboardButton("Xhosa", callback_data="xh")],
                                    [InlineKeyboardButton("Yiddish",callback_data="yi"), 
                                    InlineKeyboardButton("Yoruba",callback_data="yo"), 
                                    InlineKeyboardButton("Zulu",callback_data="zu"),
                                    InlineKeyboardButton("Oromo",callback_data="om3")],
                                    [InlineKeyboardButton("Tigrenga",callback_data="ti3"), 
                                    InlineKeyboardButton("Twi or Akan",callback_data="ak3"),
                                    InlineKeyboardButton("Quachua",callback_data="qu3"),
                                    InlineKeyboardButton ("Guarani",callback_data="gn3")],
                                    [InlineKeyboardButton ("Tsonga",callback_data="ts3") ,
                                    InlineKeyboardButton("Sepedi",callback_data="nso3"),
                                    InlineKeyboardButton ("Sanskriti",callback_data="sa3")],
                                    [InlineKeyboardButton("Previous", callback_data="next3"),
                                    InlineKeyboardButton("Back to 1st Page", callback_data="next0")]])
sound1 =  InlineKeyboardMarkup ([
                                    [InlineKeyboardButton("Africans", callback_data="2af"),
                                    InlineKeyboardButton("Arabic", callback_data="ar2"), 
                                    InlineKeyboardButton("Bulgarian",callback_data="b2g"),
                                    InlineKeyboardButton("Bengali", callback_data="bn2")],
                                    [InlineKeyboardButton("Bosnian", callback_data="bs2"), 
                                    InlineKeyboardButton("Catalan",callback_data="ca2"), 
                                    InlineKeyboardButton("Czech",callback_data="cs2"),
                                    InlineKeyboardButton("Danish", callback_data="d2a")],
                                    [InlineKeyboardButton("German", callback_data="de"), 
                                    InlineKeyboardButton("Greek",callback_data="el2"), 
                                    InlineKeyboardButton("English",callback_data="b2g"),
                                    InlineKeyboardButton("Spanish",callback_data="es2")],
                                    [InlineKeyboardButton("Estonian",callback_data="e2t"),
                                    InlineKeyboardButton("Finnish",callback_data="fr2"), 
                                    InlineKeyboardButton("Chinese🧓",callback_data="z2h-TW"),
                                    InlineKeyboardButton("Chinese🧒",callback_data="zh2-CN")],
                                    [InlineKeyboardButton("Mandarin",callback_data="zh2"), 
                                    InlineKeyboardButton("Croatian", callback_data="hr2"), 
                                    InlineKeyboardButton("Gujarati",callback_data="gu2"),
                                    InlineKeyboardButton("French", callback_data="fr2")],
                                    [InlineKeyboardButton("Hindi", callback_data="hi2"), 
                                    InlineKeyboardButton("Hungarian", callback_data="2hu")],
                                    [InlineKeyboardButton("Back",callback_data="back1"),
                                    InlineKeyboardButton ("Next",callback_data="next01")]])   
                                    
                                    
                                    
sound2 =  InlineKeyboardMarkup ([
                                    [InlineKeyboardButton("Indonesian", callback_data="2id"),
                                    InlineKeyboardButton("Icelandic", callback_data="is2"), 
                                    InlineKeyboardButton("Italian",callback_data="it2"),
                                    InlineKeyboardButton("Hebrew", callback_data="iw2")],
                                    [InlineKeyboardButton("Japanese", callback_data="2ja"), 
                                    InlineKeyboardButton("Javanese",callback_data="jw2"), 
                                    InlineKeyboardButton("Khmer",callback_data="km2"),
                                    InlineKeyboardButton("Kannada", callback_data="2kn")],
                                    [InlineKeyboardButton("Korean", callback_data="k2o"), 
                                    InlineKeyboardButton("Latin",callback_data="l2a"), 
                                    InlineKeyboardButton("Latvian",callback_data="2lv"),
                                    InlineKeyboardButton("Malayalam",callback_data="2ml")],
                                    [InlineKeyboardButton("Marathi",callback_data="mr2"),
                                    InlineKeyboardButton("Malay",callback_data="ms2"), 
                                    InlineKeyboardButton("Myanmar",callback_data="m2y"),
                                    InlineKeyboardButton("Nepali",callback_data="ne2")],
                                    [InlineKeyboardButton("Dutch",callback_data="nl2"), 
                                    InlineKeyboardButton("Norwegian", callback_data="2no"), 
                                    InlineKeyboardButton("Polish",callback_data="pl2"),
                                    InlineKeyboardButton("Portuguese", callback_data="2pt")],
                                    [InlineKeyboardButton("Romanian", callback_data="ro2"), 
                                    InlineKeyboardButton("Russian", callback_data="ru2")],
                                    [InlineKeyboardButton("Back",callback_data="tts"),
                                    InlineKeyboardButton ("Next",callback_data="next02")]])   
                          
sound2 =  InlineKeyboardMarkup ([
                                    [InlineKeyboardButton("Sinhala", callback_data="si2"),
                                    InlineKeyboardButton("Slovak", callback_data="sk2"), 
                                    InlineKeyboardButton("Albanian",callback_data="s2q"),
                                    InlineKeyboardButton("Serbian", callback_data="s2r")],
                                    [InlineKeyboardButton("Sudanese", callback_data="2su"), 
                                    InlineKeyboardButton("Swedish",callback_data="sv2"), 
                                    InlineKeyboardButton("Swahili",callback_data="s2w"),
                                    InlineKeyboardButton("Tamil", callback_data="t2a")],
                                    [InlineKeyboardButton("Telugu", callback_data="2te"), 
                                    InlineKeyboardButton("Thai",callback_data="th2"), 
                                    InlineKeyboardButton("Filipino",callback_data="t2l"),
                                    InlineKeyboardButton("Turkish",callback_data="t2r")],
                                    [InlineKeyboardButton("Ukrainian",callback_data="2uk"),
                                    InlineKeyboardButton("Urdu",callback_data="u2r"), 
                                    InlineKeyboardButton("Vietnamese",callback_data="vi2"),
                                    InlineKeyboardButton("Amharic",callback_data="ama")],
                                    [InlineKeyboardButton("None",callback_data="oro"), 
                                    InlineKeyboardButton("None", callback_data="oro"), 
                                    InlineKeyboardButton("None",callback_data="oro"),
                                    InlineKeyboardButton("None", callback_data="oro")],
                                    [InlineKeyboardButton("None", callback_data="oro"), 
                                    InlineKeyboardButton("None", callback_data="oro")],
                                    [InlineKeyboardButton("Back",callback_data="back01"),
                                    InlineKeyboardButton ("More",callback_data="back1")]])   
                          
                          
                                     
           
  
     
@elpha.on_callback_query()
def callback (bot ,update):
    callback_data = update.data
    text2 = "Choose Language baby🤱"
    
    if callback_data == "whisper":
        uid = update.from_user.id
        print (uid)
        beta = whisper.get("data").get("ex")
        u  = int(whisper.get("data").get("id"))
        if uid == u :
            update.answer(text= str(whisper.get("data").get("text")) ,show_alert=True)
        else :
            update.answer("this message isn't sent for you ,don't click such buttons blindly as you get😏,now assume i haven't seen you & you haven't read this mesage and get back😒",show_alert=True)
       # time.sleep(480)    
       #whisper.clear() 
    elif callback_data == "whisperon":
        uid = update.from_user.id
        print (uid)
        beta = whispe.get("data").get("ex")
        w  = int(whispe.get("data").get("id"))
        if w == uid :
            update.answer("Oh sorry dude😅you're the only one who can't able to see this message🙈 ",show_alert=True)
        else :
            update.answer(str(whispe.get("data").get("text")) , show_alert=True)
                
  
    
    elif callback_data =="trans":
        user_text = update.message.reply_to_message.text 
   
        update.answer(f"choose language🤩", show_alert=True)
        update.message.edit_text (text = text2 ,reply_markup = play1 )
    elif callback_data== "next1":
        update.message.edit (text =  text2 ,reply_markup = play2)
    elif callback_data == "next2":
        update.message.edit (text=text2 , reply_markup=play3)
    elif callback_data == "next3":
        update.message.edit (text = text2 , reply_markup = play4)
    elif callback_data == "next4":
        update.message.edit(text = text2 ,reply_markup= play5)
    elif callback_data == "next0":
        update.message.edit(text = text2 ,reply_markup= play1)
    elif callback_data == "oro":
        update.message.edit(text = "Sorry Our Team were working to make available this language pls stay tuned until we finish")
    elif callback_data == "genqr":
        user_text = update.message.reply_to_message.text 
   
        q = (user_text)
        name = ("result")
        qrcode = pyqrcode.create(q)
        qrcode.png(name + '.png', scale=6)
        img = name + '.png'
        update.message.reply_photo( img,caption=f"Qr Data : {q}" ,reply_markup=InlineKeyboardMarkup ([[InlineKeyboardButton("Suggest us More",url="t.me/developerschat")]]) )
        
    elif callback_data == "ytaudio" :
        user_text = update.message.reply_to_message.text 
   
        text = update.message.reply_text("`Downloading  to my server😇`")
        yt = YouTube(user_text)
        #print ("something")
        video = yt.streams.filter(only_audio=True).first()
        folder = "downloads/video/"
        #print("something")
        if not os.path.isdir(folder):
            os.makedirs(folder)
        file = video.download(folder)
        #base, ext = os.path.splitext(file)
        new_file = yt.title + '.mp3'
        os.rename(file, new_file)
        #print('Downloading...')
        with open(new_file,'rb') as e:
            def progress(current, total):
                print(f"{current * 100 / total:.1f}%")
                text.edit(f"`Uploading to your server😇 {current*100/total:.1f}% `")
            update.message.reply_audio(e,caption=f"{yt.title} \n||why don't you click the button||",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Just Click",url="t.me/developerschat")]]),progress=progress)
  
        
                 
    elif callback_data == "ytvideo":
        user_text = update.message.reply_to_message.text 
   
        text = update.message.reply_text("`Downloading  to my server `")
        yt = YouTube(user_text)
        #print ("something") 
        video = yt.streams.filter(file_extension="mp4").first()
        folder = "downloads/video/"
        #print("something")
        if not os.path.isdir(folder):
            os.makedirs(folder)
        file = video.download(folder)
        
        #base, ext = os.path.splitext(file)
        new_file = yt.title + '.mp4'
        os.rename(file, new_file)
        #print('Downloading...')
        with open(new_file,'rb') as e:
            def progress(current, total):
                print(f"{current * 100 / total:.1f}%")
                text.edit(f"` Uploading to your server😇 {current*100/total:.1f}% `")
            update.message.reply_video(e,caption=f"{yt.title} \n||why don't you click the button||",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Just Click",url="t.me/developerschat")]]), progress=progress)
  
         
        
    elif callback_data == "source" :
        user_text = update.message.reply_to_message.text 
   
        url = user_text 
        try:
            request =requests.get(url)
            soup = BeautifulSoup(request.content , 'html.parser')
            parse = open( 'result.txt','w')
            we = parse.write(soup.prettify())
            parse.close
            update.message.reply_document("result.txt")
        except:
            update.message.reply_text("sorry it seems there's no byte data on web")
    
    elif callback_data== "back1":
        update.message.edit_text("Ohh sorry can't you find what function you wanted still you can report this to [our team](https://t.me/developerschat)")
    elif callback_data == "tts" :
        update.message.edit_text(text=text2 , reply_markup = sound1 )
    elif callback_data =="next01":
        update.message.edit_text (text=text2 , reply_markup= sound2)
    elif callback_data == "next02":
        update.message.edit_text (text=text2 , reply_markup= sound3)
    elif callback_data == "ama":
        user_text = update.message.reply_to_message.text 
   
        hi = user_text 
        json_data = { 'userId': 'public-access', 'ssml': f'{hi}','voice': 'am-ET-AmehaNeural',}
        response = requests.post('https://play.ht/api/transcribe', json =json_data)
        res = response.text 
        cv = res.replace ("false",'False')
        with open ('amharic_speech.mp3','wb')as w:
            w.write(response.content)
        update.message.reply_voice('amharic_speech.mp3') 
    
        
    else:
        call =  callback_data 
        user_text = update.message.reply_to_message.text 
   
        
        if "2" in call:
            pure = call.replace("2","")
            sound = gTTS(user_text, lang=pure)
            s = sound.save("sound.mp3")
            w = open("sound.mp3","rb")
            update.message.reply_voice(w)
        elif "3" in call:
            txt = update.message.reply_text("`Translating●●○○○○○○ baby🤱`")
            pure=call.replace("3","")
            user = user_text.replace(" ","+")
            data = f'async=translate,sl:auto,tl:{pure},st:{user},id:1672943546520,qc:true,ac:true,_id:tw-async-translate,_pms:qs,_fmt:pc'
            response = requests.post('https://www.google.com/async/translate',  headers =headers, data=data)
            v = BeautifulSoup(response.text , "html.parser")
            d = v.find("span",id="tw-answ-target-text")
            txt.edit(d)

            
        else:
            update.message.edit_text("`Translating●●●●○○○○○○ baby😺`")
            translater = Translator()
            data = callback_data
            Translation = translater.translate(user_text, dest= data)
            update.message.edit_text(f"`{Translation.text}` \n \n ** Suggest us languages available on google but not listed here ** " , reply_markup  = InlineKeyboardMarkup([[InlineKeyboardButton("Suggest", url="https://t.me/developerschat")]]))
v={}      
@elpha.on_inline_query()   
def inline (bot,msg):
    txt = msg.query
    m = msg.from_user.first_name 
    id = txt.split("|")[0]
    men = f"[User](tg://user?id={id})"
    text = txt.split("|")[1]
    if "|!" in txt :
        txt.replace("!","")
        whispe["data"]={"text":text , "id":id,"ex":txt}
    else :
        whisper["data"]={"text":text , "id":id,"ex":txt}
    
    
    msg.answer( results = [ ( InlineQueryResultArticle(
    title = "whisper to ",
    description ="user id | message content ",
    input_message_content = InputTextMessageContent(f"whisper message from {m} to {men}") , 
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Whisper", callback_data="whisper")]])
    )),
    InlineQueryResultArticle(
    title = "whisper on ",
    description ="user id |! message content ",
    input_message_content = InputTextMessageContent(f"whisper message from {m} to {men}") ,
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Whisper", callback_data="whisperon")]])
    )])
@elpha.on_callback_query()
def callback (bot ,update):
        callback_data = update.data
        text2 = "Choose Language baby🤱"
        if callback_data == "whisper":
            update.answer(text=str(text) ,show_alert=True)
        else :
            pass
     

        
print ("alive ")        
        
elpha.run()
        
        
        
    
    
    
