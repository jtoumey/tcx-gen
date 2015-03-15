from __future__ import print_function
from math import *
## Function for calculating calorie expenditure from duration and avg HR

def calorie_calc(hr_avg,duration_second):
    #
    AGE  = 22.  # [yr]
    WGHT = 64.4 # [kg]
    HGHT = 178. # [cm]
    duration_minute = duration_second/60.
    ELF = 1.725
    #
    calories = ELF*(66. + (13.7*WGHT) + (5*HGHT) - (6.8*AGE))
    #
    return int(floor(calories))

def increment_time(st_time):
    
    st_time = st_time.split(':')
    st_time = map(int, st_time)
    
    if st_time[2] < 59:
        st_time[2] = st_time[2] + 1
        
    else:
        st_time[2] = 0
        
        if st_time[1] < 59:
            st_time[1] = st_time[1] + 1
        else:
            st_time[1] = 0
            st_time[0] = st_time[0] + 1
    
    st_time = map(str, st_time)

    st_time[:] = [i.rjust(2,'0') for i in st_time]
    current_time = ':'.join(st_time)
    
    return current_time

#
#... Constants
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
duration = '00:01:12'
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


##
#
#...Convert inputs to the format necessary for *.tcx files
#
##
distance_meter = distance*MI_TO_METER


# calories
#tot_cal = raw_input('Enter total : ')
## calculate calories from heart rate

# average heart rate
hr_avg = 165
#hr_avg = raw_input('Enter average heart rate [bpm]: ')
hr_avg = int(hr_avg)

# max heart rate
hr_max = 178
#hr_avg = raw_input('Enter average heart rate [bpm]: ')
hr_avg = int(hr_avg)


cal_tot = calorie_calc(hr_avg,duration_second)

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

## Begin track points
# Initial track statement
f.write('        <Track>\n')

# Track point loop 
for ii in range(0,int(duration_second)):
    # Increment the time
    st_time = increment_time(st_time)
    # Write the information
    f.write('          <Trackpoint>\n')
    f.write('            <Time>{0}T{1}Z</Time>\n'.format(st_date,st_time))
    f.write('            <AltitudeMeters>272.2000000</AltitudeMeters>\n')
    f.write('            <HeartRateBpm>\n')
    f.write('              <Value>94</Value>\n')
    f.write('            </HeartRateBpm>\n')
    f.write('          </Trackpoint>\n')

# End track point data
f.write('        </Track>\n')


f.close()




