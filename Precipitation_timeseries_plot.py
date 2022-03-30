import h5py 
import datetime
from datetime import timedelta # Import date handler from python.
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter #Import ticker formatter.
import matplotlib.dates as mdates # Import matplotlib date handler.


fdata = open('yearly_rainy_Precipitation_outdata.txt', 'r') # Open data file in read-only mode.
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

fig, ax = plt.subplots() # Get all plots stored by matplotlib.
ax.ticklabel_format(axis="y", useOffset=False) # Change y-axis offset.
ax.yaxis.set_major_formatter(FormatStrFormatter('%0.2f')) # Display y tics as %0.2f data.
#plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right') # Rotate x tics for clear display.
fdates = [datetime.datetime.strptime(d,"%Y").date() for d in fdate] # Convert date strings into true date-time format.

x = mdates.date2num(fdates)
z, V = np.ma.polyfit(x, fmean, 1, cov = True)
p = np.poly1d(z)
print("x_1: {} +/- {}".format(z[0], np.sqrt(V[0][0])))
slope = z[0]
serror = np.sqrt(V[0][0])
terror = serror * (len(fdates) * 30)
terror = "{:.3f}".format(terror)
tChange = slope * (len(fdates) * 30)
print(tChange)
tChange = "{:.3f}".format(tChange)


plt.figure(figsize=(100,50))
plt.plot(fdates,fmean,'b-', linewidth=10) # Plot the data as a line graph.
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y')) # Display x-tics as dates with given format. (I am only showing year and month.)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(12)))
plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
plt.fill_between(fdates,fmean+fsd,fmean-fsd,alpha=0.5,facecolor='lightgrey',edgecolor='grey') # Show errors from standard deviation as grey region.
plt.xlim([x[0],x[-1]])
plt.xticks(size=80) # Plot x tics using formatted date-time array.
plt.yticks(size=80)
plt.text(fdates[1],0.75, "Total Precipitation Change = " + tChange + " +/- " + terror + " (mm/hr)", fontsize = 80)
plt.plot(x, p(x), "b--", linewidth=10)
ax.tick_params(axis='both', which='major', labelsize=40)
plt.title("Yearly Rainy Season Precipitation (mm/hr)", size = 100) # Set figure title.
plt.xlabel("Date (YYYY-MM)", size = 100) # Set x-axis label.
plt.ylabel("Average Yearly Rainy Season Precipitation (mm/hr)", size = 100) # Set y-axis label.
plt.savefig("Yearly_Rainy_Precipitation_Time_Series.png") # Save plot as a png.