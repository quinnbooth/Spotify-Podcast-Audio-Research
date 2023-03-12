# -*- coding: utf-8 -*-
"""
Script to automate the data extraction for OpenSMILE files.
"""

# Import libraries
import h5py
import pandas as pd
import numpy as np
import os
import pathlib

# Define file names
df = pd.read_csv('named_audio_csv.csv')
outfile_name = "sample_final_dataset.csv"

feature_names = df.columns[3:] # first element should be first audio feature name

# Iterate through H5 subdirectories and files in h5_files directory
directory = 'sample_h5_dir'
for subdir in os.listdir(directory):
    if subdir[:4] == "show":
        subdir_path = os.path.join(directory, subdir)
        for filename in os.listdir(subdir_path):
            file = os.path.join(subdir_path, filename)
            file_extension = pathlib.Path(file).suffix
            
            # Check that file is an H5 file
            if os.path.isfile(file) and file_extension == '.h5':
                episode_URI = filename[:-3]
                print(episode_URI)
                
                # Extract OpenSMILE data
                with h5py.File(file, "r") as f:
                    for group in f.keys():
                        members = f[group].keys()
                        for i in range(len(members)):
                            member = list(members)[i]
                            if i == 3:
                                dataset = f[group][member][:]
                                
                                # Each row represents the feature values within a 0.48s interval
                                # Each column represents a distinct feature
                                ## Hence, 88 columns
                                # Should take the mean over columns, not rows
                                
                                feature_means = dataset.mean(axis = 0)
                                print(feature_means)
                                ## print(len(feature_means)) -- Should equal 88 (one mean val per feature)

"""
# Fill out appropriate row with feature means
for feature_val, feature_name in zip(feature_means, feature_names):
    # print(feature_val, feature_name)
    df[feature_name] = feature_val

# Export to CSV
#df.to_csv(outfile_name)
"""              