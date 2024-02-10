import os
import random

# Path to the generated filename list
filename_list_path = './data/training/agroNav_LineDetection_train.txt'

# Percentage of data to be used for validation
validation_percentage = 20

# Read the list of filenames
with open(filename_list_path, 'r') as file:
    filenames = file.readlines()
    
# Shuffle the filenames
random.shuffle(filenames)

# Calculate the number of filenames for validation
num_validation_samples = int(len(filenames) * (validation_percentage / 100))

# Split the list into training and validation sets
validation_filenames = filenames[:num_validation_samples]
training_filenames = filenames[num_validation_samples:]

# Write the filenames to separate .txt files for training and validation
with open('./data/training/agroNav_LineDetection_train.txt', 'w') as train_file:
    train_file.writelines(training_filenames)

with open('./data/training/agroNav_LineDetection_val.txt', 'w') as val_file:
    val_file.writelines(validation_filenames)
