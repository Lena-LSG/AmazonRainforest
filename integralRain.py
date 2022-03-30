import h5py 
import datetime
from datetime import timedelta # Import date handler from python.
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter #Import ticker formatter.
import matplotlib.dates as mdates # Import matplotlib date handler.

fdata = open('rainy_outdata.txt', 'r') # Open data file in read-only mode.
lines = fdata.readlines() # Read all lines of the data file.
fdate = [line.split()[0] for line in lines] # Split data into columns as appropriate.
fmean = [line.split()[1] for line in lines]
fsd = [line.split()[2] for line in lines]
fdate = np.array(fdate) # Create numpy arrays of the data.
fmean = np.array(fmean)
fmean = fmean.astype(np.float64) # Store as floating point data for accuracy.
fmean = np.ma.array(fmean, mask=(fmean==0.0))
fsd = np.array(fsd)
fsd = fsd.astype(np.float64)

fdates = [datetime.datetime.strptime(d,"%Y%m").date() for d in fdate] # Convert date strings into true date-time format.
integralData = open('rain_integral.txt', 'a')
seasonInt = 0
seasonArray = []
seasonSd = 0

for i in range(len(fmean)):
	if fdates[i].month == 6:
		seasonInt = seasonInt + (fmean[i] * 720)
		seasonArray.append((fmean[i] * 720))
		seasonArray = np.array(seasonArray)
		seasonSd = seasonArray.std()
		print(seasonArray)
		print(seasonSd)
		integralData.write(str(fdates[i].year) + " " + str(seasonInt) + " " + str(seasonSd) + "\n")
		seasonInt = 0
		seasonArray = []
		
	elif fdates[i].month == 5:
		seasonInt = seasonInt + (fmean[i] * 744)
		seasonArray.append((fmean[i] * 744))

	elif fdates[i].month == 4:
		seasonInt = seasonInt + (fmean[i] * 720)
		seasonArray.append((fmean[i] * 720))

	elif fdates[i].month == 3:
		seasonInt = seasonInt + (fmean[i] * 744)
		seasonArray.append((fmean[i] * 744))

	elif fdates[i].month == 2 and (fdates[i].year == 2004 or 2008 or 2012 or 2016 or 2020):
		seasonInt = seasonInt + (fmean[i] * 696)
		seasonArray.append((fmean[i] * 696))

	elif fdates[i].month == 2:
		seasonInt = seasonInt + (fmean[i] * 672)
		seasonArray.append((fmean[i] * 672))

	elif fdates[i].month == 1:
		seasonInt = seasonInt + (fmean[i] * 744)
		seasonArray.append((fmean[i] * 744))

	elif fdates[i].month == 12:
		seasonInt = seasonInt + (fmean[i] * 744)
		seasonArray.append((fmean[i] * 744))