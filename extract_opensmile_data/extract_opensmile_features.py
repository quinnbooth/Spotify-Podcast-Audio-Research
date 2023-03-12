# -*- coding: utf-8 -*-
"""
Script to automate the feature name extraction for OpenSMILE files.
"""

# Import libraries
import h5py
import pandas as pd

# Define file names
h5_file = "h5_feature_extraction.h5"
df = pd.read_csv('sample_audio_csv.csv')

# Extract and clean feature names
with h5py.File(h5_file, "r") as f:
    for group in f.keys():
        members = f[group].keys()
        for i in range(len(members)):
            member = list(members)[i]
            if i == 0:
                dataset = f[group][member]
                for feature in dataset:
                    feature_name = str(feature)[2:-1]
                    df[feature_name] = [None]*(df.shape[0])
                    
df.to_csv('named_audio_csv.csv')