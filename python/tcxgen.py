from __future__ import print_function


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
duration = '03:45:12'
duration = duration.split(':') # split the string 
# Create individual components for each part of duration
duration_hour   = float(duration[0])
duration_minute = float(duration[1])
duration_second = float(duration[2])

# Sum the components of duration for total seconds
duration_second = duration_hour * HR_TO_SEC + duration_minute * MIN_TO_SEC + duration_second

# Workout Distance
#distance = raw_input('Enter distance [mi]      : ')
distance = 5.
distance = float(distance) # convert string (from raw_input) to float


##
#
#...Convert inputs to the format necessary for *.tcx files
#
##
distance_meter = distance * MI_TO_METER


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
#f.write('      <Lap StartTime="2015-02-25T22:33:51Z">\n')
#print("\nFilename is: ",fname,'.tcx',sep='')
f.write('        <TotalTimeSeconds>{0:.7f}</TotalTimeSeconds>\n'.format(duration_second))
f.write('        <DistanceMeters>{0:.7f}</DistanceMeters>\n'.format(distance_meter))
f.write('        <Calories>335</Calories>\n')
f.write('        <AverageHeartRateBpm>\n')
f.write('          <Value>154</Value>\n')
f.write('        </AverageHeartRateBpm>\n')
f.write('        <MaximumHeartRateBpm>\n')
f.write('          <Value>169</Value>\n')
f.write('        </MaximumHeartRateBpm>\n')
f.write('        <Intensity>Active</Intensity>\n')
f.write('        <TriggerMethod>Manual</TriggerMethod>\n')
#        <Track>
#          <Trackpoint>
#            <Time>2015-02-25T22:33:51Z</Time>
#            <AltitudeMeters>272.2000000</AltitudeMeters>
#            <HeartRateBpm>
#              <Value>94</Value>
#            </HeartRateBpm>
#          </Trackpoint>



f.close()
