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
df = pd.read_csv('named_audio_csv.csv', index_col = 0)
outfile_name = "sample_final_dataset.csv"

feature_names = df.columns[3:] # first element should be first audio feature name

# Iterate through H5 subdirectories
directory = 'sample_h5_dir'
for subdir in os.listdir(directory):
    
    # Check that subdir is a podcast show directory
    if subdir[:4] == "show":
        show_URI = subdir
        subdir_path = os.path.join(directory, subdir)
        
        show_feature_means = []
        # Iterate through files in subdir
        for filename in os.listdir(subdir_path):
            file = os.path.join(subdir_path, filename)
            file_extension = pathlib.Path(file).suffix
            
            # Check that file is an H5 file
            if os.path.isfile(file) and file_extension == '.h5':
                episode_URI = filename[:-3]
                
                # Extract OpenSMILE data
                with h5py.File(file, "r") as f:
                    for group in f.keys():
                        members = f[group].keys()
                        for i in range(len(members)):
                            member = list(members)[i]
                            if i == 3: # Holds audio feature values
                                dataset = f[group][member][:]
                                
                                # Each row represents the feature values within a 0.48s interval
                                # Each column represents a distinct feature
                                ## Hence, 88 columns
                                # Should take the mean over columns, not rows
                                
                                episode_feature_means = dataset.mean(axis = 0)
                                show_feature_means.append(episode_feature_means)
                                ## print(feature_means)
                                ## print(len(feature_means)) -- Should equal 88 (one mean val per feature)
    
        show_feature_means = np.array(show_feature_means)
        for i in range(len(feature_names)):
            feature_name = feature_names[i]
            val_array = show_feature_means[:, i]
            # print(feature_name, val_array)
            
            current_row = df.loc[df['show_URI'] == show_URI]
            current_row[feature_name] = val_array
    
"""

# Export to CSV
#df.to_csv(outfile_name)
"""              