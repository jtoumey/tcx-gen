from __future__ import print_function


# 
# Query user for filename
#
fname = raw_input('Enter a file name to generate: ')
print("Filename is: ",fname,'.tcx',sep='')

# concatenate file name and extension
exten = '.tcx'
fname = fname + exten
# open file to write
f = open(fname,'w')


#
#...Write the header information
#
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')





f.close()
