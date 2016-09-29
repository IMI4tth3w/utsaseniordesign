#Created by Heath Spidle

import mne
import numpy as np
import matplotlib.pyplot as plt

##  Setup Import File -------------------

#data_path = '/home/seniordesign/Desktop/Data/'
##look for function to have user select data
#fname = 'record-[2016.09.22-13.49.32].csv'
#raw_fname = data_path + fname


import Tkinter as tk
import tkFileDialog as filedialog


root = tk.Tk()
root.withdraw()
raw_fname = filedialog.askopenfilename()

print raw_fname



# --------------------------------------------------------

# http://martinos.org/mne/dev/generated/mne.io.Raw.html
# http://martinos.org/mne/stable/python_reference.html#reading-raw-data

# importing data types
# http://martinos.org/mne/stable/manual/io.html#ch-convert

# Read the CSV file as a NumPy array
data = np.genfromtxt(raw_fname, delimiter=';',skip_header=2, dtype=float, usecols=(1,2,3,4,5,6,7,8))

# Read EDF File
# mne.io.read_raw_edf()

#data = np.loadtxt(raw_fname, delimiter=';',skiprows=2)
data = data.transpose()
data = data*0.0001
(x,y) = data.shape
print data.shape
# Some information about the channels
ch_names = ['Fp1', 'Fp2', 'Fz', 'C3', 'C4', 'Pz', 'O1', 'O2']

# Sampling rate of the Nautilus machine
sfreq = 128  # Hz
t = np.arange(0, y)*1/128

info = mne.create_info(ch_names, sfreq)

raw = mne.io.RawArray(data, info)

raw.plot()


plt.figure(2)
data1 = data[1,:]
for i in range(0,7):
    plt.plot(t,data[i,:]+i*.01, linestyle='-', label = ch_names[i])

plt.axis('tight')
# plt.plot(t, data1, linestyle='-', color = 'b', label = 'Fp1')
# plt.Line2D(t, data1, 'ro')
plt.xlabel('time in s')
plt.ylabel('channel')
plt.legend()
plt.show()



# -----------------------------------------------------
plt.figure(3)
#Y1 = np.fft.fft(data1)
f = np.linspace(0,y,y)*sfreq/y
f2 = np.fft.fftfreq(y,(128))
#Y1 = np.abs(Y1[0:y/2])
Y = np.zeros((8,y))
Y2 = np.zeros((8,y/2))
for k in range(0,7):
    Y[k] = np.abs(np.fft.fft(data[k,:]))
    Y2[k] = Y[k,0:y/2]
    plt.plot(f[0:y/2],Y2[k], label = ch_names[k])


#plt.plot(f[0:y/2],Y1)
plt.xlim(0,20)
plt.ylim(0,5)
plt.legend()
plt.show()
