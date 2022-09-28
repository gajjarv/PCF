#!/usr/bin/env python
import os, sys, glob
import shlex
#import matplotlib.pyplot as plt
import numpy
import math
#---------------------------------------------------------------
def histogram(data,low,high,step):
        data = [int(i) for i in data]
        low = float(low)
        high = float(high)
#       step = float(high - low  + 1)/bins # For fixed number of bins 
        bins = int(math.ceil((high-low+1)/step))
        range1 = float(low)
        range2 = float(low + step)
        freq = []
        values = []
        for i in range(bins):
                k = 0
                for j in data:
                        if(range1 <= j < range2):
                                k = k + 1
#               print k,low,high                                        
                freq.append(k) # Freq of in each bin 
                values.append(range1 + (range2-range1)/2) # Middle of the bin
#               print data,freq,range1,range2
#               values.append(low)
#               values.append(high)
                range1 = range1 + step
                if(range2 < int(high)):
                        range2 = range2 + step
                if(range2 > int(high)):
                        range2 = high

#       norm = float(np.sum(freq))
#       print freq,values

#       for i in range(len(freq)):
#               freq[i]=float(freq[i])/norm
        return freq,bins,values

if __name__ == "__main__":
        if(len(sys.argv) < 4):
		print "USAGE : <burst_number> <outfile_hist> <bins>"
		print "This prog calculates the PCF from the given burst numbers. It saves the normalized PCF histogram"
		sys.exit(0)


	fp1 = open(sys.argv[1],'r')
        data1 = fp1.read().split("\n")
        fp1.close()
	
	fp3 = open(sys.argv[2],'w')
	
	inpbins = int(sys.argv[3])
	
	data2 = []
	
#	print data1

	for line1 in data1:
                if(line1 != ''):
			for line2 in data1:
				if(line2 != ''):
#					print line1,line2	
					if(abs(int(line1)-int(line2)) != 0):
						data2.append(abs(int(line1)-int(line2)))
					
	
	min1 = min(data2)
	max1 = max(data2)

	print min1,max1
	step = 10

#	data3,bins,freq = histogram(data2,min1,max1,step)

#	print data2
	
	data3,freq = numpy.histogram(data2,bins=inpbins)

	for i in range(0,len(data3)):
		fp3.write("%f %f\n" % (freq[i],data3[i]))		

	fp3.close()

#	print bins,data3
#	plt.plot(freq,data3)
#       plt.show()
	
