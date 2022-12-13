#!/usr/bin/env python2.7
 
import sys
import os, glob
import csv 
import numpy as np
import xarray as xr
import calendar
import matplotlib
import matplotlib.pyplot as plt 
from datetime import datetime, date, timedelta
import pandas as pd
import scipy
from scipy.optimize import curve_fit


def vpd_from_rh(T,RH):
    """Calculate Vapor Pressure Deficit (kPa) from Temperature (C) and RH (%)
    Parameters : T   : Temperature (C)
                 RH  : Relative Humidity (%)
    Returns    : VPD : vapor pressure deficit (kPa)"""

    for x in range(0,len(RH)):
        if RH[x]<0:
            RH[x]=40

    # convert input variables
    TK = T+273.15 # convert temperature from celcius to Kelvin

    # Calculate VPD using Emanuel 1994 equations for saturated vapor pressure (es)
    es = np.exp(53.67957 - (6743.769/TK) - 4.8451*np.log(TK))
    ea = (RH/100)*es
    VPD = es-ea
    VPD = VPD/10 # convert hPa to kPa

    return VPD
