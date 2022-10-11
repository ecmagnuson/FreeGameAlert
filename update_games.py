from utils import get_sendfrom_email, get_sendto_email, get_apppassword
import feedparser
import smtplib

#RSS feed of free games - https://steamcommunity.com/groups/freegamesfinders/announcements
d = feedparser.parse('https://steamcommunity.com/groups/freegamesfinders/rss/')

def update_game_list():
    #File of all games in RSS feed
    with open('games.txt','w') as f:
        for entry in d.entries:
            f.write(f'{entry.title}\n') 

def get_newest_file_game():
    #get newest game on top of file
    with open('games.txt', 'r') as f:
        return f.readline().strip()

def get_newest_RSS_game():
    #get newest game on RSS feed
    return f'{d.entries[0].title}'.strip()

def is_same_game():
    #check if RSS feed and top game from file is the same
    return get_newest_file_game() == get_newest_RSS_game()

def get_offer_deadline():
    #TODO
    return f'{d.entries[0].description}'.strip()

def alert():
    #Google removed less-secure-apps now must use app password
    #https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
    #send email if games are not the same
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
        email_address = get_sendfrom_email()
        email_password = get_apppassword()
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs=get_sendto_email(), 
        msg=f'subject:Free Game! \n\n Looks like there is a free game :D \n {d.entries[0].title} is free right now. \n\n See the link: {d.entries[0].link}')

if __name__ == '__main__':
    if not is_same_game():
        alert()
        update_game_list()