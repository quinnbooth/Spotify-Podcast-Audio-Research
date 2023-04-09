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
import ast
import zipfile
import shutil

## NOTE: place this file in the same directory as metadata CSV, and as openSMILE folder
## OR: modify filepaths below

# Define file names
df = pd.read_csv('refined_metadata_v2.2.csv') # updated CSV with feature names
outfile_name = "refined_metadata_v2.3.csv"

feature_names = df.columns[11:] # change 2 to the column index at which the feature columns begin

# Iterate through H5 subdirectories                
directory = 'openSMILE' 
for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        zip_file = os.path.join(directory, filename)
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            subfolder_name = os.path.splitext(filename)[0] # extract the name of the subfolder
            zip_ref.extractall(directory) # extract the zip contents to the main directory
            subdir_path = os.path.join(directory, subfolder_name)
            show_URI = subfolder_name
            df['show_filename_prefix'] = df['show_filename_prefix'].apply(lambda x: ast.literal_eval(x)[0] if show_URI in x else x)
            show_feature_means = []
            
            for filename in os.listdir(subdir_path):
                file = os.path.join(subdir_path, filename)
                file_extension = pathlib.Path(file).suffix
                if file_extension == '.h5':
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
                                    ## print(len(show_feature_means)) # -- Should equal 88 (one mean val per feature)
                                
                os.remove(file)
    
            show_feature_means = np.array(show_feature_means)
            for i in range(len(feature_names)):
                feature_name = feature_names[i]
                val_array = show_feature_means[:, i]
                df.loc[df.show_filename_prefix == show_URI, feature_name] = np.mean([val_array])
                        
            # Remove the episode directory
            os.rmdir(subdir_path)

# Export to CSV
df.to_csv(outfile_name)   
