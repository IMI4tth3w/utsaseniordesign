# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 09:11:57 2016

@author: seniordesign
"""

#Created by Heath Spidle

import mne
import numpy as np
import matplotlib.pyplot as plt
import Tkinter as tk
import tkFileDialog as filedialog

##  Setup Import File -------------------

#data_path = '/home/seniordesign/Desktop/Data/'
#look for function to have user select data
#fname = 'record_Key_Stimulation-[2016.09.23-11.42.59].edf'
#raw_fname = data_path + fname

root = tk.Tk()
root.withdraw()
raw_fname = filedialog.askopenfilename()



print raw_fname

# Read EDF File
data = mne.io.read_raw_edf(raw_fname, preload = True)
data1 = mne.find_events(data)
data2 = mne.Epochs(data, data1)

mne.viz.plot_raw(data, scalings='auto')
mne.viz.plot_events(data1)
mne.viz.plot_epochs(data2, scalings='auto')

# http://martinos.org/mne/stable/generated/mne.io.Raw.html#mne.io.Raw
# Export data as Pandas.data file
# data.to_data_frame(raw.fif, raw.fif.gz, raw_sss.fif, raw_sss.fif.gz, raw_tsss.fif or raw_tsss.fif.gz.)
# data.save(fname)
# data.pick_types(EEG = True)
# data.plot_psd(tmin=0.0, tmax=60.0, fmin=0, fmax=inf, proj=False, n_fft=2048, picks=None, ax=None, color='black', area_mode='std', area_alpha=0.33, n_overlap=0, dB=True, show=True, n_jobs=1, verbose=None)
#
# pandas.DataFrame.to_csv()

#


