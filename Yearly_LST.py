import h5py
import mapplot
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter



#create empty array to store file names

name = []
LST = 0
ysd = []
month = 0
year = 2002

outdata = open("yearly_LST_outdata.txt","w")
outdata.close()

#full directory path (use pwd in terminal once cd into correct location)

#make sure this file contains ALL 120 NDVI files in h5

directory = r'..\..\Data\LST\h5\Yearly'

 

#each filename ending in .h5 in this directory is added to name array

for filename in os.listdir(directory):

    if filename.endswith(".h5"):

        name.append(os.path.join(filename))

    else:

        continue

### Modify the lines below ####################################################

i = 0

while i < 241:  #(change to your number of files)

    if(month + 1) == 13:

     if(year == 2000 and month == 12):
      LST = LST/11
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_LST_outdata.txt","a")
      outdata.write(date + " " + str(LST) + " " + str(yearSd) + "\n")

      LST = 0
      ysd = []

     elif(month == 12):
      LST = LST/12
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_LST_outdata.txt","a")
      outdata.write(date + " " + str(LST) + " " + str(yearSd) + "\n")

      LST = 0
      ysd = []

     month = 1
     year = year + 1
     f = h5py.File(directory + '/' + name[i], 'r')
     i = i + 1

     ### Modify the lines below ####################################################

     # Set the file to read in

     #f = h5py.File(r'..\..\Data\Precipitation\h5\3A12.20150301.7.h5', 'r')

     # Set the HDF field we want to read in
     h5root = f['MODIS_MONTHLY_0.05DEG_CMG_LST/Data Fields/LST_Day_CMG']


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_LST_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='LST'
     ### Don't touch the script from here on! ######################################
     ###############################################################################

     ### Calculate which parts of the big array we actually want to grab ###########
     lat_n, lon_n = h5root.shape

     north_lat = int((-lat_n / 180.0) * boxcorners[0] + lat_n / 2.0)
     south_lat = int((-lat_n / 180.0) * boxcorners[1] + lat_n / 2.0)
     west_lon = int((lon_n / 360.0) * boxcorners[2] + lon_n / 2.0)
     east_lon = int((lon_n / 360.0) * boxcorners[3] + lon_n / 2.0)

     ###############################################################################

     # Replace fill values by NaN's
     data = np.array(h5root[south_lat:north_lat,
                       west_lon:east_lon]).astype(float)

     mean = data[np.where(data != h5root.attrs['_FillValue'])].mean()
     sd = data[np.where(data != h5root.attrs['_FillValue'])].std()
     date = str(year) + str(month)
     mean *= h5root.attrs['scale_factor']
     sd *= h5root.attrs['scale_factor']

     LST = LST + mean
     ysd.append(mean)


     #data[np.where(data == h5root.fillvalue)] = np.nan
     data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
     #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

     # # Plot and save the thing
     mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label)

    else:
     month = month + 1

     f = h5py.File(directory + '/' + name[i], 'r')
     i = i + 1

     ### Modify the lines below ####################################################

     # Set the file to read in

     #f = h5py.File(r'..\..\Data\Precipitation\h5\3A12.20150301.7.h5', 'r')

     # Set the HDF field we want to read in
     h5root = f['MODIS_MONTHLY_0.05DEG_CMG_LST/Data Fields/LST_Day_CMG']


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_LST_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='LST'
     
     ### Don't touch the script from here on! ######################################
     ###############################################################################

     ### Calculate which parts of the big array we actually want to grab ###########
     lat_n, lon_n = h5root.shape

     north_lat = int((-lat_n / 180.0) * boxcorners[0] + lat_n / 2.0)
     south_lat = int((-lat_n / 180.0) * boxcorners[1] + lat_n / 2.0)
     west_lon = int((lon_n / 360.0) * boxcorners[2] + lon_n / 2.0)
     east_lon = int((lon_n / 360.0) * boxcorners[3] + lon_n / 2.0)

     ###############################################################################

     # Replace fill values by NaN's
     data = np.array(h5root[south_lat:north_lat,
                       west_lon:east_lon]).astype(float)

     mean = data[np.where(data != h5root.attrs['_FillValue'])].mean()
     sd = data[np.where(data != h5root.attrs['_FillValue'])].std()
     date = str(year) + str(month)
     mean *= h5root.attrs['scale_factor']
     sd *= h5root.attrs['scale_factor']
     LST = LST + mean
     ysd.append(mean)

     #if(year == 2021 and month == 11):
      #LST = LST/11
      #ysd = ysd/11

      #date = str(year)
      #outdata = open("yearly_NDVI_outdata.txt","a")
      #outdata.write(date + " " + str(NDVI) + " " + str(ysd) + "\n")

      #LST = 0
      #ysd = 0


     #data[np.where(data == h5root.fillvalue)] = np.nan
     data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
     #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

     # # Plot and save the thing
     mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label)



    

