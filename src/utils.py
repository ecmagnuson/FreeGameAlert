from os.path import dirname, abspath

def get_sendfrom_email():
    #get the email to send from
    with open(dirname(dirname(abspath(__file__))) + '/auth/emailfrom','r') as f:
        return f.readline().strip()

def get_sendto_email():
    #get the email to send to
    with open(dirname(dirname(abspath(__file__))) + '/auth/emailto','r') as f:
        return f.readline().strip()

def get_apppassword():
    #https://support.google.com/accounts/answer/185833?hl=en
    with open(dirname(dirname(abspath(__file__))) + '/auth/app_password', 'r') as f:
        return f.readline().strip()

def get_newest_file_game():
    #get newest game on top of file
    with open(dirname(dirname(abspath(__file__))) + '/games.txt', 'r') as f:
        return f.readline().strip()