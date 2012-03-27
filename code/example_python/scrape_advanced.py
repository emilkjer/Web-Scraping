#!/usr/bin/env python

###################################################
# RMIT University, Melbourne
# Date 27 Mar 2012
# By Emil Broegger Kjer
# For questions or comments contact emil@kjer.info
###################################################


from route_handling import DataConnector

print "Start reading timetable"

# Create the object for reading timetable files
dd = DataConnector()

transport_line = "epping_line"
weekday = "weekday"
direction = "true"

# Read the timetable
dd.read_timetable_file(transport_line, weekday, direction)

print "Do something to the timetable....."

print "Finished reading timetable"
