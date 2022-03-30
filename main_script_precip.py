import h5py
import mapplot
import numpy as np
import os
import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter



#create empty array to store file names

name = []
month = 5 # Create variables to contain starting month and year for data.
year = 2000

outdata = open("curve_outdata.txt","w") # Create a text file to hold the data.
outdata.close()

#full directory path (use pwd in terminal once cd into correct location)

#make sure this file contains ALL 120 NDVI files in h5

directory = r'..\..\Data\Precipitation\h5'

 

#each filename ending in .h5 in this directory is added to name array

for filename in os.listdir(directory):

    if filename.endswith(".HDF5"):

        name.append(os.path.join(filename))

    else:

        continue

### Modify the lines below ####################################################

for i in range(258):  #(change to your number of files)

    if(month + 1) == 13: # If a year has passed, reset the month scale and add 1 to the year.
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
    date = str(year) + "." + str(month) # Create a string to hold the date.
    outdata = open("curve_outdata.txt","a") # Open storage file in append mode.
    #if(month == 12 or month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6): # Store data for every May. (If full data is needed, just remove the if statement.)
    outdata.write(date + " " + str(mean) + " " + str(sd) + "\n")


    #data[np.where(data == h5root.fillvalue)] = np.nan
    data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
    #data /= h5root.attrs['scale_factor'] # Multiply with scale factor

    # # Plot and save the thing
    mapplot.plot(data, boxcorners=boxcorners, fname=fname,vmin = 0, vmax = 1.2, title=title, colorbar_label=colorbar_label,reverse_lat='True')

# Set the file to read in

#f = h5py.File('3B-MO.MS.MRG.3IMERG.20210101-S000000-E235959.01.V06B.HDF5', 'r')

# Set the HDF field we want to read in
#h5root = f['Grid/precipitation']
#data2d=np.reshape(h5root,(3600,1800))


 # Set the box corners of our region of interest
 # lower latitude, upper latitude, western longitude, eastern longitude
#boxcorners = [-90, 90, -180, 180]

#fname = 'Amazon_Precipitation.png'
#title = 'Month: MM, Year: YYYY'
#colorbar_label=''


# ### Don't touch the script from here on! ######################################
# ###############################################################################

# ### Calculate which parts of the big array we actually want to grab ###########
#lon_n, lat_n = data2d.shape

#north_lat = int((lat_n / 180.0) * boxcorners[0] + lat_n / 2.0)
#south_lat = int((lat_n / 180.0) * boxcorners[1] + lat_n / 2.0)

#north_lat = int((lat_n / 180.0) * (boxcorners[1] + 90.))
#south_lat = int((lat_n / 180.0) * (boxcorners[0] + 90.))

#west_lon = int((lon_n / 360.0) * (boxcorners[2] + 180.) )
#east_lon = int((lon_n / 360.0) * (boxcorners[3] + 180.) )

#west_lon = int((lon_n / 360.0) * boxcorners[2] + lon_n / 2.0)
#east_lnon = int((lon_n / 360.0) * boxcorners[3] + lon_n / 2.0)


# ###############################################################################

# # Replace fill values by NaN's

#data2d_t=np.transpose(data2d)

#data = np.array(data2d_t[south_lat:north_lat,
#                        west_lon:east_lon]).astype(float)


#data[np.where(data == h5root.fillvalue)] = np.nan
#data[np.where(data == h5root.attrs['_FillValue'])] = np.nan
#data /= h5root.attrs['scale_factor'] # Multiply with scale factor

# # Plot and save the thing
#mapplot.plot(data, boxcorners=boxcorners, fname=fname, title=title, colorbar_label='',reverse_lat='True')