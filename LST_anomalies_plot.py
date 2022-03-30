import h5py 
import datetime
from datetime import timedelta # Import date handler from python.
import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter #Import ticker formatter.
import matplotlib.dates as mdates # Import matplotlib date handler.


fdata = open('LST_anomaly_outdata.txt', 'r') # Open data file in read-only mode.
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
fdates = [datetime.datetime.strptime(d,"%Y%m").date() for d in fdate] # Convert date strings into true date-time format.



janAvg = 0
janCount = 0
febAvg = 0
febCount = 0
marAvg = 0
marCount = 0
marAvg = 0
aprCount = 0
aprAvg = 0
mayCount = 0
mayAvg = 0
junCount = 0
junAvg = 0
julCount = 0
julAvg = 0
augCount = 0
augAvg = 0
sepCount = 0
sepAvg = 0
octCount = 0
octAvg = 0
novCount = 0
novAvg = 0
decCount = 0
decAvg = 0

for i in range(len(fdate)):

	l = len(fdate[i])
	month = int(fdate[i][4:])

	if month == 1:
		janCount = janCount + 1
		janAvg = janAvg + fmean[i]

	elif month == 2:
		febCount = febCount + 1
		febAvg = febAvg + fmean[i]

	elif month == 3:
		marCount = marCount + 1
		marAvg = marAvg + fmean[i]

	elif month == 4:
		aprCount = aprCount + 1
		aprAvg = aprAvg + fmean[i]

	elif month == 5:
		mayCount = mayCount + 1
		mayAvg = mayAvg + fmean[i]

	elif month == 6:
		junCount = junCount + 1
		junAvg = junAvg + fmean[i]

	elif month == 7:
		julCount = julCount + 1
		julAvg = julAvg + fmean[i]

	elif month == 8:
		augCount = augCount + 1
		augAvg = augAvg + fmean[i]

	elif month == 9:
		sepCount = sepCount + 1
		sepAvg = sepAvg + fmean[i]

	elif month == 10:
		octCount = octCount + 1
		octAvg = octAvg + fmean[i]

	elif month == 11:
		novCount = novCount + 1
		novAvg = novAvg + fmean[i]

	elif month == 12:
		decCount = decCount + 1
		decAvg = decAvg + fmean[i]


janAvg = janAvg / janCount
febAvg = febAvg / febCount
marAvg = marAvg / marCount
aprAvg = aprAvg / aprCount
mayAvg = mayAvg / mayCount
junAvg = junAvg / junCount
julAvg = julAvg / julCount
augAvg = augAvg / augCount
sepAvg = sepAvg / sepCount
octAvg = octAvg / octCount
novAvg = novAvg / novCount
decAvg = decAvg / decCount

for j in range(len(fdate)):
	l = len(fdate[j])
	month = int(fdate[j][4:])

	if month == 1:
		fmean[j] = fmean[j] - janAvg

	elif month == 2:
		fmean[j] = fmean[j] - febAvg

	elif month == 3:
		fmean[j] = fmean[j] - marAvg

	elif month == 4:
		fmean[j] = fmean[j] - aprAvg

	elif month == 5:
		fmean[j] = fmean[j] - mayAvg

	elif month == 6:
		fmean[j] = fmean[j] - junAvg

	elif month == 7:
		fmean[j] = fmean[j] - julAvg

	elif month == 8:
		fmean[j] = fmean[j] - augAvg

	elif month == 9:
		fmean[j] = fmean[j] - sepAvg

	elif month == 10:
		fmean[j] = fmean[j] - octAvg

	elif month == 11:
		fmean[j] = fmean[j] - novAvg

	elif month == 12:
		fmean[j] = fmean[j] - decAvg

print(fmean)

x = mdates.date2num(fdates)
z, V = np.ma.polyfit(x, fmean, 1, cov = True)
p = np.poly1d(z)
print("x_1: {} +/- {}".format(z[0], np.sqrt(V[0][0])))
slope = z[0]
serror = np.sqrt(V[0][0])
terror = serror * len(fmean)
terror = "{:.3f}".format(terror)
tChange = slope * len(fmean)
tChange = "{:.3f}".format(tChange)

plt.figure(figsize=(100,50))
plt.plot(fdates,fmean,'r-', linewidth=10) # Plot the data as a line graph.
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # Display x-tics as dates with given format. (I am only showing year and month.)
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(bymonth=(12)))
plt.setp(plt.gca().get_xticklabels(), rotation=30, horizontalalignment='right')
#plt.fill_between(fdates,fmean+fsd,fmean-fsd,alpha=0.5,facecolor='lightgrey',edgecolor='grey') # Show errors from standard deviation as grey region.
plt.xlim([x[0],x[-1]])
plt.xticks(size=80) # Plot x tics using formatted date-time array.
plt.yticks(size=80)
plt.text(fdates[3],2.25, "Total LST Deviation Change = " + tChange + " +/- " + terror + "K", fontsize = 80)
plt.plot(x, p(x), "y--", linewidth=10)
plt.axhline(y=0, color = "black", linestyle='-', linewidth = 10)
ax.tick_params(axis='both', which='major', labelsize=40)
plt.title("Average-Subtracted Daytime LST from Nov 2001 - Dec 2021", size = 100) # Set figure title.
plt.xlabel("Date (YYYY-MM)", size = 100) # Set x-axis label.
plt.ylabel("Average Deviation in LST (K)", size = 100) # Set y-axis label.
plt.savefig("LST_Time_Series_Anomalies.png") # Save plot as a png.