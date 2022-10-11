from utils import get_sendfrom_email, get_sendto_email, get_apppassword
import feedparser
import smtplib

#RSS feed of free games - https://steamcommunity.com/groups/freegamesfinders/announcements
d = feedparser.parse('https://steamcommunity.com/groups/freegamesfinders/rss/')

def update_game_list():
    #File of all games in RSS feed
    with open('games.txt','w') as f:
        for entry in d.entries:
            f.write(f'{entry.title}, {entry.published}\n') 

def get_newest_file_game():
    #get newest game on top of file
    with open('games.txt', 'r') as f:
        return f.readline().strip()

def get_newest_RSS_game():
    #get newest game on RSS feed
    return f'{d.entries[0].title}, {d.entries[0].published}'.strip()

def is_same_game():
    #check if RSS feed and top game from file is the same
    return get_newest_file_game() == get_newest_RSS_game()

def alert():
    #Google removed less-secure-apps now must use app password
    #https://stackoverflow.com/questions/72480454/sending-email-with-python-google-disables-less-secure-apps
    #send email if games are not the same
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
        email_address = get_sendfrom_email()
        email_password = get_apppassword()
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs=get_sendto_email(), 
        msg='subject:New Free Game! \n\n Just thought you would want to know :D')

if __name__ == '__main__':
    if not is_same_game():
        alert()
        update_game_list()