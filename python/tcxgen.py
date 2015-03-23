"""
                                                                          
  Module:       tcxgen.py                                                 
                                                                          
  Programmer:   Julian M. Toumey                                          
                Madison, WI                                               
                                                                          
  Date:         March 2015                                                
                                                                          
  Language:     Python                                                    
                                                                          
  Description:  This code generates *.tcx files according to 
                specifications that you enter. The random noise portion
                attempts to add noise to an average signal (such as HR,
                power, etc.) so it looks realistic.
                                                                          
"""


from __future__ import print_function
from math import *

## Function for calculating calorie expenditure from duration and avg HR

def calorie_calc(hr_avg,duration_second):
    #
    # Subject-specific data
    #
    AGE    = 22.  # [yr]
    WEIGHT = 64.4 # [kg]
    #
    # Convert workout duration to minutes
    #
    duration_minute = duration_second/60.
    #
    # Compute calories burned
    #
    calories = ((AGE*0.2017) + (WEIGHT*0.1988) + (hr_avg*0.6309) - 55.0969)*duration_minute/4.184
    #
    return int(floor(calories))

## Function to increment the time that the code prints in the *.tcx file

def increment_time(st_time):
    #
    # Split the current time (CHAR) into an array based on `:' delimiter and convert to INT
    #
    st_time = st_time.split(':')
    st_time = map(int, st_time)
    #
    # Begin increment
    #
    # Seconds test
    if st_time[2] < 59:
        st_time[2] = st_time[2] + 1
    # move to next minute
    else:
        st_time[2] = 0
        # Minutes test
        if st_time[1] < 59:
            st_time[1] = st_time[1] + 1
        # move to next hour
        else:
            st_time[1] = 0
            st_time[0] = st_time[0] + 1
    # map the new time (INT array) back to a string
    st_time = map(str, st_time)
    # format the time with two characters per time division and a `0' in front if just one digit
    st_time[:] = [i.rjust(2,'0') for i in st_time]
    # join the array, splitting each time division with `:'
    current_time = ':'.join(st_time)
    #
    return current_time

## BEGIN MAIN PROGRAM

#
#...Constants for conversion
#
MI_TO_METER = 1609.34
HR_TO_SEC   = 3600.
MIN_TO_SEC  = 60.
# 
#...Query user for filename
#
#fname = raw_input('Enter a file name to generate: ')
#print("\nFilename is: ",fname,'.tcx',sep='')
fname = 't'
#
#...Query user for file specifics
#
st_time = '2023-02-17-21:45:12'
#st_time = raw_input('Enter Start time using 24 hr time,\n [YYYY-MM-DD-hh:mm:ss]: ')
#st_time = st_time.split('-')
st_spl  = st_time.rfind('-')
st_date = st_time[0:st_spl]
st_time = st_time[st_spl+1:]

# Workout Duration
#duration = raw_input('Enter duration [hh:mm:ss]: ')
duration = '01:01:12'
duration = duration.split(':') # split the string 
# Create individual components for each part of duration
duration_hour   = float(duration[0])
duration_minute = float(duration[1])
duration_second = float(duration[2])

# Sum the components of duration for total seconds
duration_second = duration_hour*HR_TO_SEC + duration_minute*MIN_TO_SEC + duration_second

# Workout Distance
#distance = raw_input('Enter distance [mi]      : ')
distance = 5.
distance = float(distance) # convert string (from raw_input) to float
distance_meter = distance*MI_TO_METER # convert distance to meters

# Calories
#tot_cal = raw_input('Enter total : ')

# calculate calories from heart rate
# average heart rate
hr_avg = 165
#hr_avg = raw_input('Enter average heart rate [bpm]: ')
hr_avg = int(hr_avg) # convert string (raw_input) to INT

# max heart rate
hr_max = 178
#hr_avg = raw_input('Enter average heart rate [bpm]: ')
hr_avg = int(hr_avg) # convert STR to INT

# calculate calorie expenditure
cal_tot = calorie_calc(hr_avg,duration_second)

# Altitude
altitude = 272. # [m] for test
#altitude = raw_input('Enter average altitude [m]: ')
altitude = int(altitude)

# concatenate file name and extension
exten = '.tcx'
fname = fname + exten
# open file to write
f = open(fname,'w')

#
#...Write the header information
#
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
f.write('<TrainingCenterDatabase xmlns="http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.garmin.com/xmlschemas/ActivityExtension/v2 http://www.garmin.com/xmlschemas/ActivityExtensionv2.xsd http://www.garmin.com/xmlschemas/FatCalories/v1 http://www.garmin.com/xmlschemas/fatcalorieextensionv1.xsd http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2 http://www.garmin.com/xmlschemas/TrainingCenterDatabasev2.xsd">\n')
f.write('  <Activities>\n')
f.write('    <Activity Sport="Biking">\n')
f.write('      <Id>{0}T{1}Z</Id>\n'.format(st_date,st_time))
f.write('      <Lap StartTime="{0}T{1}Z">\n'.format(st_date,st_time))
f.write('        <TotalTimeSeconds>{0:.7f}</TotalTimeSeconds>\n'.format(duration_second))
f.write('        <DistanceMeters>{0:.7f}</DistanceMeters>\n'.format(distance_meter))
f.write('        <Calories>{0}</Calories>\n'.format(cal_tot))
f.write('        <AverageHeartRateBpm>\n')
f.write('          <Value>{0}</Value>\n'.format(hr_avg))
f.write('        </AverageHeartRateBpm>\n')
f.write('        <MaximumHeartRateBpm>\n')
f.write('          <Value>{0}</Value>\n'.format(hr_max))
f.write('        </MaximumHeartRateBpm>\n')
f.write('        <Intensity>Active</Intensity>\n')
f.write('        <TriggerMethod>Manual</TriggerMethod>\n')

# Begin track points

# Initial track statement
f.write('        <Track>\n')

# Track point loop 
for ii in range(0,int(duration_second)):
    # Increment the time
    st_time = increment_time(st_time)
    # Write the information
    f.write('          <Trackpoint>\n')
    f.write('            <Time>{0}T{1}Z</Time>\n'.format(st_date,st_time))
    f.write('            <AltitudeMeters>{0:.7f}</AltitudeMeters>\n'.format(altitude))
    f.write('            <HeartRateBpm>\n')
    f.write('              <Value>94</Value>\n')
    f.write('            </HeartRateBpm>\n')
    f.write('          </Trackpoint>\n')

# End track point data
f.write('        </Track>\n')
f.write('        <Extensions>\n')
f.write('          <FatCalories xmlns="http://www.garmin.com/xmlschemas/FatCalories/v1">\n')
f.write('            <Value>0</Value>\n')
f.write('          </FatCalories>\n')
f.write('          <LX xmlns="http://www.garmin.com/xmlschemas/ActivityExtension/v2">\n')
f.write('            <AvgSpeed>{0:.7f}</AvgSpeed>\n'.format(distance/duration_hour))
f.write('          </LX>\n')
f.write('        </Extensions>\n')
f.write('      </Lap>\n')
f.write('      <Creator xsi:type="Device_t">\n')
f.write('        <Name>edge500</Name>\n')
f.write('        <UnitId>3805951086</UnitId>\n')
f.write('        <ProductID>1036</ProductID>\n')
f.write('        <Version>\n')
f.write('          <VersionMajor>3</VersionMajor>\n')
f.write('          <VersionMinor>30</VersionMinor>\n')
f.write('        </Version>\n')
f.write('      </Creator>\n')
f.write('    </Activity>\n')
f.write('  </Activities>\n')
f.write('</TrainingCenterDatabase>\n')

f.close()