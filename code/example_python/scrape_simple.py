#!/usr/bin/env python

###################################################
# RMIT University, Melbourne
# Date 27 Mar 2012
# By Emil Broegger Kjer
# For questions or comments contact emil@kjer.info
###################################################


from BeautifulSoup.BeautifulSoup import BeautifulSoup
import urllib2, re

#### Read from URL
page = urllib2.urlopen("http://tt.metlinkmelbourne.com.au/tt/XSLT_TTB_REQUEST?command=direct&language=en&outputFormat=0&net=vic&line=02EPP&project=ttb&itdLPxx_selLineDir=R&sup=B")
soup = BeautifulSoup(page)


#### Read from file
# transport_line = "epping_line"
# weekday = "weekday"
# direction = "true"
# filestr = ('data/timetables/%s_%s_%s.html' % (transport_line, weekday, direction))
# fil = open(filestr, "r")
# soup = BeautifulSoup(fil.read(), fromEncoding='utf8')
# fil.close()


divs =  soup.html.body.findAll('div')
children = divs[0].contents

#### Set the timetable
tt = children[1].contents[3].contents[3].contents[3].contents[1].contents[2]


#### Show all stop names
print "List of all stops/stations"
for name in tt.contents[0].contents[4].contents:
    print name.contents[1].find('a').contents[0]


#### Show all am / pm values
# print "All am / pm values"
# for name in tt.contents[0].contents[3].contents[2].contents:
#     print name.text


#### Read a timetable line where X in tt.contents[0].contents[5].contents[X] is the stop number
# print "A timetable line"
# for name in tt.contents[0].contents[5].contents[1].contents:
#     print name.contents[0].text

#### BONUS: Great python debugger tool
# import ipdb; ipdb.set_trace()
