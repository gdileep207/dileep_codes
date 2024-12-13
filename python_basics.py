import pandas as pd
import os
import glob

# Folder where your CSV files are located
csv_folder = "E:/Dileep/csvfiles"  # Example for Windows

# Create a pattern to match all CSV files
csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

# Create an Excel writer object to write multiple sheets
with pd.ExcelWriter('master_excel_file.xlsx', engine='xlsxwriter') as writer:
    # Loop through the CSV files and read them
    for file in csv_files:
        # Read each CSV file into a DataFrame
        df = pd.read_csv(file)
        
        # Use the file name (without extension) as the sheet name
        sheet_name = os.path.splitext(os.path.basename(file))[0]
        
        # Write DataFrame to individual sheet in the Excel file
        df.to_excel(writer, sheet_name=sheet_name, index=False)

# The Excel file will be saved as 'master_excel_file.xlsx' in your current working directory

