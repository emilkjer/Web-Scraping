#!/usr/bin/env python
    
###################################################
# RMIT University, Melbourne
# Date 27 Mar 2012
# By Emil Broegger Kjer
# For questions or comments contact emil@kjer.info
###################################################


class DataConnector:
    def __init__(self):
        pass

    def read_timetable_file(self, route_filename, weekday, direction):
        # Example of how the timetables can be read and returned as a Map
        
        from BeautifulSoup.BeautifulSoup import BeautifulSoup
        import urllib2, re, time


        filestr = ('data/timetables/%s_%s_%s.html' % (route_filename, weekday, direction))
        fil = open(filestr, "r")
        soup = BeautifulSoup(fil.read(), fromEncoding='utf8')
        fil.close()


        divs =  soup.html.body.findAll('div')
        children = divs[0].contents

        #timetable
        tt = children[1].contents[3].contents[3].contents[3].contents[1].contents[2]

        route_list = []
        route_times_list = []
        # stop names values
        for (j, name) in enumerate(tt.contents[0].contents[4].contents):

            route_times_list = []
            route_name = name.contents[1].find('a').contents[0]
            print route_name
            #am / pm values
            for (i, name) in enumerate(tt.contents[0].contents[3].contents[2].contents):
                time_value = tt.contents[0].contents[5].contents[j+1].contents[i].contents[0].text
                if time_value == '-':
                    print time_value
                    continue
                time_prefix = name.text
                #values minus the first
                time_str = ''+time_value+' '+ time_prefix
                try:
                    time_result = time.strftime('%H:%M:%S', time.strptime(time_str, '%I:%M %p'))
                    route_times_list.append(time_result)
                    print time_result
                except:
                    print "ERR", time_str

            route_list.append((route_name, route_times_list))

        return route_list
