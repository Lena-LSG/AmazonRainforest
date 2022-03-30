import h5py
import mapplot
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter



#create empty array to store file names

name = []
precipitation = 0
ysd = []
month = 11
year = 2000

outdata = open("yearly_Precipitation_outdata.txt","w")
outdata.close()

#full directory path (use pwd in terminal once cd into correct location)

#make sure this file contains ALL 120 NDVI files in h5

directory = r'..\..\Data\Precipitation\h5\Yearly'

 

#each filename ending in .h5 in this directory is added to name array

for filename in os.listdir(directory):

    if filename.endswith(".HDF5"):

        name.append(os.path.join(filename))

    else:

        continue

### Modify the lines below ####################################################

i = 0

for i in range(258):  #(change to your number of files)

    if(month + 1) == 13:

     if(year == 2000 and month == 12):
      precipitation = precipitation/7
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_Precipitation_outdata.txt","a")
      outdata.write(date + " " + str(precipitation) + " " + str(yearSd) + "\n")

      precipitation = 0
      ysd = []

     elif(month == 12):
      precipitation = precipitation/12
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_Precipitation_outdata.txt","a")
      outdata.write(date + " " + str(precipitation) + " " + str(yearSd) + "\n")

      precipitation = 0
      ysd = []

     month = 1
     year = year + 1
     f = h5py.File(directory + '/' + name[i], 'r')

     ### Modify the lines below ####################################################

     # Set the file to read in

     #f = h5py.File(r'..\..\Data\Precipitation\h5\3A12.20150301.7.h5', 'r')

     # Set the HDF field we want to read in
     h5root = f['Grid/precipitation']
     data2d=np.reshape(h5root,(3600,1800))


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_Precipitation_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='Precipitation (mm/hr)'
    

     precipitation = precipitation + mean
     ysd.append(mean)


     #data[np.where(data == h5root.fillvalue)] = np.nan
     data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
     #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

     # # Plot and save the thing
     mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label)

    else:
     month = month + 1
     f = h5py.File(directory + '/' + name[i], 'r')

     ### Modify the lines below ####################################################

     # Set the file to read in

     #f = h5py.File(r'..\..\Data\Precipitation\h5\3A12.20150301.7.h5', 'r')

     # Set the HDF field we want to read in
     h5root = f['Grid/precipitation']
     data2d=np.reshape(h5root,(3600,1800))


     # Set the box corners of our region of interest
     # lower latitude, upper latitude, western longitude, eastern longitude
     boxcorners = [-2, 2, -60, -53]

     fname = 'Amazon_Precipitation_' + str(month) + '.png'
     title = 'Month: ' + str(month) + ', Year: ' + str(year)
     colorbar_label='Precipitation (mm/hr)'



     ### Don't touch the script from here on! ######################################
     ###############################################################################

     ### Calculate which parts of the big array we actually want to grab ###########
     lon_n, lat_n = data2d.shape

     north_lat = int((lat_n / 180.0) * (boxcorners[1] + 90.))
     south_lat = int((lat_n / 180.0) * (boxcorners[0] + 90.))

     west_lon = int((lon_n / 360.0) * (boxcorners[2] + 180.) )
     east_lon = int((lon_n / 360.0) * (boxcorners[3] + 180.) )

     ###############################################################################

     data2d_t=np.transpose(data2d)

     data = np.array(data2d_t[south_lat:north_lat,
                         west_lon:east_lon]).astype(float)

     mean = data[np.where(data != h5root.attrs['_FillValue'])].mean() # Calculate mean of data array.
     sd = data[np.where(data != h5root.attrs['_FillValue'])].std() # Calculate standard deviation of array.
     date = str(year) + str(month) # Create a string to hold the date.
     outdata = open("rainy_outdata.txt","a") # Open storage file in append mode.
     precipitation = precipitation + mean
     ysd.append(mean)

     if(year == 2021 and month == 9):
      precipitation = precipitation/9
      sdArray = np.array(ysd)
      yearSd = sdArray.std()
      print(ysd)
      print(sdArray)
      print(yearSd)

      date = str(year)
      outdata = open("yearly_Precipitation_outdata.txt","a")
      outdata.write(date + " " + str(precipitation) + " " + str(yearSd) + "\n")

      precipitation = 0
      ysd = []


     #data[np.where(data == h5root.fillvalue)] = np.nan
     data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
     #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

     # # Plot and save the thing
     mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label)



    

