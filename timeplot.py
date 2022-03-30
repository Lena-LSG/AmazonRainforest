import h5py 
import datetime
from datetime import timedelta # Import date handler from python.
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter #Import ticker formatter.
import matplotlib.dates as mdates # Import matplotlib date handler.


fdata = open('outdata.txt', 'r') # Open data file in read-only mode.
lines = fdata.readlines() # Read all lines of the data file.
fdate = [line.split()[0] for line in lines] # Split data into columns as appropriate.
fmean = [line.split()[1] for line in lines]
fsd = [line.split()[2] for line in lines]
fdate = np.array(fdate) # Create numpy arrays of the data.
fmean = np.array(fmean)
fsd = np.array(fsd)
fmean = fmean.astype(np.float64) # Store as floating point data for accuracy.
fsd = fsd.astype(np.float64)

fig, ax = plt.subplots() # Get all plots stored by matplotlib.
ax.ticklabel_format(axis="y", useOffset=False) # Change y-axis offset.
ax.yaxis.set_major_formatter(FormatStrFormatter('%0.2f')) # Display y tics as %0.2f data.
plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right') # Rotate x tics for clear display.
fdates = [datetime.datetime.strptime(d,"%Y%m").date() for d in fdate] # Convert date strings into true date-time format.
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # Display x-tics as dates with given format. (I am only showing year and month.)

plt.figure(figsize=(100,40))
plt.plot(fdates,fmean,marker = None) # Plot the data as a line graph.
plt.fill_between(fdates,fmean+fsd,fmean-fsd,alpha=0.5,facecolor='lightgrey',edgecolor='grey') # Show errors from standard deviation as grey region.
plt.xticks(size=40) # Plot x tics using formatted date-time array.
plt.yticks(size=40)
ax.tick_params(axis='both', which='major', labelsize=40)
plt.title("Precipitation Timeseries", size = 50) # Set figure title.
plt.xlabel("Date (YYYY)", size = 50) # Set x-axis label.
plt.ylabel("Monthly Average Precipitation (mm/hr)", size = 50) # Set y-axis label.
plt.savefig("Full_Precipitation_Time_Series.png") # Save plot as a png.