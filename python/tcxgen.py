from __future__ import print_function


#
#... Constants
#
MI_TO_METER = 1609.34


# 
#...Query user for filename
#
fname = raw_input('Enter a file name to generate: ')
print("\nFilename is: ",fname,'.tcx',sep='')

#
#...Query user for file specifics
#
#st_time  = raw_input('Enter Start time using 24 hr time,\n [YYYY-MM-DD-hh:mm:ss]: ')

# Workout Duration
#duration = raw_input('Enter duration [hh:mm:ss]: ')



# Workout Distance
distance = raw_input('Enter distance [mi]: ')
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
f.write('      <Id>2015-02-25T22:33:51Z</Id>\n')
f.write('      <Lap StartTime="2015-02-25T22:33:51Z">\n')
f.write('        <TotalTimeSeconds>1590.6140000</TotalTimeSeconds>\n')
f.write('        <DistanceMeters>{0:.7f}</DistanceMeters>\n'.format(distance_meter))
#f.write('        <DistanceMeters>0.0000000</DistanceMeters>\n')
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
