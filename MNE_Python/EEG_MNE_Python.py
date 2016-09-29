# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 17:27:49 2016

@author: Heath

http://mne-tools.github.io/mne-python-intro/
Using Anaconda Python 2.7
Spyder Python 2.7

Importing EEG Data
http://martinos.org/mne/stable/manual/io.html#importing-eeg-data
http://martinos.org/mne/stable/manual/io.html#ch-convert

Sample Data
C:\Users\Heath\Anaconda2\lib\site-packages\examples\
"""
#http://martinos.org/mne/stable/auto_tutorials/plot_eeg_erp.html
import mne

from mne.datasets import sample
#data_path = sample.data_path() # Downloads the Data package
#data_path = 'C:/Users/Heath/Anaconda2/lib/site-packages/examples'
#raw_fname = data_path + '/MNE-sample-data/MEG/sample/sample_audvis_filt-0-40_raw.fif'
data_path = './EEG_Sample/MEG/sample/'
raw_fname = data_path + 'sample_audvis_filt-0-40_raw.fif'

print raw_fname
#http://martinos.org/mne/stable/python_reference.html#reading-raw-data
raw = mne.io.RawFIF(raw_fname)

print raw
#http://nullege.com/codes/search/mne.Epochs
start, stop = raw.time_as_index([100,115]) #Take only these seconds from the sample

data, times = raw[:, start:stop]

#http://mne-tools.github.io/mne-python-intro/
#http://martinos.org/mne/stable/auto_tutorials/plot_visualize_raw.html
raw.plot(block=True)
raw.plot_psd()



