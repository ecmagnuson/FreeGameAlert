import feedparser
import os
import smtplib

import tkinter as tk
from tkinter import messagebox

from datetime import datetime
from utils import get_sendfrom_email, get_sendto_email, get_apppassword

#RSS feed of free games - https://steamcommunity.com/groups/freegamesfinders/announcements
d = feedparser.parse('https://steamcommunity.com/groups/freegamesfinders/rss/')

def update_game_list():
    #File of all games in RSS feed
    with open(os.path.dirname(__file__) + '/games.txt','w') as f:
        for entry in d.entries:
            f.write(f'{entry.title}\n') 

def get_newest_file_game():
    #get newest game on top of file
    with open(os.path.dirname(__file__) + '/games.txt', 'r') as f:
        return f.readline().strip()

def get_newest_RSS_game():
    #get newest game on RSS feed
    return f'{d.entries[0].title}'.strip()

def is_same_game():
    #check if RSS feed and top game from file is the same
    return get_newest_file_game() == get_newest_RSS_game()

def get_offer_deadline():
    #the description is formated the same way every time
    return d.entries[0].description[d.entries[0].description.index('Offer') : d.entries[0].description.index('GMT') + 3]

def get_CST_deadline():
    #convert GMT time to CST because I'm not british
    #This is so convoluted, it's gonna break I feel
    deadline = get_offer_deadline()
    GMT = int(deadline[deadline.index(',') + 2 : deadline.index('GMT')])
    CST_time = GMT - 500
    CST_time = str(CST_time)
    CST_time = CST_time[0 : 2] + ':' + CST_time[2:]
    deadline = deadline[ : deadline.index(',') + 1]
    d = datetime.strptime(CST_time, "%H:%M")
    return f'{deadline} {d.strftime("%I:%M %p")}'

def email():
    #Google removed less-secure-apps now must use app password
    #https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
        email_address = get_sendfrom_email()
        email_password = get_apppassword()
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs=get_sendto_email(), 
        msg=f'subject:Free Game! {get_CST_deadline()} \n\n Looks like there is a free game :D \n\n {d.entries[0].title} is free right now. \n See the link: {d.entries[0].link} \n\n {get_CST_deadline()}.')

def alert():
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning('Free Game!', 'New free game :)')

if __name__ == '__main__':
    if not is_same_game():
        email()
        alert()
        update_game_list()