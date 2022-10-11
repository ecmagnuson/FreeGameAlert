import os.path

def get_sendfrom_email():
    #get the email to send from
    with open(os.path.dirname(__file__) + '/auth/emailfrom','r') as f:
        return f.readline().strip()

def get_sendto_email():
    #get the email to send to
    with open(os.path.dirname(__file__) + '/auth/emailto','r') as f:
        return f.readline().strip()

def get_apppassword():
    #https://support.google.com/accounts/answer/185833?hl=en
    with open(os.path.dirname(__file__) + '/auth/app_password', 'r') as f:
        return f.readline().strip()