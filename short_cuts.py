#   Author Hari Krishna Moorthy
#   done on 01.06.2020
#______________________________________________________________________________________________________________________________________________________________

import time
import webbrowser as web
import pyautogui as pg
import wikipedia
import requests
import subprocess
from tkinter import *
from gtts import gTTS  
import os 
import playsound
from tkinter import messagebox as msg
from PIL import ImageTk , Image
from bs4 import BeautifulSoup


bg_col = "gray97"
but_col = "gray72"
ent_col = "gray81"

def check(val):
    try :
        requests.get(val)
    except requests.exceptions.ConnectionError :
        return False
    return True

def check_internet():
    error_message = '''No internet

      Try:

          Checking the network cables, modem, and router
          Reconnecting to Wi-Fi
          Running Windows Network Diagnostics
          DNS_PROBE_FINISHED_NO_INTERNET'''
    if not (check("https://google.com")):
        msg.showerror("Network Error", error_message )
    else:
       return True

def playonyt():
    '''Opens YouTube video with following title'''
    if not check_internet():
        quit()
    if yt_entry.get() == "" :
            error_message = '''Enter the proper details '''
            msg.showerror("Error", error_message )
            return
    
    url = 'https://www.youtube.com/results?q=' + yt_entry.get()
    sc = requests.get(url)
    sctext = sc.text
    soup = BeautifulSoup(sctext,"html.parser")
    songs = soup.findAll("div",{"class":"yt-lockup-video"})
    song = songs[0].contents[0].contents[0].contents[0]
    songurl = song["href"]
    web.open("https://www.youtube.com"+songurl)

#def sendwhatmsg():
#    if not check_internet():
##        quit()
#    phone_no = wa_num_entry.get()
#    message = wa_msg_entry.get()
#    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
#    time.sleep(20)
#    pg.press('enter')

def info():
    '''Gives information on the topic'''
    if not check_internet():
        quit()
    check_internet()
    topic = wekipedia_input.get()
    if topic =="" :
            error_message = '''Enter the proper details'''
            msg.showerror("Error", error_message )
            return 
    lines = 3
    result = wikipedia.summary(topic, sentences = lines)
    file = open("result.txt" , 'w')
    file.write(result)
    file.close()

    (gTTS(text=result, lang="en", slow=False)).save("result.mp3")
    os.system("mpg321 welcome.mp3")

    playsound.playsound('result.mp3', True)
    subprocess.call(['notepad.exe' , 'result.txt'])
    os.remove("result.mp3")
    os.remove("result.txt")

def wa_frame():
    root.destroy()
    rootwa = Tk()
    rootwa.title("short-cut ")
    rootwa.geometry("240x320+1100+110")

    def sendwhatmsg():
        if not check_internet():
            quit()
        phone_no = str(wa_num_entry.get()).strip()
        message = str(wa_msg_entry.get()).strip()
        if len(phone_no) != 10  and message =="" :
            error_message = '''Enter the proper details
                                 1)Check the Number Entered
                                 2)fill the message column ... '''
            msg.showerror("Error", error_message )
            return
        if not phone_no.startswith("+91"):
            phone_no = "+91"+phone_no
        print(phone_no)
        web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+message)
        time.sleep(20)
        pg.press('enter')

    wa_frame = Frame(rootwa ,width = 240 , height = 320 , relief="raise")
    wa_frame.pack()
    
    yt_logo = Canvas(wa_frame, width=175, height=52 ,bd = 0, bg = bg_col)
    yt_logo.pack()
    wa_img = ImageTk.PhotoImage(Image.open("img\wa_logo.png"))
    yt_logo.create_image(0, 0, anchor=NW, image=wa_img)
    yt_logo.place(relx = 0.12 ,rely = 0.01)

    wa_num_lable = Label(wa_frame , font=('arial', 16, 'bold'), text = "Phone No" ) 
    wa_num_lable.place(relx = 0.03 ,rely = 0.29,)
    wa_num_entry = Entry(wa_frame ,bg = ent_col, font=('arial', 12, 'bold'),width = 13 ) 
    wa_num_entry.place(relx = 0.46 , rely = 0.3)
    
    wa_msg_lable = Label(wa_frame , font=('arial', 16, 'bold'), text = "Message" ) 
    wa_msg_lable.place(relx = 0.03 ,rely = 0.49,)
    wa_msg_entry = Entry(wa_frame ,bg = ent_col, font=('arial', 12, 'bold'),width = 13  ) 
    wa_msg_entry.place(relx = 0.46 , rely = 0.5)

    
    wa_button = Button(wa_frame ,width = 32 , bg = but_col, text = "Send", command = sendwhatmsg )
    wa_button.place(relx = 0.05 , rely = 0.7)
    
    
def search():
    if not check_internet():
        quit()
    '''Searches about the topic on Google'''
    check_internet()
    if google_input.get() == "" :
            error_message = '''Enter the proper details '''
            msg.showerror("Error", error_message )
            return
    web.open("https://google.com?q="+google_input.get().strip())
    time.sleep(3)
    pg.press('enter')



root = Tk()
root.title("short-cut ")
root.geometry("240x460+1100+110")

#wa_frame()
yt_input = StringVar()
wekipedia_input = StringVar()
google_input = StringVar()

main_frame = Frame(root ,width = 240 , height = 460,bg = bg_col,  relief="raise")
main_frame.pack()
x = 0
yt_logo = Canvas(main_frame, width=175, height=52 ,bd = 0, bg = bg_col)
yt_logo.pack()
yt_img = ImageTk.PhotoImage(Image.open("img\yt_logo.png"))
yt_logo.create_image(0, 0, anchor=NW, image=yt_img)
yt_logo.place(relx = 0.12 ,rely = x+0.01,)

yt_entry = Entry(main_frame , bg = ent_col, font=('arial', 12, 'bold'),width = 13  ,textvariable=yt_input) 
yt_entry.place(relx = 0.03 , rely = 0.13)
yt_button = Button(main_frame ,width = 13 , bg = but_col , text = "Watch", command = playonyt )
yt_button.place(relx = 0.56 , rely = 0.13)    

x+=0.25
yt_logo = Canvas(main_frame, width=175, height=52 ,bd = 0, bg = bg_col)
yt_logo.pack()
wiki_img = ImageTk.PhotoImage(Image.open("img\wiki_logo.png"))
yt_logo.create_image(0, 0, anchor=NW, image=wiki_img)
yt_logo.place(relx = 0.12 ,rely = x+0.01,)

wekipedia_input = Entry(main_frame , bg = ent_col, font=('arial', 12, 'bold'),width = 13  ,textvariable= wekipedia_input) 
wekipedia_input.place(relx = 0.03 , rely = x+0.13)
wekipedia_button = Button(main_frame , font = ("times" , 8 , ), bg = but_col  ,width = 13 ,  text = "Find",command = info )
wekipedia_button.place(relx = 0.56 , rely = x+0.13)

x+=0.25
yt_logo = Canvas(main_frame, width=175, height=52 ,bd = 0, bg = bg_col)
yt_logo.pack()
gl_img = ImageTk.PhotoImage(Image.open("img\gl_logo.png"))
yt_logo.create_image(0, 0, anchor=NW, image=gl_img)
yt_logo.place(relx = 0.12 ,rely = x+0.01,)

google_input = Entry(main_frame , bg = ent_col , font=('arial', 12, 'bold'),width = 13 ,textvariable=google_input) 
google_input.place(relx = 0.03 , rely = x+0.13)
google_button = Button(main_frame , font = ("times" , 8 , ), bg = but_col  ,width = 13 ,  text = "Search",command = search )
google_button.place(relx = 0.56 , rely = x+0.13)

x+=0.25
yt_logo = Canvas(main_frame, width=175, height=52 ,bd = 0, bg = bg_col)
yt_logo.pack()
wa_img = ImageTk.PhotoImage(Image.open("img\wa_logo.png"))
yt_logo.create_image(0, 0, anchor=NW, image=wa_img)
yt_logo.place(relx = 0.12 ,rely = x+0.01,)
wa_button = Button(main_frame , font = ("times" , 8 , ), bg = but_col  ,width = 35 ,  text = "Whatsapp",command = wa_frame )
wa_button.place(relx = 0.05 , rely = x+0.13)

check_internet()
root.mainloop()
