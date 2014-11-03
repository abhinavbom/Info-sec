#-------------------------------------------------------------------------------
# Name:        IMAP Email Backup
# Purpose:      This script can help you in creating a local backup of your emails
#               You can create a local backup from email services like gmail and yahoo
#               The script stores the emails in a local MySql server.

# Author:      darklord
#
# Created:     01/11/2014
# Copyright:   (c) darklord 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import imaplib
import email
import MySQLdb

def parse_email(raw_email):
    email_complete = email.message_from_string(raw_email)
    email_to = email_complete["To"]
    email_from = email_complete["From"]
    email_header = email_complete.items()
    email_msg = get_first_text_block(email_complete)
    con = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                        user="admin", # your username
                        passwd="pwd", # your password
                        db="sec_crawl") # name of the data base
    con.cursor().execute("INSERT INTO email VALUES (%s,%s,%s,%s)",
 (buffer(str(email_to)),buffer(str(email_from)),buffer(str(email_header)),buffer(str(email_msg))))
    con.commit()

def get_first_text_block(email_message_instance):
    maintype = email_message_instance.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message_instance.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message_instance.get_payload()

obj = imaplib.IMAP4_SSL('cp-40.webhostbox.net', 993)
obj.login('admin@securitycalculus.com','Terminat0r12!@12')
rv, mailboxes = obj.list()
if rv == 'OK':
    print "Mailboxes:"
    print mailboxes
rv, data = obj.select("INBOX")
if rv == 'OK':
    print "Processing mailbox...\n"
result, data = obj.search(None, "ALL")
ids = data[0]          # data is a list.
id_list = ids.split() # ids is a space separated string
con = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                        user="admin", # your username
                        passwd="pwd", # your password
                        db="sec_crawl") # name of the data base

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS EMAIL")
cur.execute("CREATE TABLE email(email_to TEXT,email_from TEXT,email_header TEXT, email_msg TEXT)")
con.close()

for id in id_list:
    result, data = obj.fetch(id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data[0][1]
    parse_email(raw_email)


