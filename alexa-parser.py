#-------------------------------------------------------------------------------
# Name:        Alexa-parser
# Purpose:      Following scripts parse Alexa.com for top 100 websites and cralws their robots.txt
#               to figure out what all directories are disabled in top websites
#               The result is stored in a textfile.
# Author:      darklord
#
# Created:     04/11/2014
# Copyright:   (c) darklord 2014
# Licence:     MIT
#-------------------------------------------------------------------------------

import mechanize
from bs4 import BeautifulSoup
import sys
import urllib2
import re

def robotsParse(site):
    try:
        opener=urllib2.build_opener()
        opener.addheaders= [('User-Agent','Mozilla/5.0')]
        html1=opener.open("http://www."+site+"/robots.txt")
        if "robots.txt" in html1.geturl():
            soup1=BeautifulSoup(html1)
            robots=soup1.find('html')
            robostring=robots.find(text=re.compile("Disallow"))
            if robostring:
                    robotsList=robostring.splitlines()
            for robot in robotsList:
                            if "Disallow" in robot:
                                f = open("robotslist.txt", 'r+b')
                                newlist=robot.split(':')
                                dir=newlist[1].strip()
                                f.write(dir)

    except:
        print "Sorry! Can't access robots.txt."
        return


for i in range(0,5):        #20 URLs per page. You can change the range to parse more websites
    url = 'http://www.alexa.com/topsites/global;'+str(i)
    print "opening url %s", url
    print "========================================================="
    print "========================================================="
    html = urllib2.urlopen(url)
    soup=BeautifulSoup(html,"lxml")
    table=soup.find('section',{"class":"td col-r"}) #class defining location of urls
#    print table
    div_search=table.findAll('div',{"class":"desc-container"})
#    print div_search
    for divs in div_search:
        link = divs.find('a')
        site = link.get_text().lower()
        print site
        robotsParse(site)
