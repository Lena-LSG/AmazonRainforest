import h5py
import mapplot
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter



#create empty array to store file names

name = []
NDVI = 0
ysd = []
month = 5
year = 2002

outdata = open("NDVI_outdata.txt","w")
outdata.close()

#full directory path (use pwd in terminal once cd into correct location)

#make sure this file contains ALL 120 NDVI files in h5

directory = r'..\..\Data\NDVI\h5'

 

#each filename ending in .h5 in this directory is added to name array

for filename in os.listdir(directory):

    if filename.endswith(".h5"):

        name.append(os.path.join(filename))

    else:

        continue

### Modify the lines below ####################################################

i = 0

while i < 234:  #(change to your number of files)

    if(month + 1) == 13:

     print(NDVI)
     print(ysd)

     if(year == 2002 and month == 12):
      NDVI = NDVI/7
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)


      date = str(year)
      outdata = open("yearly_NDVI_outdata.txt","a")
      outdata.write(date + " " + str(NDVI) + " " + str(yearSd) + "\n")

      NDVI = 0
      ysd = []

     elif(month == 12):
      NDVI = NDVI/12
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)


      date = str(year)
      outdata = open("yearly_NDVI_outdata.txt","a")
      outdata.write(date + " " + str(NDVI) + " " + str(yearSd) + "\n")

      NDVI = 0
      ysd = []

     month = 1
     year = year + 1
     f = h5py.File(directory + '/' + name[i], 'r')
     i = i + 1

     ### Modify the lines below ####################################################

     # Set the file to read in

     #f = h5py.File(r'..\..\Data\Precipitation\h5\3A12.20150301.7.h5', 'r')

     # Set the HDF field we want to read in
     h5root = f['MOD_Grid_monthly_CMG_VI/Data Fields/CMG 0.05 Deg Monthly NDVI']


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_NDVI_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='NDVI'
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
     mean /= h5root.attrs['scale_factor']
     sd /= h5root.attrs['scale_factor']

     NDVI = NDVI + mean
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
     h5root = f['MOD_Grid_monthly_CMG_VI/Data Fields/CMG 0.05 Deg Monthly NDVI']


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_NDVI_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='NDVI'
     
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
     mean /= h5root.attrs['scale_factor']
     sd /= h5root.attrs['scale_factor']
     NDVI = NDVI + mean
     ysd.append(mean)

     if(year == 2021 and month == 11):
      NDVI = NDVI/11
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_NDVI_outdata.txt","a")
      outdata.write(date + " " + str(NDVI) + " " + str(yearSd) + "\n")

      NDVI = 0
      ysd = []


     #data[np.where(data == h5root.fillvalue)] = np.nan
     data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
     #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

     # # Plot and save the thing
     mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label)



    

