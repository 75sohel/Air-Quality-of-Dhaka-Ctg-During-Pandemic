import ipywidgets
from matplotlib import pyplot as plt
from termcolor import colored
import cartopy.crs as ccrs
import matplotlib.colors as colors
import xarray as xr
import numpy as np
import cartopy
import matplotlib.gridspec as gridspec
from glob import iglob
from os.path import join
from functools import reduce
import pandas as pd
from netCDF4 import Dataset
import numpy as np



product_path = "F:\mar2020"


#2019 data stored in a list
#files2019 =sorted(list(iglob(join(product_path, "*2019*.nc"), recursive =True)))
#print(colored("NO2 2019 files:","red"), len(files2019))

#2020 data stored in a different list
files2020 = sorted(list(iglob(join(product_path, "*L3*.nc4"), recursive =True)))
print(colored("NO2 2021 files:","red"), len(files2020))


#sample file for testing on a 1stMARCH2019 data
file1 = files2020[0]
file2 = files2020[1]
print(colored("Product selected for analyis:","blue"), file1)
print(colored("Product selected for analyis:","blue"), file2)

with xr.open_dataset(file1) as file1GA:
    print(colored("Global attributes:\n", "blue"), file1GA)



#import sys
for i in files2020:
    file1GA = xr.open_dataset(i)
    no2 = file1GA['tropospheric_NO2_column_number_density']
    no2_new = np.nan_to_num(no2.values)
    no2_new_no2 = no2_new[0,319:341, 339:361]
    sumele = np.sum(no2_new_no2)
    nonzero = np.count_nonzero(no2_new_no2)
    average = sumele/nonzero
    name = i[31:39]
    print(name," = ", average)
    




























