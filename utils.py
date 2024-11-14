import os
import pandas as pd

# Specify the folder containing the CSV files
folder_path = './static/nba'  # Adjust to your folder path

# List to store data from each file
data_frames = []

# Loop over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):  # Only process CSV files
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)  # Read each CSV file
        data_frames.append(df)       # Append the DataFrame to the list

# Concatenate all DataFrames in the list
combined_df = pd.concat(data_frames, ignore_index=True)

# Specify the output path for the combined CSV
output_file = './static/combined.csv'  # Adjust the output file path as needed

# Save the combined data to a new CSV file
combined_df.to_csv(output_file, index=False)

print(f'All files have been concatenated into {output_file}')

